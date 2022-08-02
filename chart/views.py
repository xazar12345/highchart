from django.shortcuts import render
from django.http import JsonResponse
from .models import Staff

def index(request):
	return render(request, 'chart/analytics.html')

def pie_chart(request):
    adult_staff = Staff.objects.filter(age__lt=40).count()
    old_staff = Staff.objects.filter(age__gte=40).count()
    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Analytics of Staff'},
        'series': [{
            'data': [{
            'y': 100,
            'name': "Adult staff",
            'color': '#1C3FAA'
        }, {
            'y': 50,
            'name': "Old staff",
            'color': "#FBC500"
        }]
        }]
    }
    return JsonResponse(chart)
