from django.urls import path

from . import views

app_name = 'polls'

# 해당 앱에 대한 URL 패턴을 생성하고 연결한다. 
#  <question_id> 에서 <pk> 로 변경
urlpatterns = [
  # ex: /polls/
  path('', views.IndexView.as_view(), name='index'),
  # ex: /polls/5/  이때 question_id은 뷰에서 넘어온 데이터 임 
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  # ex: /polls/5/results/
  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
  # ex: /polls/5/vote/
  path('<int:question_id>/vote/', views.vote, name='vote'),
]