from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientRequests.as_view(), name='client-root'),
    path('create', views.EventCreate.as_view(), name='Event-create'),
]
