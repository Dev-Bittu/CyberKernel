from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def terms_and_conditions(request):
	return render(request, 'cyberkernel/terms_and_conditions.html')	

def about(request):
	return HttpResponse('about page')	


def help_and_feedback(request):
	return HttpResponse('help&feedback')