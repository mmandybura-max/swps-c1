from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Książka, Autor, Osoba, Wypozyczenie


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
        return render(request, "autor/lista.html", {"autorzy": autorzy})

def autor_szczegóły(request, id):
    autor = Autor.objects.get(id=id)

    return render(request, 
                  "autor/szczegóły.html",
                  {'autor': autor})

def osoba_lista(request):
    osoby = Osoba.objects.all()
    return render(request, "osoba/lista.html",
                  {"osoby": osoby})

def osoba_szczegóły(request, id):
    osoba =Osoba.objects.get(id=id)
    return render(request, "osoba/szczegóły.html", {"osoba": osoba})

def wypozyczenie_lista(request):
    wypozyczenia = Wypozyczenie.objekts.all()
    return render(request, "wypozyczenie/lista.html", 
                  {"wypozyczenia": wypozyczenia})
def wypozyczenie_szczegóły(request, id):
    wypozyczenie = Wypozyczenie.objects.get(id=id)
    return render(request, "wypozyczenie/szczegóły.html", {"wypozyczenie": wypozyczenie})
