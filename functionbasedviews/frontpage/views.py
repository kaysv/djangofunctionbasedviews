from django.shortcuts import render
from django.http import HttpResponse
from django.views import View #Base view
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from django.utils import timezone
from .import models

from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

# from articles.models import Article


# Create your views here.
class FronView(View):
    # ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    def get(self,request,*args,**kwargs):
        return HttpResponse('hello')


class DetailViewView(DetailView):
    model = models.Person
    template_name = 'frontpage/detailview.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ListViewView(ListView):
    model = models.Person
    template_name = 'frontpage/listview.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



class GenericEditingView(FormView):
    template_name = 'frontpage/GenericEditingView.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data.get("name"))
        form.send_email()
        return super().form_valid(form)

class CreateViewView(CreateView):
    model = models.Author
    template_name = "frontpage/createview.html"
    fields = ['name']

class UpdateViewView(UpdateView):
    model = models.Author
    template_name = "frontpage/updateview.html"
    fields = ['name']
    template_name_suffix = '_update_form'

class DeleteViewView(DeleteView):
    model = models.Author
    template_name = "frontpage/deleteview.html"
    success_url = reverse_lazy('FrontView')


# https://docs.djangoproject.com/en/2.0/search/?q=class+based+views
# https://docs.djangoproject.com/en/2.0/topics/class-based-views/
# https://docs.djangoproject.com/en/2.0/ref/class-based-views/
# https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/
# https://www.codingforentrepreneurs.com/blog/ajaxify-django-forms/
