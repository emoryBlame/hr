from django.shortcuts import render
from django.views.generic import ListView 

from rest_framework.views import APIView
from rest_framework.response import Response

from source.models import Category, Vacancy
from source.serializers import CategoriesListSerializer, VacancyListSerializer
# Create your views here.


class CategoriesListView(ListView, APIView):

    def get(self, request, format=None):
        categories = Category.objects.filter(active=True)
        serializer = CategoriesListSerializer(categories, many=True)
        return Response(serializer.data)


class VacanciesListView(ListView, APIView):

    def get(self, request, format=None):
        vacancies = Vacancy.objects.filter(active=True)
        serializer = VacancyListSerializer(vacancies, many=True)
        return Response(serializer.data)