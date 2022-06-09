"""
todo project URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views as vw
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authors.views import ArticleModelViewSet, AuthorModelViewSet, BiographyModelViewSet, BookModelViewSet
from todos.views import ProjectModelViewSet, ToDoModelViewSet
from users.views import UserCustomViewSet

router = DefaultRouter()  # Создаёт точку входа
router.register("authors", AuthorModelViewSet)  # Регистрируем авторов и ставим сюда конкретные вьюхи.
router.register("users", UserCustomViewSet)
router.register("biographies", BiographyModelViewSet)
router.register("articles", ArticleModelViewSet)
router.register("books", BookModelViewSet)
router.register("projects", ProjectModelViewSet)
router.register("todos", ToDoModelViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Authorization
    path("api/auth/", include("rest_framework.urls")),
    # Token Authorization
    path("api/token-auth/", vw.obtain_auth_token),
    # JWT token Authorization
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Other
    path("", include(router.urls)),  # Мы создали объект класса router и он
    # является основным адресом нашего сайта, при этом админка и авторизация не изменились.
]
