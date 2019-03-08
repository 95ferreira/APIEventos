from rest_framework import serializers
from django.contrib.auth.models import User
from eventManager.models import Type, Event, Prog, Guests, Companions, Service, Images, Editor, Location

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		extra_kwargs = {
			'password': {'write_only': True},
		}


class TypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Type
		fields = ("id", "tp")

class ImagesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Images
		exclude = ('eventFk', )

	def create(self, validated_data):
		event = self.context.get('eventFk') 
		image = Images.objects.create(eventFk_id=event, **validated_data)
		return image


class ProgSerializer(serializers.ModelSerializer):

	class Meta:
                model = Prog
                fields = ('id', 'time', 'descr')

	def create(self, validated_data):
		event = self.context.get('eventFk') 
		prog = Prog.objects.create(eventFk_id=event, **validated_data)
		return prog

class ServiceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Service
		exclude = ('eventFk', )

	def create(self, validated_data):
		event = self.context.get('eventFk')
		service = Service.objects.create(eventFk_id=event, **validated_data)
		return service


class LocationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Location
		exclude = ('eventFk',)

	def create(self, validated_data):
		event = self.context.get('eventFk')
		location = Location.objects.create(eventFk_id=event, **validated_data)
		return location

class EventSerializer(serializers.ModelSerializer):

	images = ImagesSerializer(many=True, read_only=True)
	prog = ProgSerializer(many=True, read_only=True)
	service = ServiceSerializer(many=True, read_only=True)
	location = LocationSerializer(many=True, read_only=True)

	class Meta:
		model = Event
		fields = ('text', "numInvitation",  'service', 'url', 'prog', 'images', 'tp', 'location')
		lookup_field = 'url'
		extra_kwargs = {
			'tp': {'write_only': True},
			'user:': {'write_only': True}
		}

	def create(self, validated_data):
		request = self.context.get('request')
		event = Event.objects.create(user=request.user, **validated_data)
		return event

class EditorSerializer(serializers.ModelSerializer):

	user = UserSerializer()
	
	class Meta:
		model = Editor
		fields = ('user', 'id')
		read_only = ('id',)

	def create(self, validated_data):
		data = validated_data.pop('user')
		user = User.objects.create_user(**data)
		event = self.context.get('eventFk')
		editor = Editor.objects.create(user=user, eventFk_id=event)
		return editor

	def update(self, instance, validated_data):
		self.context.update({'eventFk': instance.eventFk_id})
		instance.delete()
		return self.create(validated_data)

class CompanionsSerializer(serializers.ModelSerializer):

	class Meta:
                model = Companions
                fields = ('name', 'tp')

class GuestsSerializer(serializers.ModelSerializer):

	companions = CompanionsSerializer(required=False, many=True)

	class Meta:
		model = Guests
		fields = ('name', 'tel', 'email', 'companions')

	def create(self, validated_data):

		companions_data = validated_data.pop('companions')
		guest = Guests(**validated_data)
		guest.eventFk_id = self.context.get('eventFk')
		guest.save()
		for companion in companions_data:
			Companions.objects.create(guest=guest, **companion)
		return guest
