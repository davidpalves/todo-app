from django.urls import path 

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodoViewSet, base_name='todos')
urlpatterns = router.urls
