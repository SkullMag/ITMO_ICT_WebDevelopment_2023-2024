from blog_app.views import PostViewSet, UserViewSet, CommentViewSet, FollowViewSet, UsernameViewSet
from rest_framework.routers import DefaultRouter
from djoser.views import UserViewSet

r = DefaultRouter()
r.register('users', UserViewSet)
r.register('posts', PostViewSet)
r.register('comments', CommentViewSet)
r.register('follows', FollowViewSet)
r.register('username', UsernameViewSet, basename="username")
urlpatterns = r.urls