from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import książka_api_views, autor_api_views, osoba_api_views, wypożyczenie_api_views

urlpatterns = [
    path('książki/', książka_api_views.książka_lista),
    path('książki/<int:pk>/', książka_api_views.książka_szczegóły),
    path('książki/nowa/', książka_api_views.książka_nowa),
    path('książki/szukaj/<str:fraza>/', książka_api_views.książka_wg_nazwy),

    path('autorzy/', autor_api_views.autor_lista),
    path('autorzy/<int:pk>/', autor_api_views.autor_szczegóły),
    path('autorzy/nowa/', autor_api_views.autor_nowa),
    path('autorzy/szukaj/<str:fraza>/', autor_api_views.autor_wg_nazwy),

    path('osoby/', osoba_api_views.osoba_lista),
    path('osoby/<int:pk>/', osoba_api_views.osoba_szczegóły),
    path('osoby/<int:pk>/wypożyczenia/', osoba_api_views.osoba_wypożyczenia),
    path('osoby/nowa/', osoba_api_views.osoba_nowa),
    path('osoby/szukaj/<str:fraza>/', osoba_api_views.osoba_wg_nazwy),

    path('wypożyczenia/', wypożyczenie_api_views.wypożyczenie_lista),
    path('wypożyczenia/<int:pk>/', wypożyczenie_api_views.wypożyczenie_szczegóły),
    path('wypożyczenia/nowa/', wypożyczenie_api_views.wypożyczenie_nowa),
    path('wypożyczenia/szukaj/<str:fraza>/', wypożyczenie_api_views.wypożyczenie_wg_nazwy),

    path('token', obtain_auth_token),
]