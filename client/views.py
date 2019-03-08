from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

from eventManager.serializers import EventSerializer

class ClientRequests(APIView):

	permission_classes = (IsAuthenticated,)

	def get(self, request):
		return Response("client")

class EventCreate(CreateAPIView):

	permission_classes = (IsAuthenticated, )
	serializer_class = EventSerializer
