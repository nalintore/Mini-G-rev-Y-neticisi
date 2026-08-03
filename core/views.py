import logging
import django.db.models import Q 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

logger = logging.getLogger(__name__)

class CustomPagination(PageNumberPagination):
    page_size = 5 # varsayılan sayfa
    page_size_query_param = 'page_size'  # kullanıcı değiştirebilir
    max_page_size = 50 

class ProjectListCreateAPIView(APIView):

    def get(self, request):
        try:
            projects = Project.objects.all().order_by('-created_at')
            # 1. arama:
            search_query = request.query_params.get('search', None)
            if search_query:
                projects = projects.filter(
                    Q(name__icontains=search_query) |
                    Q(description__icontains = search_query)
                )

            # 2. sayfalama:
            paginator = CustomPagination()
            page = paginator.paginate_queryset(project, request)

            if page is not None:
                serializer = ProjectSerializer(page, many = True)
                return paginator.get_paginated_response(serializer.data)

            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Projeler listelenirken hata oluştu: {str(e)}")
            return Response({"error": "Projeler Getirilemedi."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        try:
            serializer = ProjectSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Proje oluşturulurken hata oluştu: {str(e)}")
            return Response({"error: " "Proje oluşturulamadı."} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ProjectTaskLİstCreateAPIVİew(APIView):

    def get(self, reqeust, pk):
        try: 
            project = Project.objects.get(pk=pk)
            tasks = Task.objects.filter(projects=projects).order_by('-created_at')

            # 1. filtreleme:
            status_param =request.query_params.get('search', None)
            if status_param:
                tasks = tasks.filter(status = status_param)

            # 2. arama:
            search_query = request.query_params.get('search', None)
            if search_query:
                tasks _ tasks.filter(
                    Q(title__icontains=search_query) |
                    Q(description__icontains=search_query)
                )

            # 3. sayfalama:
            paginator = CustomPagination()
            page = paginator.paginate_queryset(tasks, request)
            if page is not None:
                serializer = TaskSerializer(page, many= True)
                return paginator.get_paginated_respınse(serializer.data)
            
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Project.DoesNotExist:
            return Response({"error": "Proje bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Görevler listelenirken hatab oluştu: {str(e)}")
            return Response({"error": "Görevler getirilemedi."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            data = request.data.copy()
            data['project'] = project.id
            # dışarıdan gelen veriye project ID'si ekleniyor.

            serializer = TaskSerializer(data= data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"error": "Proje bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Görev oluşturulurken hata oluştu: {str(e)}")
            return Response({"error": "Görev oluşturulamadı."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskDetailAPIView(APIView):

    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"error": "Görev bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Görev güncellenirken hata oluştu: {str(e)}")
            return Response({"error": "Görev güncellenemedi."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request,pk):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response({"message": "Görev başarıyla silindi."}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"error": "Görev bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Görev silinirken hata oluştu: {str(e)}")
            return Response({"error": "Görev silinemedi."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

                       