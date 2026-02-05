from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Osoba, Wypożyczenie
from .serializers import OsobaSerializer, WypożyczenieSerializer


@api_view(['GET'])
def osoba_lista(request):
    """
    Lista wszystkich obiektów modelu Osoba.
    """
    osoby = Osoba.objects.all()
    serializer = OsobaSerializer(osoby, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def osoba_szczegóły(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Osoba
    :return: Response (with status and/or object/s data)
    """
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Osoba.
    """
    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def osoba_wypożyczenia(request, pk):

    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    wypożyczenia = Wypożyczenie.objects.filter(osoba=osoba)
    serializer = WypożyczenieSerializer(wypożyczenia, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def osoba_nowa(request):
    serializer = OsobaSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def osoba_wg_nazwy(request, fraza):
    osoby = Osoba.objects.filter(tytuł__icontains=fraza)
    serializer = OsobaSerializer(osoby, many=True)
    return Response(serializer.data)