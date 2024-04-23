from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Student
from .serializers import StudentSerializer


class StudentPagination(PageNumberPagination):
    page_size = 30


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_student(request, telegram_id):
    try:
        student = Student.objects.get(telegramId=telegram_id)
    except Student.DoesNotExist:
        return Response(status=404)

    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_student(request, telegram_id):
    try:
        student = Student.objects.get(telegramId=telegram_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(status=404)
    

@api_view(['GET'])
def get_all_students(request):
    paginator = StudentPagination()
    students = Student.objects.all()
    result_page = paginator.paginate_queryset(students, request)
    serializer = StudentSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)