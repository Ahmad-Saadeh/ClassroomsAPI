from classes.models import Classroom
from rest_framework.generics import (
	ListAPIView, RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
	)
from .serializers import (
	ClassroomSerializer,ClassroomDetailSerializer,UpdateClassroomSerializer,UserCreateSerializer
	)


class UserCreate(CreateAPIView):
    serializer_class = UserCreateSerializer


class ClassroomList(ListAPIView) :
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer


class ClassroomDetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class CreateClassroom(CreateAPIView) :
	serializer_class = UpdateClassroomSerializer

	def perform_create (self, serializer) :
		serializer.save(teacher=self.request.user)


class UpdateClassroom(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = UpdateClassroomSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class CancelClassroom(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
