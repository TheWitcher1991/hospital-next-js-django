from graphene import Schema

from graphql.mutations import Mutation
from graphql.queries import Query

schema = Schema(query=Query, mutation=Mutation)
