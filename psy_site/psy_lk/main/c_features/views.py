from django.shortcuts import render, redirect
from django.template.loader import render_to_string
import requests
from django_htmx.http import HttpResponseClientRedirect, HttpResponseRedirectBase
from django.http import JsonResponse, HttpResponse
from django.contrib.sessions.backends.cache import SessionStore


def create_complaint(request):
    if request.method == 'POST':
        resp = HttpResponse("Неизвестная ошибка. Жалоба не создана")
        return resp
    else:
        return JsonResponse({'error': 'Неверный метод запроса'}, status=400)


def card_panel(request):
    return render(request, 'psy_lk/3_features/card_panel.html')

