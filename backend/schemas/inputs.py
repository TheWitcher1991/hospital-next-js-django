import graphene


class ServiceInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    price = graphene.Decimal()
    employee = graphene.ID()
    service_type = graphene.ID()


class PositionInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    functions = graphene.String()
    salary = graphene.Decimal()
