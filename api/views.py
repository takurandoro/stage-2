from rest_framework import generics
from .models import Room, Resident, Student
from .serializers import (
    ResidentSerializer,
    RoomSerializer,
    StudentSerializer,
    StudentLoginSerializer,
)
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .filters import *
from django_filters import rest_framework as filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

# Create your views here.


class CreateStudentAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # use the basic authentication
    authentication_classes = [BasicAuthentication, SessionAuthentication]


class LoginAPIView(generics.CreateAPIView):
    serializer_class = StudentLoginSerializer
    # use the basic authentication
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    def post(self, request):

        try:
            student = Student.objects.get(email=request.data["email"])
        except Student.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Invalid email",
                }
            )
        if not student.check_password(request.data["password"]):
            return Response(
                {
                    "success": False,
                    "message": "Password incorrect",
                }
            )

        token, created = Token.objects.get_or_create(user=student)
        serializer = StudentLoginSerializer(instance=student)
        return Response(
            {
                "success": True,
                "message": "Logged in Successfuly",
                "token": token.key,
                "student": serializer.data,
            }
        )


class LogoutAPIView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response({"message": "logged out successfuly"})


class StudentProfileAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # allow Authenticated user
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


class ResidentCreateAPIView(generics.CreateAPIView):
    model = Resident
    serializer_class = ResidentSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # Allow only authenticated users
    permission_classes = [IsAuthenticated]


# paginatioin
class ResidentListAPIView(generics.ListAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # allow any user
    permission_classes = [AllowAny]

    # set limitation for retrieving data
    pagination_class = LimitOffsetPagination


class ResidentDetailAPIView(generics.RetrieveAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    lookup_url_kwarg = "resident_id"


class ResidentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    lookup_url_kwarg = "resident_id"
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # Allow only authenticated users
    permission_classes = [IsAuthenticated]


class ResidentDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    lookup_url_kwarg = "resident_id"
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # allow only Admin
    permission_classes = [IsAdminUser]


# filter Resident fields
class FilterResidentListAPIView(generics.ListAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ResidentFilter


class RoomCreateAPIView(generics.CreateAPIView):
    model = Room
    serializer_class = RoomSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # Allow only authenticated users
    permission_classes = [IsAuthenticated]


# Caching concept
class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # allow any user
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer
        ser = serializer(rooms, many=True)
        return Response(ser.data)


class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "room_id"


class RoomUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "room_id"
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # Allow only authenticated users
    permission_classes = [IsAuthenticated]


class RoomDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "room_id"
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # allow only Admin
    permission_classes = [IsAdminUser]


# filter Room fields
class FilterRoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RoomFilter
