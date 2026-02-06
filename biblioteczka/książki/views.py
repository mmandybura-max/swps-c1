from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Książka, Autor, Osoba, Wypożyczenie


def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)


def książka_lista(request):
    książki = Książka.objects.all()
    return render(request,
                  "książki/lista.html",
                  {'książki': książki})

def książka_szczegóły(request, id):
    książka = Książka.objects.get(id=id)

    return render(request,
                  "książki/szczegóły.html",
                  {'książka': książka})\
                  
def autor_lista(request):
    if request.method == "GET":
        autorzy = Autor.objects.all()
        return render(request, "autorzy/lista.html", {"autorzy": autorzy})

def autor_szczegóły(request, id):
    autor = Autor.objects.get(id=id)

    return render(request, 
                  "autorzy/szczegóły.html",
                  {'autor': autor})

def osoba_lista(request):
    osoby = Osoba.objects.all()
    return render(request, "osoby/lista.html",
                  {"osoby": osoby})

def osoba_szczegóły(request, id):
    osoba =Osoba.objects.get(id=id)
    return render(request, "osoby/szczegóły.html", {"osoba": osoba})

def wypożyczenie_lista(request):
    wypożyczenia = Wypożyczenie.objekts.all()
    return render(request, "wypożyczenia/lista.html",
                  {"wypożyczenia": wypożyczenia})

def wypożyczenie_szczegóły(request, id):
    wypożyczenie = Wypożyczenie.objects.get(id=id)
    return render(request, "wypożyczenia/szczegóły.html", {"wypożyczenie": wypożyczenie})
