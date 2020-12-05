from django.contrib import admin
from .models import Contact, Intro, About

# Register your models here.
admin.site.register(Contact)
admin.site.register(Intro)
admin.site.register(About)