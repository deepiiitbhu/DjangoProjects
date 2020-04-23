'''
from django.urls import path
from .views import PostList, PostDetail, UserDetail, UserList


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    # Added new User

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

]

'''

from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')
urlpatterns = router.urls