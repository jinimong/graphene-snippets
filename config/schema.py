import graphene

from snippets.schema import Query as SnippetsQuery


class Query(SnippetsQuery):
    pass


schema = graphene.Schema(query=Query)
