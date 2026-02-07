from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Autor, Książka
from .serializers import AutorSerializer, KsiążkaSerializer


@api_view(['GET'])
def autor_lista(request):
    """
    Lista wszystkich obiektów modelu Autor.
    """
    autorzy = Autor.objects.all()
    serializer = AutorSerializer(autorzy, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def autor_szczegóły(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Autor
    :return: Response (with status and/or object/s data)
    """
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Autor.
    """
    if request.method == 'GET':
        autor = Autor.objects.get(pk=pk)
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def autor_książki(request, pk):

    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    książki = Książka.objects.filter(autor=autor)
    serializer = KsiążkaSerializer(książki, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def autor_nowa(request):
    serializer = AutorSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def autor_wg_nazwy(request, fraza):
    autorzy = Autor.objects.filter(nazwisko__icontains=fraza) | Autor.objects.filter(imię__icontains=fraza)
    serializer = AutorSerializer(autorzy, many=True)
    return Response(serializer.data)