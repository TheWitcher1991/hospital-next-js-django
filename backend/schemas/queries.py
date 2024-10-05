import graphene

from core.models import Cabinet, PatientType, Position
from core.models import ServiceType as ServiceCategory
from employee.models import Employee, Service
from patient.models import Patient
from schemas.types import CabinetType, EmployeeType, PositionType, ServiceCategoryType, ServiceType


class Query(graphene.ObjectType):
    employee = graphene.Field(EmployeeType, id=graphene.Int())
    service = graphene.Field(ServiceType, id=graphene.Int())
    cabinet = graphene.Field(CabinetType, id=graphene.Int())
    employees = graphene.List(EmployeeType)
    service_types = graphene.List(ServiceCategoryType)
    patient_types = graphene.List(PatientType)
    services = graphene.List(ServiceType)
    cabinets = graphene.List(CabinetType)
    positions = graphene.List(PositionType)

    def resolve_employee(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Employee.objects.get(id=id)

        return None

    def resolve_service(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Service.objects.get(id=id)

        return None

    def resolve_cabinet(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Cabinet.objects.get(id=id)

        return None

    def resolve_employees(self, info, **kwargs):
        return Employee.objects.all()

    def resolve_service_types(self, info, **kwargs):
        return ServiceCategory.objects.all()

    def resolve_patient_types(self, info, **kwargs):
        return Patient.objects.all()

    def resolve_services(self, info, **kwargs):
        return Service.objects.select_related("employee", "service_type").all()

    def resolve_cabinets(self, info, **kwargs):
        return Cabinet.objects.all()

    def resolve_positions(self, info, **kwargs):
        return Position.objects.all()
