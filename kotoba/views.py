from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.shortcuts import render

from .models import Aikotoba

from django.db.models import Q

def AikotobaIndexView(request):
    return render(request, 'kotoba/index.html')

class AikotobaCreateView(generic.edit.CreateView):
    success_url = reverse_lazy("aikotoba_list")
    model = Aikotoba
    fields = ['kotoba','dengon']


class AikotobaListView(generic.ListView):
    model = Aikotoba
    paginate_by = 100



    def get_queryset(self):
        q_word = self.request.GET.get('aikotoba')
 
        if q_word:
            object_list = Aikotoba.objects.filter(
                Q(kotoba__exact=q_word)
                )
        else:
            object_list = Aikotoba.objects.filter(
                id = 'a2016c1c823541c683208276f7413d18'
                )
        return object_list





class AikotobaDetailView(generic.DetailView):
    model = Aikotoba


class AikotobaUpdateView(generic.UpdateView):
    model = Aikotoba
    fields = ['kotoba','dengon']
    success_url = reverse_lazy('aikotoba_list')
    

class AikotobaDeleteView(generic.DeleteView):
    model = Aikotoba
    success_url = reverse_lazy('aikotoba_list')

