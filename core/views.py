from django.shortcuts import render


def get_url():
    base_url = "https://developers.tagplus.com.br/authorize?response_type=code"
    return base_url + "&client_id=d5d295a844634ad0b423f5e2fb5151ae&scope=read:pedidos"


def home(r):
    return render(r, 'core/index.html', {"url": get_url()})
