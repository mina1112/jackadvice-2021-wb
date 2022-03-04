from django.urls import path

from rest_framework import routers
from .views import UserViewSet, TaskViewSet, VoiceViewSet 
from praise import views


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'voices', VoiceViewSet)

urlpatterns = [
    path('', views.index, name='index'),
]
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<uuid:User.id>/', views.TaskListView.as_view(), name="List"),
#    path('<uuid:User.id>/<uuid:Tasks.id>/', views.TaskDetailView.as_view(), name="detail"),
#    path('<uuid:User.id>/<uuid:Tasks.id>/delete/', views.TaskDeleteView.as_view(), name="delete"),
#    path('<uuid:User.id>/create/', views.TaskCreateView.as_view(), name="create"),
#    path('<uuid:User.id>/<uuid:Tasks.id>/<uuid:Voices.id>/', views.VoiseUpdateView.as_view(), name="voise_update")
#]
