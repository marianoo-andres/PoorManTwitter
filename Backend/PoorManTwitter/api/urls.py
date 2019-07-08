from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tweets', views.TweetViewSet)
urlpatterns = router.urls