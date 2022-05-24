from authors.views import AuthorModelViewSet, BiographyModelViewSet, ArticleModelViewSet, BookModelViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from todos.views import ProjectModelViewSet, ToDoModelViewSet

router = DefaultRouter() #Создаёт точку входа
router.register("authors", AuthorModelViewSet) #Регистрируем авторов и ставим сюда конкретные вьюхи.
router.register("users", UserModelViewSet)
router.register('biographies', BiographyModelViewSet)
router.register('articles', ArticleModelViewSet)
router.register('books', BookModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', ToDoModelViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls)), #Мы создали объект класса router и он является основным адресом нашего сайта, при этом админка и авторизация не изменились.
]
