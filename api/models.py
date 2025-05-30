from tastypie.resources import ModelResource
from shop.models import Category, Course
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization


# Create your models here.

class CategoryResourses(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resourse_name = 'categories'
        allowed_methods = ['get']


class CourseResourses(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resourse_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        excludes = ['reviews_qty', 'created_at']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        bundle.obj.category = bundle.data['category']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle
