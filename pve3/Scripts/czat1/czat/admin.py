# -*- coding: utf-8 -*-
# czat/models.py

from django.contrib import admin
from czat import models # importujemy nasz model

# Register your models here.
# Rejsetrujemy model Wiadomosc w panelu administracyjnym

admin.site.register(models.Wiadomosc)