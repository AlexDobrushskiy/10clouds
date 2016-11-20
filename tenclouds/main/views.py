from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.views.generic import FormView, DetailView
from main.models import URLStorage
from django.core.urlresolvers import reverse


class URLShortenerForm(forms.Form):
    url = forms.URLField()

    def create_shortented_url(self):
        url = self.cleaned_data['url']
        shortened_url = URLStorage.objects.get_or_create_by_url(url)
        return shortened_url


class RootView(FormView):
    template_name = 'root.htm'
    form_class = URLShortenerForm
    success_url = '/'

    def form_valid(self, form):
        shortened = form.create_shortented_url()

        return HttpResponseRedirect(reverse())


class ShortenedUrlDetailsView(DetailView):
    template_name = 'details.htm'
    model = URLStorage
    slug_field = 'shortened_postfix'
    slug_url_kwarg = 'postfix'

