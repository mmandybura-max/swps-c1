from django.urls import path
from . import książka_api_views, autor_api_views, osoba_api_views

urlpatterns = [
    path('książki/', książka_api_views.książka_lista),
    path('książki/<int:pk>/', książka_api_views.książka_szczegóły),
    path('książki/nowa/', książka_api_views.książka_nowa),
    path('książki/szukaj/<str:phrase>/', książka_api_views.książka_wg_nazwy),

    path('autorzy/', autor_api_views.autor_lista),
    path('autorzy/<int:pk>/', autor_api_views.autor_szczegóły),
    path('autorzy/nowa/', autor_api_views.autor_nowa),
    path('autorzy/szukaj/<str:phrase>/', autor_api_views.autor_wg_nazwy),

    path('osoby/', osoba_api_views.osoba_lista),
    path('osoby/<int:pk>/', osoba_api_views.osoba_szczegóły),
    path('osoby/nowa/', osoba_api_views.osoba_nowa),
    path('osoby/szukaj/<str:phrase>/', osoba_api_views.osoba_wg_nazwy),
]