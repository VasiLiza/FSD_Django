from django.shortcuts import render, redirect
from django.template.loader import render_to_string
import requests
from django_htmx.http import HttpResponseClientRedirect, HttpResponseRedirectBase
from django.http import JsonResponse, HttpResponse
from django.contrib.sessions.backends.cache import SessionStore

