from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My courses"
admin.site.index_title = "Admin"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = models.Course
    extra = 1
    exclude = ['created_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
