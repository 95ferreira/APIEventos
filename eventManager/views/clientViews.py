from .baseViews import *
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from eventManager.models import Event, Guests, Prog, Service, Editor, Location
from eventManager.permissions import IsOwner, IsEventRelated, IsEditor, IsEditorCreator
from eventManager.serializers import EventSerializer, GuestsSerializer, ProgSerializer, ServiceSerializer, ImagesSerializer, EditorSerializer, LocationSerializer, TypeSerializer

				# Admin exclusive class views

class AdminPage(RetrieveBase, APIView):

	permission_classes = (IsOwner, IsAuthenticated)

	def get(self, request, url):

		obj = get_object_or_404(self.get_queryset())
		self.check_object_permissions(self.request, obj)
		return Response("test")

class RetrieveUpdateDelEvent(RetrieveBase, RetrieveUpdateDestroyAPIView):

	lookup_field = 'url'
	serializer_class = EventSerializer
	permission_classes = (IsOwner, IsAuthenticated)

class CreateProg(CreateSerializer):

	permission_classes = (IsAuthenticated, IsOwner|IsEditorCreator)
	serializer_class = ProgSerializer

class RetrieveUpdateDelProg(RetrieveUpdateDelSerializer):

	model_class = Prog
	serializer_class = ProgSerializer
	permission_classes = (IsEventRelated|IsEditor, IsAuthenticated)

class CreateService(CreateSerializer):

	permission_classes = (IsAuthenticated, IsOwner|IsEditorCreator)
	serializer_class = ServiceSerializer

class RetrieveUpdateDelService(RetrieveUpdateDelSerializer):

	model_class = Service
	serializer_class = ServiceSerializer
	permission_classes = (IsEventRelated|IsEditor, IsAuthenticated)

class CreateLocation(CreateSerializer):

	permission_classes = (IsAuthenticated, IsOwner|IsEditorCreator)
	serializer_class = LocationSerializer

class RetrieveUpdateDelLocation(RetrieveUpdateDelSerializer):

	model_class = Location
	serializer_class = LocationSerializer
	permission_classes = (IsEventRelated|IsEditor, IsAuthenticated)

class CreateEditor(CreateSerializer):

	permission_classes = (IsAuthenticated, IsOwner)
	serializer_class = EditorSerializer

class RetrieveUpdateDelEditor(RetrieveUpdateDelSerializer):

	model_class = Editor
	serializer_class = EditorSerializer
	permission_classes = (IsEventRelated, IsAuthenticated)

	def destroy(self, request, *args, **kwargs):
		user = self.get_object().user
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class CreateImage(CreateSerializer):

	serializer_class = ImagesSerializer
	permission_classes = (IsOwner, IsAuthenticated)

	def perform_create(self, serializer):

		serializer.save(image=self.request.data.get('image'))

class DeleteImage(RetrieveBase, DestroyAPIView):

	lookup_field = 'id'
	serializer_class = ImagesSerializer
	permission_classes = (IsOwner, IsAuthenticated)

class RetrieveType(RetrieveAPIView):

	serializer_class = TypeSerializer
	permission_classes = (IsAuthenticated)
