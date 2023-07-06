# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import View, TemplateView
from datetime import datetime


# def hello_world(request):
#     return HttpResponse('Hello world!')

# class HelloWorldView(View):
#     def get(self, *args):
#         return HttpResponse('Hello world!')

# def check_kwargs(request, **kwargs):
#     return HttpResponse(f'kwargs:<br>{kwargs}')

class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)

        contex['news_title'] = 'Первый пробный заговок'
        contex['news_preview'] = 'Предварительное описание для первой новости'

        contex['range'] = range(5)
        contex['datetime_obj'] = datetime.now()

        return contex


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'
