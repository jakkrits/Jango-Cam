import graphene
from graphene_django import DjangoObjectType

from graphql import GraphQLError

# django database query utils
from django.db.models import Q

from .models import Link, Vote
from users.schema import UserType


# Types
class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


# Query
class Query(graphene.ObjectType):
    links = graphene.List(
        LinkType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int()
    )

    votes = graphene.List(VoteType)

    def resolve_links(self, info, search=None, first=None, skip=None, **kwargs):
        qs = Link.objects.all()

        # value passed in search argument --> *arg
        if search:
            filter = (
                    Q(url__icontains=search) | Q(description__icontains=search)
            )

            qs = qs.filter(filter)

        if skip:
            qs = qs[skip::]

        if first:
            qs = qs[:first]

        return qs

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


# Mutation
class CreateLink(graphene.Mutation):
    # (A) output data that server can send to client
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    # (B) data that we can send to server
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # (C) arguments defined in Arguments class
    #     to mutate data in the database
    def mutate(self, info, url, description):
        user = info.context.user or None

        link = Link(
            url=url,
            description=description,
            posted_by=user
        )

        link.save()

        # return class with data spec in (A)
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by
        )


class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    link = graphene.Field(LinkType)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('You must be logged in to vote!')

        link = Link.objects.filter(id=link_id).first()
        if not link:
            # instead of exception, we can use GraphQLError
            raise GraphQLError('Invalid Link')

        Vote.objects.create(
            user=user,
            link=link
        )

        return CreateVote(
            user=user,
            link=link
        )


# create mutation class with field to be resolved.
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()
