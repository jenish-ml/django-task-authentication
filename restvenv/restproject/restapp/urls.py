from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('task', TaskViewSet)
router.register('completed_task', CompletedTaskViewSet)
router.register('user', UserTaskViewSet)
router.register('due_task', DueTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    