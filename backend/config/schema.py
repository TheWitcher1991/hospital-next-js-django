import graphene

import schemas


class Query(schemas.schema.Query, graphene.ObjectType):
    pass


class Mutation(schemas.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
