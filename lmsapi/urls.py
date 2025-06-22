from django.urls import path
from lmsapi.views import TeacherApiView, TeacherApiListCreateView

urlpatterns = [
    path('teacher/list/', TeacherApiListCreateView.as_view(), name='api.teacher.list'),
    path('teacher/create/', TeacherApiListCreateView.as_view(), name='api.teacher.create'),
    path('teacher/<int:pk>/detail/', TeacherApiView.as_view(), name='api.teacher.detail'),
    path('teacher/<int:pk>/update/', TeacherApiView.as_view(), name='api.teacher.update'),
    path('teacher/<int:pk>/delete/', TeacherApiView.as_view(), name='api.teacher.delete'),
    path('teacher/create/', TeacherApiView.as_view(), name='api.teacher.create'),
]
