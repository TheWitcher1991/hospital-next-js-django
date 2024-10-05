import graphene

from core.models import Position
from core.models import ServiceType as ServiceCategory
from employee.models import Employee, Service
from schemas.inputs import PositionInput, ServiceInput
from schemas.types import PositionType, ServiceType


class CreateService(graphene.Mutation):
    class Arguments:
        input = ServiceInput(required=True)

    ok = graphene.Boolean()
    service = graphene.Field(ServiceType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        employee_instance = Employee.objects.get(id=input.employee)
        service_type_instance = ServiceCategory.objects.get(id=input.service_type)
        service_instance = Service(
            name=input.name,
            price=input.price,
            employee=employee_instance,
            service_type=service_type_instance,
        )
        service_instance.save()
        return CreateService(
            ok=ok,
            service=service_instance,
        )


class CreatePosition(graphene.Mutation):
    class Arguments:
        input = PositionInput(required=True)

    ok = graphene.Boolean()
    position = graphene.Field(PositionType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        position_instance = Position.objects.create(
            name=input.name,
            functions=input.functions,
            salary=input.salary,
        )
        position_instance.save()
        return CreatePosition(
            ok=ok,
            position=position_instance,
        )


class UpdatePosition(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PositionInput(required=True)

    ok = graphene.Boolean()
    position = graphene.Field(PositionType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        position_instance = Position.objects.get(id=id)
        if position_instance:
            ok = True
            position_instance.name = input.name
            position_instance.functions = input.functions
            position_instance.salary = input.salary
            position_instance.save()
            return UpdatePosition(
                ok=ok,
                position=position_instance,
            )
        return UpdatePosition(
            ok=ok,
            position=None,
        )


class Mutation(graphene.ObjectType):
    create_service = CreateService.Field()
    create_position = CreatePosition.Field()
    update_position = UpdatePosition.Field()
