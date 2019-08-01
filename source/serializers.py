from rest_framework import serializers

from source.models import *

class CategoriesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['title', 'description']


class VacancyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'category', 'date_starts', 'date_ends']

