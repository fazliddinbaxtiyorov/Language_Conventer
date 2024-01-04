from django.urls import path
from .views import LanguageCreateView, home_page, LanguageFileAddView

urlpatterns = [
    path('', home_page),
    path('add/', LanguageCreateView.as_view(), name='add'),
    path('file/', LanguageFileAddView.as_view(), name='file')

]