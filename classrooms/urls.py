from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView
)

from APIclasses.views import(
UserCreate,ClassroomList,ClassroomDetail,CancelClassroom,CreateClassroom,UpdateClassroom
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

# API urls
    path('login/', TokenObtainPairView.as_view(), name="api-login"),
    path('register/', UserCreate.as_view(), name="api-register"),
    path('classroom', ClassroomList.as_view(), name="api-classroom-list"),
    path('classroom/<int:classroom_id>/', ClassroomDetail.as_view(), name="api-classroom-detail"),
    path('classroom/create/', CreateClassroom.as_view(), name="api-classroom-create"),
    path('classroom/<int:classroom_id>/update/', UpdateClassroom.as_view(), name="api-classroom-update"),
    path('classroom/<int:classroom_id>/cancel/', CancelClassroom.as_view(), name="api-classroom-delete"),
]


if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
