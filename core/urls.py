from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    ProjectListCreateAPIView,
    ProjectTaskListCreateAPIView,  # <-- 'İ' harfleri 'I' yapıldı
    TaskDetailAPIView,
)

urlpatterns = [
    # JWT Auth endpointleri
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Proje endpointleri
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/tasks/', ProjectTaskListCreateAPIView.as_view(), name='project-task-list-create'),  # <-- 'İ' harfleri 'I' yapıldı

    # Görev endpointleri
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
]