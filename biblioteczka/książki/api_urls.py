from django.urls import path
from . import książka_api_views

urlpatterns = [
    path('książki/', książka_api_views.książka_lista),
    path('książki/<int:pk>/', książka_api_views.książka_szczegóły),
    path('książki/nowa/', książka_api_views.książka_nowa),
    path('książki/szukaj/<str:phrase>/', książka_api_views.książka_wg_nazwy),
]