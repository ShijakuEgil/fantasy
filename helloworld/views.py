# helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from yahoo_oauth import OAuth2


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        oauth = OAuth2(None, None, from_file='files/oauth2.json')
        print(oauth)

        return render(request, 'index.html', context=None)


class GetLeague(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'start.html', context=None)
