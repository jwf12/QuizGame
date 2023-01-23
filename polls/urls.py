from django.urls import path
from . import views


app_name='polls'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pk>', views.DetailView.as_view(), name='numPreg'),
    path('<question_id>/vote', views.vote, name='vote'),
    # path('<question_id>/results', views.results, name='results'),
]