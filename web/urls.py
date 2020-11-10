from django.urls import path
from . import views

app_name='web'

urlpatterns=[
	path('', views.main, name='main'),
	path('introduction/', views.introduction, name='introduction'),
	path('history/', views.history, name="history"),
	path('map/', views.map, name="map"),
]
