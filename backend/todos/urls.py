from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, base_name='tasks')
router.register('', views.TodoViewSet, base_name='todos')

urlpatterns = router.urls
