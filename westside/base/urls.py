from . import views

from django.urls import path

urlpatterns = [
     path('', views.index, name='index'),
     path('preschool', views.preschool, name='preschool'),
     path('elementary', views.elementary, name='elementary'),
     path('pricing', views.pricing, name='pricing'),
     path('church', views.church, name='church')

]
