from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet, RegisterUserView, LoginUserView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/users/register/', RegisterUserView.as_view(), name='register'),
    path('api/users/login/', LoginUserView.as_view(), name='login'),
    path('', include(router.urls)),
]
