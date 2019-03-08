from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from eventManager.models import Event

class RetrieveBase():

	def get_queryset(self):
		url = self.kwargs['url']
		return Event.objects.filter(url=url)

class CreateSerializer(RetrieveBase, CreateAPIView):

	def get_serializer_context(self):
		context = super(CreateAPIView, self).get_serializer_context()
		obj = get_object_or_404(self.get_queryset())
		self.check_object_permissions(self.request, obj)
		context.update({'eventFk': obj.id})
		return context

class RetrieveUpdateDelSerializer(RetrieveUpdateDestroyAPIView):

	lookup_field = 'id'
	model_class = None

	def get_queryset(self):
		assert(self.model_class != None)
		url = self.kwargs.get('url')
		id = self.kwargs.get('id')
		return self.model_class.objects.filter(id=id,  eventFk__url=url)

