from django.urls import path

from .views import normalViews, clientViews

urlpatterns = [
    path('guestconfirm', normalViews.GuestConfirm.as_view(), name='guest-confirm'),
    path('info', normalViews.InfoRetrieve.as_view(), name='info'),
    path('', clientViews.RetrieveUpdateDelEvent.as_view(), name='delete'),
    path('prog', clientViews.CreateProg.as_view(), name='prog-create'),
    path('prog/<id>', clientViews.RetrieveUpdateDelProg.as_view(), name='prog-methods'),
    path('service', clientViews.CreateService.as_view(), name='service-create'),
    path('service/<id>', clientViews.RetrieveUpdateDelService.as_view(), name='service-methods'),
    path('location', clientViews.CreateLocation.as_view(), name='location-create'),
    path('location/<id>', clientViews.RetrieveUpdateDelLocation.as_view(), name='location-methods'),
    path('editor', clientViews.CreateEditor.as_view(), name='editor-create'),
    path('editor/<id>', clientViews.RetrieveUpdateDelEditor.as_view(), name='editor-delete'),
    path('image', clientViews.CreateImage.as_view(), name='image-create'),
    path('image/<id>', clientViews.DeleteImage.as_view(), name='image-delete'),
    path('admin', clientViews.AdminPage.as_view(), name='admin-page'),
]
