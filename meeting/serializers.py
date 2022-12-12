from rest_framework import serializers
from meeting.models import CategoryDocuments, NestedDocuments, Tags, MeetingArticles, Category


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


class MeetingArticlesSerializer(serializers.ModelSerializer):
    nested_documents = NestedDocumentsSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MeetingArticles
        fields = '__all__'
