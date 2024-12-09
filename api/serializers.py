from rest_framework import serializers
from .models import Room, Resident, Student


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ("id", "name", "size")


class RoomSerializer(serializers.ModelSerializer):
    resident = Resident
    resident_name = serializers.ReadOnlyField(source="resident.name")

    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "floor",
            "room_type",
            "resident_name",
            "resident",
        )
        extra_kwargs = {
            "resident": {"write_only": True},
        }


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "roll_number", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        student = Student.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            roll_number=validated_data["roll_number"],
        )

        student.set_password(validated_data["password"])
        student.save()

        return student


class StudentLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "password", "email")
        extra_kwargs = {
            "password": {"write_only": True},
        }
