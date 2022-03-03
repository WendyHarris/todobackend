from django.urls import include, path
from todo import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

urlpatterns = [
    path(r'^', include(router.urls)),
]