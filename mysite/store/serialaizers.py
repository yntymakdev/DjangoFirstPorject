from rest_framework import serializers
from .models import Category, Product, Comment, ProductPhotos


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Вложенный сериализатор для категории

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'description', 'category', 'created_date', 'have', 'video']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше нуля.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'text', 'product', 'created_date']


class ProductPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = ['id', 'product', 'image']
