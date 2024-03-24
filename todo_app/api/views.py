from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
# from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import  IsAuthenticated

from todo_app.models import (TaskList, Category)
from todo_app.api.serializers import (TaskListSerializer, 
                                           CategorySerializer)

from todo_app.api.pagination import TaskListCPagination

class TaskListGV(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    pagination_class = TaskListCPagination
    permission_classes = [IsAuthenticated]

class TaskListAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        movies = TaskList.objects.all()
        serializer = TaskListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
         serializer = TaskListSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            movie = TaskList.objects.get(pk=pk)
        except TaskList.DoesNotExist:
            return Response({'Error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = TaskList.objects.get(pk=pk)
        serializer = TaskListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = TaskList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      
    
class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]