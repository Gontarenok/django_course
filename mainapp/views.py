from django.http import HttpResponse, HttpResponseRedirect
# import json
from mainapp import models as mainapp_models
from django.shortcuts import get_object_or_404

from django.conf import settings
from django.views.generic import TemplateView
from datetime import datetime


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)

        # Task 6
        # with open(settings.BASE_DIR / 'news.json', encoding="utf-8") as news_file:
        #     contex['object_list'] = json.load(news_file)
        # return contex

        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_qs"] = mainapp_models.News.objects.all()[:5]
        return context

    # # Task 7
    # def get(self, *args, **kwargs):
    #     query = self.request.GET.get('q', None)
    #     if query:
    #         return HttpResponseRedirect(f'https://google.ru/search?q={query}')
    #
    #     return super().get(*args, **kwargs)


class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Course.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            mainapp_models.Course, pk=pk
        )
        context["lessons"] = mainapp_models.Lesson.objects.filter(
            course=context["course_object"]
        )
        context["teachers"] = mainapp_models.CourseTeachers.objects.filter(
            course=context["course_object"]
        )
        return context


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'
