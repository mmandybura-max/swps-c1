from django.contrib import admin

# Register your models here.
from .models import Autor, Osoba, Książka, Wypożyczenie

admin.site.register(Autor)
admin.site.register(Osoba)
admin.site.register(Książka)
admin.site.register(Wypożyczenie)