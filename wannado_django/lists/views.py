from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from lists.forms import CollectionForm
from lists.models import Collection


def index(request):
    return HttpResponse("Hello, world. You're at the lists index.")



class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collection = Collection.objects.all()[0]
        if collection:
            txt_file = collection.file.open()
            txt = txt_file.read().decode("utf-8", "strict")
            form = CollectionForm({'text_area':txt})
            context['form'] = form
        return context


    def post(self, request, *args, **kwargs):
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = Collection.objects.all()[0]
            new_txt = form.data['text_area']
            txt_file = collection.file.open(mode='wb')
            print(new_txt.encode('utf-8'))
            txt_file.write(new_txt.encode('utf-8'))
            txt_file.close()
        return self.get(request, *args, **kwargs)