import graphene
from graphene import ObjectType, Mutation
from graphene_django import DjangoObjectType
from todos.models import ToDo, Project
from users.models import User


# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value='Hi')
#
# schema = graphene.Schema(query=Query)


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        Typefields = "__all__"


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        Typefields = "__all__"


class UserType(DjangoObjectType):
    class Meta:
        model = User
        Typefields = "__all__"

# Мутации (запросы на изменение):
class UserMutation(graphene.Mutation):
    class Arguments: # Arguments - это то, что передаём или изменяем при мутации
        birthday = graphene.Int(required=False)
        id = graphene.ID()
        email = graphene.String(required=False)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, birthday, id):
        user = User.objects.get(pk=id)
        user.birthday = birthday
        user.save()
        return UserMutation(user=user)

class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()

# Запросы на получение:
class Query(ObjectType):
    # Названия полей
    all_todos = graphene.List(ToDoType)
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    # Методы-резолверы (обработчики для названий полей):
    def resolve_all_todos(self, info):
        return ToDo.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None


schema = graphene.Schema(query=Query, mutation=Mutation)
