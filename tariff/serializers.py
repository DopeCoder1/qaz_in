from rest_framework import serializers
from tariff.models import CategoryDocuments, NestedDocuments, Tags, TariffArticles, Category


class CategoryDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDocuments
        fields = '__all__'


class NestedDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NestedDocuments
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    category_documents = CategoryDocumentsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class TariffArticlesSerializer(serializers.ModelSerializer):
    nested_documents = NestedDocumentsSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = TariffArticles
        fields = '__all__'
