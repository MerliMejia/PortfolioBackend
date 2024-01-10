from dotenv import load_dotenv

import graphene

load_dotenv()

class Queries(graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass

schema = graphene.Schema(query=Queries, mutation=Mutation)
