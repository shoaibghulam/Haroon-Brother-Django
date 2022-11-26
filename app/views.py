from django.shortcuts import render , HttpResponse
from django.views import View
# Create your views here.
# def index(request):
#     return HttpResponse("hello world")

class Home(View):
    def get(self,request):
        return render(request,'app/index.html')


class About(View):
    def get(self,reuqest):
        return render(reuqest,'app/about.html')

class Contact(View):
    def get(self,reuqest):
        return render(reuqest,'app/contact.html')