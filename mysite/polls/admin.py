from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    min_num = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
