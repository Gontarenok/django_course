# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json

from django.conf import settings
from django.views.generic import View, TemplateView
from datetime import datetime


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)

        # contex['news_title'] = 'Первый пробный заголовок'
        # contex['news_preview'] = 'Предварительное описание для первой новости'
        #
        # contex['range'] = range(5)
        # contex['datetime_obj'] = datetime.now()

        # Task 6
        with open(settings.BASE_DIR / 'news.json', encoding="utf-8") as news_file:
            contex['object_list'] = json.load(news_file)
        return contex

    # Task 7
    def get(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        if query:
            return HttpResponseRedirect(f'https://google.ru/search?q={query}')

        return super().get(*args, **kwargs)


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
