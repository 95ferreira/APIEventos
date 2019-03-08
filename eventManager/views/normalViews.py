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


class GuestConfirm(CreateSerializer):

	lookup_field = 'url'
	serializer_class = GuestsSerializer


class InfoRetrieve(RetrieveBase, RetrieveAPIView):

	lookup_field = 'url'
	serializer_class = EventSerializer

