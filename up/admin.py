from django.contrib import admin
from up.models import Database

class UploadAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,           {'fields': ['user']}),
		(None,		     {'fields': ['introduction']}),
		(None,		     {'fields': ['files']}),
		('Date information', {'fields': ['time']}),
    	]
	list_display = ('id','user','introduction','files','time')
	search_fields = ['user']
	date_hierarchy = 'time'
admin.site.register(Database,UploadAdmin)