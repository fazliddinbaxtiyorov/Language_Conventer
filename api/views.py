from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import LanguageModels, LanguageFileModels
from .serializers import LanguageSerializers, LanguageFileSerializers
from .latters import CYRILLIC_TO_LATIN, LATIN_TO_CYRILLIC


def home_page(request):
    return render(request, 'api/index.html')

