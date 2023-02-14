from django.conf import settings
from django.db import models
from django.utils import timezone


class Post1(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200)
    task = models.TextField()


class Table(models.Model):
    table = models.CharField(max_length=200)
    table1 = models.CharField(max_length=200)
    table2 = models.CharField(max_length=200)
    table3 = models.CharField(max_length=200)
    table4 = models.CharField(max_length=200)
    table5 = models.CharField(max_length=200)
    table6 = models.CharField(max_length=200)
    table7 = models.CharField(max_length=200)
    table8 = models.CharField(max_length=200)
    table9 = models.CharField(max_length=200)
    table10 = models.CharField(max_length=200)
    table11 = models.CharField(max_length=200)
    table12 = models.CharField(max_length=200)
    time = models.TextField()
