from rest_framework import serializers

from product.models import Category, Producty, Review

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductySerializer(serializers.ModelSerializer):

    class Meta:
        model = Producty
        fields = ('id', 'title', 'description', 'price', 'category')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'text', 'producty')

class CategoryRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductyRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producty
        fields = '__all__'

class ReviewRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'