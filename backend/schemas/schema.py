from graphene import Schema

from schemas.mutations import Mutation
from schemas.queries import Query

schema = Schema(query=Query, mutation=Mutation)
