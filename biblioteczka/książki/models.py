from django.db import models

class Autor(models.Model):
    id = models.IntegerField(primary_key=True)
    imię = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=60)
    url = models.URLField(max_length=180)
    notatki = models.TextField(null=True)

    class Meta: 
        verbose_name_plural = "Autors"
        ordering = ['nazwisko'] 
    
    def __str__(self):
        return f"{self.imię} {self.nazwisko}".strip()


class Osoba(models.Model):
    id = models.IntegerField(primary_key=True)
    imię = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=60)
    telefon = models.CharField(max_length=20)
    notatki = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Osoby"

    def __str__(self):
        return f"{self.imię} {self.nazwisko}".strip()
        
class Książka(models.Model):
    JAKOŚĆ=[
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    ]
    STAN=[
        ('chciana', 'chciana'),
        ('do przeczytania', 'do przeczytania'),
        ('czytana', 'czytana'),
        ('przeczytana', 'przeczytana'),
    ]
    id = models.IntegerField(primary_key=True)
    tytuł = models.CharField(max_length=60)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    isbn = models.CharField(max_length=30)
    jakość = models.IntegerField(choices=JAKOŚĆ, null=True)
    właściciel = models.ForeignKey(Osoba, on_delete=models.PROTECT)
    stan = models.CharField(choices=STAN)
    notatki = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Ksiąki"
        ordering = ['tytuł']

    def __str__(self):
        return self.tytuł

class Wypozyczenie(models.Model):
    JAKOŚĆ = [(i, i) for i in range(1, 11)]

    ksiazka = models.ForeignKey(Książka, on_delete=models.CASCADE)
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    data_wypozyczenia = models.DateField(auto_now_add=True)
    data_zwrotu = models.DateField(null=True, blank=True)
    jakość_wypozyczenia = models.IntegerField(choices=JAKOŚĆ, null=True, blank=True)
    jakość_zwrotu = models.IntegerField(choices=JAKOŚĆ, null=True, blank=True)
    notatki = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-data_wypozyczenia']

    def __str__(self):
        return f"{self.ksiazka} - {self.osoba}"
