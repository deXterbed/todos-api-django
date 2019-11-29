from django.urls import path
from rest_framework.routers import DefaultRouter

from .apiviews import TodoViewSet, UserCreate, LoginView

router = DefaultRouter()
router.register('todos', TodoViewSet, base_name='todos')

app_name='todos'
urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]

urlpatterns += router.urls
