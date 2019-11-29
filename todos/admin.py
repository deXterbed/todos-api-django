from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_by')
    list_filter = ['completed']
    search_fields = ['title']
    fieldsets = [
        (None,               {'fields': ['title', 'completed']}),
        ('Author', {'fields': ['created_by']}),
    ]

admin.site.register(Todo, TodoAdmin)
