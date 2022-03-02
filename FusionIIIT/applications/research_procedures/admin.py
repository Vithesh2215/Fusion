from django.contrib import admin
from applications.research_procedures.models import Patent
from django.utils.html import format_html

# Adding a custom admin view for patent
class PatentAdmin(admin.ModelAdmin):

    list_filter = ('status',) 
    search_fields = ['title', 'faculty_id', 'application_id']

    def _status(self, obj):
        color = "orange"
        if obj.status == "Approved":
            color = "green"
        elif obj.status == "Disapproved":
            color = "red"
        return format_html('<span style="color: %s"><b>%s</b></span>' % (color, obj.status))

    list_display = ["faculty_id","title","_status"]

# Register your models here.
admin.site.register(Patent,PatentAdmin)