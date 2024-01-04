from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import LanguageModels, LanguageFileModels
from .serializers import LanguageSerializers, LanguageFileSerializers
from .latters import CYRILLIC_TO_LATIN, LATIN_TO_CYRILLIC


def home_page(request):
    return render(request, 'api/index.html')


class LanguageCreateView(CreateAPIView):
    queryset = LanguageModels
    serializer_class = LanguageSerializers

    def post(self, request):
        data = request.data
        if 'context' in data and 'pattern' in data:
            context = data['context']
            pattern = data['pattern']

            if pattern == 'cyrillic':
                result = ''
                for i in context.replace('Sh', 'Ш').replace('Ch', 'Ч').replace('sh', 'ш').replace('ch', 'ч'):
                    if i in CYRILLIC_TO_LATIN:
                        result += CYRILLIC_TO_LATIN[i]
                    else:
                        result += i
            elif pattern == 'latin':
                result = ''
                for i in context.replace('Ш', 'Sh').replace('Ч', 'Ch').replace('ш', 'sh').replace('ч', 'ch'):
                    if i in LATIN_TO_CYRILLIC:
                        result += LATIN_TO_CYRILLIC[i]
                    else:
                        result += i
            else:
                return Response({'error': 'Invalid pattern'})

            return Response({'result': result})
        else:
            return Response({'error': 'Invalid request'})

