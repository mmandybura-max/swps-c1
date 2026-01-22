from django.shortcuts import render

from .models import Książka


def książka_lista(request):
    książki = Książka.objects.all()
    return render(request,
                  "książki/lista.html",
                  {'książki': książki})

def książka_szczegóły(request, id):
    książka = Książka.objects.get(id=id)

    return render(request,
                  "książki/szczegóły.html",
                  {'książka': książka})