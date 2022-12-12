from rest_framework import serializers
from onpf.models import CategoryDocuments, NestedDocuments, Tags, OnpfArticles, Category, Executor, FormRealization, \
    SubCategory, SubCategory2


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


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'


class FormRealizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormRealization
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    category_documents = CategoryDocumentsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    subcategory1 = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = '__all__'


class SubCategorySerializer2(serializers.ModelSerializer):
    subcategory2 = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory2
        fields = '__all__'


class OnpfArticlesSerializer(serializers.ModelSerializer):
    nested_documents = NestedDocumentsSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    executor = ExecutorSerializer(read_only=True)
    form_realization = FormRealizationSerializer(read_only=True)
    subcategory3 = SubCategorySerializer2(read_only=True)

    class Meta:
        model = OnpfArticles
        fields = '__all__'
