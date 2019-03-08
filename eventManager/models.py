from django.db import models

# Create your models here.

class Type(models.Model):
	tp = models.CharField(max_length=30)

class Event(models.Model):
	numInvitation = models.IntegerField()
	text = models.TextField()
	url = models.CharField(max_length=20, unique=True)
	tp = models.ForeignKey(Type,  on_delete=models.PROTECT)
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Service(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=30, null=True)
	site = models.CharField(max_length=50, null=True)
	descr = models.CharField(max_length=30)
	email = models.EmailField(null=True)
	tel = models.CharField(max_length=20, null=True)
	eventFk = models.ForeignKey(Event, related_name='service', on_delete=models.CASCADE)

class Location(models.Model):
	address = models.CharField(max_length=30)
	num = models.DecimalField(max_digits=19, decimal_places=8)
	eventFk = models.ForeignKey(Event, related_name='location', on_delete=models.CASCADE)	

class Images(models.Model):
	image = models.ImageField(upload_to='static/imgs')
	eventFk = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)

class Prog(models.Model):
	time = models.TimeField()
	descr = models.CharField(max_length=50)
	eventFk = models.ForeignKey(Event, related_name='prog', on_delete=models.PROTECT)

class Editor(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	eventFk = models.ForeignKey(Event, related_name='editor', on_delete=models.CASCADE)

class Guests(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	tel = models.CharField(max_length=20, null=True)
	eventFk = models.ForeignKey(Event, on_delete=models.PROTECT)
	confirmData = models.DateTimeField(auto_now_add=True)

class Companions(models.Model):
	COMP_TYPE_CHOICES = (
		(1, 'Criança'),
		(2, 'Adulto')
	)
	tp = models.CharField(max_length=1, choices=COMP_TYPE_CHOICES)
	name = models.CharField(max_length=50)
	guest = models.ForeignKey(Guests, on_delete=models.PROTECT)
