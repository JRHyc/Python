# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        my_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first'] = "First name must be at least 2 characters long"
        if len(postData['last_name']) < 2:
            errors['last'] = "Last name must be at least 2 characters long"
        if not my_re.match(postData['email']):
            errors['email'] = "Please enter a valid email address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
