from api.models import CategoryResourses, CourseResourses
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name="v1")
course_resourses = CourseResourses()
category_resourses = CategoryResourses()
api.register(course_resourses)
api.register(category_resourses)

urlpatterns = [
    path('', include(api.urls), name='index')
]
