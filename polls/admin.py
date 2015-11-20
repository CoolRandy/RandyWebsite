from django.contrib import admin
from polls.models import Poll, Choice
# Register your models here.

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	"""docstring for ClassName"""
	model = Choice
	extra = 3
		

class PollAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	fieldsets = [
		(None,     {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

date_hierarchy = 'pub_date'		
admin.site.register(Poll, PollAdmin)

#admin.site.register(Choice)
