from django.urls import path
from .views import LanguageCreateView, Home, LanguageFileAddView

urlpatterns = [
    path('', Home.as_view()),
    path('add/', LanguageCreateView.as_view()),
    path('file/', LanguageFileAddView.as_view())

]