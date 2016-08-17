# coding=utf-8
from django.db import models


# Create your models here.


class autobus(models.Model):
    class Meta:
        verbose_name = "Автобус"
        verbose_name_plural = "Автобусы"

    regnum = models.CharField(max_length='6', verbose_name="Регистрационный номер")

    def __unicode__(self):
        return self.regnum


class counter(models.Model):
    class Meta:
        verbose_name = "Счетчик"
        verbose_name_plural = "Счетчики"

    datetime = models.DateTimeField(blank=True)
    counter = models.IntegerField(default='0', null=True)
    latitude = models.FloatField(blank=True, null=True)
    longtitude = models.FloatField(blank=True, null=True)
    duration = models.DurationField(default='0', null=True)
    kilometrage = models.FloatField(default='0', null=True)
    bus = models.ForeignKey(autobus, verbose_name='Автобус')

    def __unicode__(self):
        return self.counter


class driver(models.Model):
    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"

    firstname = models.CharField(max_length=20, verbose_name='Имя')
    lastname = models.CharField(max_length=20, verbose_name='Фамилия')
    bus = models.ForeignKey(autobus, verbose_name='Автобус')

    def __unicode__(self):
        return self.lastname + ' ' + self.firstname

class page(models.Model):
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.CharField(max_length=10000000, verbose_name="Контент")
    alias = models.CharField(max_length=20, verbose_name="Имя шаблона")

    def __unicode__(self):
        return self.alias
