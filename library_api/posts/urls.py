from django.urls import path
from .views import UserList,UserDetail, PostList, PostDetail
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

router= SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls

