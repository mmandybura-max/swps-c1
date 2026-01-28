from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Książka, Autor


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
                  
def autor_list(request):
    autory = Autor.objects.all()
    imiona = "br".join([f"{a.imię}{a.nazwisko}" for a in autory])
    return HttpResponse(f"<h1>Lista Autorów:</h1>{imiona}")

def autor_szczegóły(request, id):
    autor = Autor.objects.get(id=id)

    return render(request, 
                  "autor/szczegóły.html",
                  {'autor': autor})