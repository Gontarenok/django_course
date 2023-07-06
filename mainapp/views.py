# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import View, TemplateView
from datetime import datetime


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


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'
