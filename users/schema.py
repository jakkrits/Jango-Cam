from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


# Type
class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


# Query
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not Logged!')

        return user

class Me(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not Logged!')

        return user


# Mutation
class CreateUser(graphene.Mutation):
    # (A) output data that server can send to client
    user = graphene.Field(UserType)

    # (B) data that we can send to server
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    # (C) arguments defined in Arguments class
    #     to mutate data in the database
    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        # return class with data spec in (A)
        return CreateUser(user=user)


# create mutation class with filed to be resolved
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
