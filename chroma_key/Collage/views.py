from django.views import generic
from .models import Collage
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# class for each url #
class IndexView(generic.ListView):
    template_name ="Collage/index.html"
    def get_queryset(self):
        return Collage.objects.all()

class DetailView(generic.DetailView):
    model = Collage
    template_name = 'Collage/detail.html'

class CollageCreate(CreateView):
    model = Collage
    fields = ['background_image','objects_iamge']

class CollageUpdate(UpdateView):
    model = Collage
    fields = ['background_image','objects_iamge']

class CollageDelete(DeleteView):
    model = Collage
    success_url = reverse_lazy('collage:index')