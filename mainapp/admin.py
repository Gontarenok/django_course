from django.contrib import admin
from mainapp import models
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'preamble', 'body']


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_course_name', 'num', 'created_at', 'title', 'deleted']
    ordering = ['-course__name', 'num']
    list_per_page = 8
    list_filter = ['course', 'deleted', 'created_at']
    actions = ['mark_deleted', 'mark_active']

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _('Course')

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _('Пометить удаленным')

    def mark_active(self, request, queryset):
        queryset.update(deleted=False)

    mark_active.short_description = _('Восстановить')


@admin.register(models.CourseTeachers)
class CourseTeachersAdmin(admin.ModelAdmin):
    pass