from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Autor, Osoba, Książka, Wypozyczenie

admin.site.register(Autor)
admin.site.register(Osoba)
admin.site.register(Książka)
admin.site.register(Wypozyczenie)