import graphene
from graphene_django import DjangoObjectType

from .models import Link


# Types
class LinkType(DjangoObjectType):
    class Meta:
        model = Link


# Query
class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()


# Mutation
class CreateLink(graphene.Mutation):
    # (A) output data that server can send to client
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    # (B) data that we can send to server
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # (C) arguments defined in Arguments class
    #     to mutate data in the database
    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        # return class with data spec in (A)
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description
        )


# create mutation class with field to be resolved.
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
