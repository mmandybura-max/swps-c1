from django.urls import path
from . import api_views

urlpatterns = [
    path('książki/', api_views.książka_lista),
    path('książki/<int:pk>/', api_views.książka_szczegóły),
    path('książki/nowa/', api_views.książka_nowa),
    path('książki/szukaj/<str:phrase>/', api_views.książka_wg_nazwy),
]