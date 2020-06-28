from django.urls import path

from . import views

# 해당 앱에 대한 URL 패턴을 생성하고 연결한다. 
urlpatterns = [
  path('', views.index, name='index')
]