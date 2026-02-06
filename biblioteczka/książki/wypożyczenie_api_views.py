from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Wypożyczenie
from .serializers import WypożyczenieSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def wypożyczenie_lista(request):
    """
    Lista wszystkich obiektów modelu Wypożyczenie.
    """
    wypożyczenia = Wypożyczenie.objects.all()
    serializer = WypożyczenieSerializer(wypożyczenia, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def wypożyczenie_szczegóły(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Wypożyczenie
    :return: Response (with status and/or object/s data)
    """
    try:
        wypożyczenie = Wypożyczenie.objects.get(pk=pk)
    except Wypożyczenie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Wypożyczenie.
    """
    if request.method == 'GET':
        wypożyczenie = Wypożyczenie.objects.get(pk=pk)
        serializer = WypożyczenieSerializer(wypożyczenie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WypożyczenieSerializer(wypożyczenie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wypożyczenie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def wypożyczenie_nowa(request):
    serializer = WypożyczenieSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def wypożyczenie_wg_nazwy(request, fraza):
    wypożyczenia = Wypożyczenie.objects.filter(tytuł__icontains=fraza)
    serializer = WypożyczenieSerializer(wypożyczenia, many=True)
    return Response(serializer.data)