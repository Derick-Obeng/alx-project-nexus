from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('', views.poll_list, name='index'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('<int:poll_id>/results/', views.poll_results, name='results'),



]