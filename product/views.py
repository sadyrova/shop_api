from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from product.models import Category, Producty, Review
from product.serializers import CategorySerializer, ProductySerializer, ReviewSerializer, CategoryRetrieveSerializer, ProductyRetrieveSerializer, ReviewRetrieveSerializer

@api_view(['GET'])
def hello_api_view(request):
    return Response(data={'message': 'Hello, its my first Rest API Response:'},
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def category_list_api_view(request):
    product = Category.objects.all()

    data = CategorySerializer(product, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def producty_list_api_view(request):
    product = Producty.objects.all()

    data = ProductySerializer(product, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_list_api_view(request):
    product = Review.objects.all()

    data = ReviewSerializer(product, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def category_retrieve_api_view(request, **kwargs):
    category = Category.objects.get(id=kwargs['id'])

    data = CategoryRetrieveSerializer(category, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def producty_retrieve_api_view(request, **kwargs):
    producty = Producty.objects.get(id=kwargs['id'])

    data = ProductyRetrieveSerializer(producty, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_retrieve_api_view(request, **kwargs):
    review = Review.objects.get(id=kwargs['id'])

    data = ReviewRetrieveSerializer(review, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)