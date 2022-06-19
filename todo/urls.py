from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from rest_framework.authtoken import views as vw
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from todos.views import ProjectModelViewSet, ToDoModelViewSet
from users.views import UserCustomViewSet
from graphene_django.views import GraphQLView

router = DefaultRouter()  # Создаёт точку входа
router.register("users", UserCustomViewSet)
router.register("projects", ProjectModelViewSet)
router.register("todos", ToDoModelViewSet)

# Спецификация OpenAPI:
schema_view = get_schema_view(
    openapi.Info(
        title='todo',
        default_version="0.1",
        description="Documentation of our project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True, # Можно делать публичной или приватной
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # Мы создали объект класса router и он является основным адресом нашего сайта, при этом админка и авторизация не изменились.
    # Authorization
    # -- Ordinary Authorization
    path("api-auth/", include("rest_framework.urls")),
    # -- Token Authorization
    path("api-token-auth/", vw.obtain_auth_token),
    # -- JWT token Authorization
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Versioning
    # -- URLPathVersioning - не очень удобно
    #re_path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),
    # -- NamespaceVersioning
    #path('api/users/0.1', include('users.urls', namespace='0.1')),
    #path('api/users/0.2', include('users.urls', namespace='0.2')),
    # -- AcceptHeaderVersioning - самый оптимальный
    path('api/users/', UserCustomViewSet.as_view),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("graphql/", GraphQLView.as_view(graphiql=True), name="graphql"), # graphiql - включить или отключить интерактивный режим
]
