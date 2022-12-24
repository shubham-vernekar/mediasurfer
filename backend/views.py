from .models import Category, Navbar, Series, UserLevelData
from .serializer import CategorySerializer, NavbarSerializer, SeriesSerializer
from .utils import get_pending_videos
from django.utils import timezone
from rest_framework import generics
from django.core.exceptions import FieldError
from django.db.models import Q
from videos.models import Video
from stars.models import Star
from videos.serializer import VideoListSerializer
from stars.serializer import StarSerializer
from rest_framework.response import Response
import os
from django.conf import settings
import json

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get("query", None)
        sort_by = self.request.GET.get("sort_by", None)

        if query:
            qs = qs.filter(Q(title__icontains=query))

        if sort_by:
            try:
                qs = qs.order_by(sort_by)
            except (FieldError):
                return qs.none()

        return qs


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class NavbarListView(generics.ListCreateAPIView):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.order_by("-weight")
        return qs


class SeriesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get("query", None)
        sort_by = self.request.GET.get("sort_by", None)
        cast = self.request.GET.get("cast", None)
        categories = self.request.GET.get("categories", None)

        if query:
            qs = qs.filter(Q(name__icontains=query))

        if sort_by:
            try:
                qs = qs.order_by(sort_by)
            except (FieldError):
                qs = qs.none()

        if cast:
            qs = qs.filter(Q(cast__icontains=cast))

        if categories:
            qs = qs.filter(Q(categories__icontains=categories))

        return qs

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        qs = self.get_queryset()
        all_stars = set()

        for records in qs:
            if records.cast:
                all_stars.update([x for x in records.cast.split(",") if x])

        for k, records in enumerate(response.data["results"]):
            video_qs = Video.objects.filter(series__id=records["id"])
            video_data = VideoListSerializer(video_qs, many=True).data 
            response.data["results"][k]["video_data"] = video_data
            
        response.data["all_stars"] = sorted(list(all_stars))
        return response


class MasterSearchView(generics.GenericAPIView):
    def get(self, request):
        query = request.GET.get("query", None)
        videos, cast, categories = [], [], []

        if query:
            videos = VideoListSerializer(Video.objects.filter(Q(search_text__icontains=query))[:8], many=True).data 
            cast = StarSerializer(Star.objects.filter(Q(name__icontains=query))[:5], many=True).data 
            categories = CategorySerializer(Category.objects.filter(Q(title__icontains=query))[:5], many=True).data 

        return Response({
            "videos": videos,
            "cast": cast,
            "categories": categories,
        })

class RunScanView(generics.GenericAPIView):
    def post(self, request):
        cmd = "start /B start cmd.exe @cmd /c " + '"{}" {} scan'.format(settings.PYTHON_EXE, os.path.join(settings.BASE_DIR, 'manage.py'))
        os.system(cmd)
        return Response({
                "Status": "Success"
            })


class UpdateJson(generics.GenericAPIView):

    def get(self, request):
        labels_data = open(os.path.join(settings.BASE_DIR, 'backend/management/commands/labels.json'),'r').read()
        seeds_data = open(os.path.join(settings.BASE_DIR, 'backend/management/commands/directories.json'),'r').read()

        return Response({
                "labels_data" : labels_data,
                "seeds_data" : seeds_data
            })
    
    def post(self, request, *args, **kwargs):
        filename = request.data.get('filename', False)
        data = request.data.get('data', '') 

        if filename:
            try:
                _ = json.loads(data)
                data_file = open(os.path.join(settings.BASE_DIR, f'backend/management/commands/{filename}.json'),'w')
                data_file.write(data)
                data_file.close()
                return Response({
                        "status": "OK",
                        "message": f"{filename} Updated Successfully",
                    })
            except:
                return Response({
                        "status": "Failed",
                        "message": f"{filename} Update Failed",
                    })

        return Response({
                "status": "Failed",
                "message": f"{filename} Not found"
            })

class CategoryNamesListAPIView(generics.GenericAPIView):
    def get(self, request):
        query = request.GET.get("query", None)
        qs = Category.objects.all()
        if query:
            qs = qs.filter(title__icontains=query)
        
        return Response(qs.values_list('title', flat=True))

class FindPending(generics.GenericAPIView):

    def get(self, request):
        get_data = request.GET.get("get_data", False)

        if get_data == "true":
            pending_videos, unsupported_videos = get_pending_videos()
            return Response({
                "pending" : len(pending_videos),
                "pending_videos" : pending_videos,
                "unsupported" : len(unsupported_videos),
                "unsupported_videos" : unsupported_videos
            })
        else:
            try:
                user_data_object = UserLevelData.objects.latest('update_timestamp')
            except UserLevelData.DoesNotExist:
                user_data_object = UserLevelData()

            if user_data_object.scan_timestamp:
                time_delta = timezone.now() - user_data_object.scan_timestamp
                time_delta_minutes = (time_delta.days*3600*24 + time_delta.seconds)/60
                if time_delta_minutes<60:
                    return Response({
                        "pending" : user_data_object.pending_videos,
                        "unsupported" : user_data_object.unsupported_videos
                    })

            pending_videos, unsupported_videos = get_pending_videos()
            user_data_object.pending_videos = len(pending_videos)
            user_data_object.unsupported_videos = len(unsupported_videos)
            user_data_object.scan_timestamp = timezone.now()
            user_data_object.update_timestamp = timezone.now()
            user_data_object.save()
            return Response({
                "pending" : len(pending_videos),
                "unsupported" : len(unsupported_videos)
            })

