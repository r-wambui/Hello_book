# -*- coding: utf-8 -*- 
from django.db import models


class User(models.Model):
    """docstring for User"""
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    password = models.CharField(max_length=200)



class Book(models.Model):
    """docstring for ClassName"""
    book_name = models.CharField(max_length=50)
    book_category = models.CharField(max_length=150)

