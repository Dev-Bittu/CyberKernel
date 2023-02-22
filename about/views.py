from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from cyberkernel.settings import DEBUG
import logging

logger = logging.getLogger('About')
logger.setLevel(logging.DEBUG) if DEBUG else logger.setLevel(logging.WARNING)
fh = logging.FileHandler('logs/about.log')
formatter = logging.Formatter(
	'[*] {asctime} :: {name} :: {filename} :: {funcName} :: {lineno} :: {levelname:<8} {message}', style='{'
	)
fh.setFormatter(formatter)
logger.addHandler(fh)

def terms_and_conditions(request):
	return render(request, 'cyberkernel/terms_and_conditions.html')	

def about(request):
	logger.critical('visited about')
	return HttpResponse('about page')	


def help_and_feedback(request):
	return HttpResponse('help&feedback')