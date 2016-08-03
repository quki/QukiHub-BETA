from django.shortcuts import render
from django.http import HttpRequest


def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'QukiHub-BETA'
        }
    )
