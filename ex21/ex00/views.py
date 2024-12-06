from django.http import HttpResponse
import datetime

def ola(request):
	html = '<html><body><center><br><br><h1>Hello World!!!</h1></center></body></html>'
	return HttpResponse(html)

def horas(request):
	now = datetime.datetime.now()
	html = f'<html><body>A hora do Brasil: {now}</body></html>'
	return HttpResponse(html)
