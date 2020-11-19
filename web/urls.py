from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='web'

urlpatterns=[
	path('', views.main, name='main'),
	path('menu_1/<str:page>', views.menu_1, name='menu_1'),
	path('menu_2/<str:page>', views.menu_2, name='menu_2'),
	path('menu_3', views.menu_3, name='menu_3'),
	path('menu_3/<int:result_post_pk>', views.detail_result, name='detail_result'),
	path('menu_4', views.menu_4, name='menu_4'),
	path('menu_5', views.menu_5, name='menu_5'),
	path('menu_6/<str:page>', views.menu_6, name='menu_6'),
	path('menu_6/<str:page>/<int:notice_post_pk>', views.detail_notice, name='detail_notice'),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
