from django.urls import path,include
from .views import index, pie_chart

app_name = 'chart'

urlpatterns = [
    path('', index, name='index'),
    path('pie_chart/', pie_chart, name='pie_chart'),
]