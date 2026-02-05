from django.conf import settings
from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("welcome", views.welcome_view),
    path("książki", views.książka_lista),
    path("książki/<int:id>", views.książka_szczegóły),
    path("autory/", views.autor_lista),
    path("autory/<int:id>/", views.autor_szczegóły),
    path("osoby/", views.osoba_lista),
    path("osoby/<int:id>", views.osoba_szczegóły),
    path("wypozyczenia/", views.wypozyczenie_lista),
    path("wypozyczenia/<int:id>/", views.wypozyczenie_szczegóły),
    
]