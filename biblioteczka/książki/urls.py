from django.conf import settings
from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("książki", views.książka_lista),
    path("książki/<int:id>", views.książka_szczegóły),
]