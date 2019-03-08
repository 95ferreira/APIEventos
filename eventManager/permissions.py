from rest_framework import permissions
from eventManager.models import Editor

class IsOwner(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		return obj.user == request.user

class IsEventRelated(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		return obj.eventFk.user == request.user

class IsEditor(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		try:
			editor = Editor.objects.get(user=request.user, eventFk_id=obj.eventFk_id)
			return True
		except Editor.DoesNotExist:
			return False

class IsEditorCreator(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		try:
			editor = Editor.objects.get(user=request.user, eventFk_id=obj.id)
			return True
		except Editor.DoesNotExist:
			return False

