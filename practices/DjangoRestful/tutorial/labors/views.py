# Create your views here.
from labors.models import Labor
from labors.serializers import LaborSerializer
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def add(request):
	labor = Labor.objects.create(name='dingsu')
	labor.save()

	return HttpResponse()

class LaborList(APIView):
    """
    List all labors, or create a new labor.
    """
    def get(self, request, format=None):
        labors = Labor.objects.all()
        serializer = LaborSerializer(labors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LaborSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaborDetail(APIView):
    """
    Retrieve, update or delete a labor instance.
    """
    def get_object(self, pk):
        try:
            return Labor.objects.get(pk=pk)
        except Labor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        labor = self.get_object(pk)
        serializer = LaborSerializer(labor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        labor = self.get_object(pk)
        serializer = LaborSerializer(labor, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        labor = self.get_object(pk)
        labor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)