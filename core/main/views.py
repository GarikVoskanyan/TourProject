from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from calendar import month_name, month_abbr
from .models import *
from .forms import *

class HomeListView(ListView):   
    template_name = 'index.html'

    @staticmethod
    def __extract_all_data(): 
        general_slider = GeneralSlider.objects.all()
        routes = Routes.objects.all()
        pictures = Pictures.objects.all()
        blogDate = BlogDate.objects.all()
        blog = Blog.objects.all()

        for date in blogDate:
            date.month_name = month_abbr[date.date.month]

        context = {
            'general_slider':general_slider,
            'routes':routes,
            'pictures':pictures,
            'blogDate': blogDate,
            'blog':blog,
        }
        print(blogDate)

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        context = self.__extract_all_data()

        return render(request,self.template_name,context)   
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = ContactForm()

        context = self.__extract_all_data()
        context.update({form:'form'})

        return render(request,self.template_name,context) 
