from django.contrib.sites import requests
from django.shortcuts import render


def get_url():
    base_url = "https://developers.tagplus.com.br/authorize?response_type=code"
    return base_url + "&client_id=d5d295a844634ad0b423f5e2fb5151ae&scope=read:pedidos+read:produtos+read:clientes"


def home(r):
    return render(r, 'core/index.html',
                  {"url": get_url(),
                   "url_2": "https://api.tagplus.com.br/oauth2/token",
                   "url_produtos": "https://api.tagplus.com.br/produtos?access_token"})
