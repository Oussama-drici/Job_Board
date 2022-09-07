from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import job
from .serializers import JobSerializer
from rest_framework import generics


@api_view(['GET'])
def job_list_api(request):
    job_list = job.objects.all()
    data = JobSerializer(job_list, many=True).data
    return Response({"data": data})


@api_view(['GET'])
def job_detail_api(request, id):
    job_detail = job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    return Response({'data': data})


class JobListAPI(generics.ListCreateAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer


class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = job.objects.all()
    serializer_class = JobSerializer
