from django.contrib import admin

from .models import Question, Option


class OptionInline(admin.TabularInline):
    model = Option
    extra = 2


class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [OptionInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Question, SurveyAdmin)
