import graphene

import graphql.schema


class Query(graphql.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphql.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
