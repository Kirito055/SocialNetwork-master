from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns=[

		url(r'^$',views.index, name='index'),
		url('homepage/', views.home, name='home'),

		
]