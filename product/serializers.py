from rest_framework import serializers

from product.models import Category, Review, Producty

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id', 'name', 'product_count')

    def get_product_count(self, category):
        return category.product_count


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = 'text stars'.split()

class ProductySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    filtered_review = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()


    class Meta:
        model = Producty
        fields = ('id', 'filtered_review', 'rating', 'category_name', 'title', 'description', 'price',  'category')

    def get_rating(self, producty):
        return producty.rating


class CategoryRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ReviewRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ProductyRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producty
        fields = '__all__'

