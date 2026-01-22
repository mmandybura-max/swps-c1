from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Książka
from .serializers import KsiążkaSerializer


@api_view(['GET'])
def książka_lista(request):
    """
    Lista wszystkich obiektów modelu Książka.
    """
    książki = Książka.objects.all()
    serializer = KsiążkaSerializer(książki, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def książka_szczegóły(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Książka
    :return: Response (with status and/or object/s data)
    """
    try:
        książka = Książka.objects.get(pk=pk)
    except Książka.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Książka.
    """
    if request.method == 'GET':
        książka = Książka.objects.get(pk=pk)
        serializer = KsiążkaSerializer(książka)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = KsiążkaSerializer(książka, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        książka.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def książka_nowa(request):
    serializer = KsiążkaSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def książka_wg_nazwy(request, fraza):
    książki = Książka.objects.filter(tytuł__icontains=fraza)
    serializer = KsiążkaSerializer(książki, many=True)
    return Response(serializer.data)