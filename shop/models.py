from django.db import models
from django.utils import timezone

# Create you here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Дата создания')

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    students_qty = models.IntegerField(verbose_name='Количество студентов')
    reviews_qty = models.IntegerField(verbose_name='Количество отзывов')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Дата создания')

    class Meta():
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title
