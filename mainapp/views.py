from django.shortcuts import render

# Create your views here.
def post(requests):
	return render(requests, "mainapp/index.html")
