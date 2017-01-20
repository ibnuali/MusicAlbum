from django.views import generic
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album


class indexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class detailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class albumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class albumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class albumDelete(DeleteView):
    model = Album
    succes_url = reverse_lazy('music:index')

class hello(generic.DetailView):
    template_name = 'music/hello.html'










"""
def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = { 'all_albums' : all_albums}
    return HttpResponse(template.render(context,request))
"""

"""
def detail(request,album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    context = { 'album' : album}
    return render(request,'music/detail.html',context)
"""


# version non bootstrap
"""
from django.shortcuts import render , get_object_or_404
from .models import Album
#from django.http import Http404

    def index(request):
    all_albums = Album.objects.all()
    #context = { 'all_albums' : all_albums}
    #return render(request,'music/index.html',context)
    return render(request,'music/index.html',{'all_albums' : all_albums})

def detail(request,album_id):
    #    album = Album.objects.get(pk=album_id)
    # get_object_or_404(Model,id)
    album = get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{'album' : album})

def favorite(request, album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album' : album,
            'error_message' : "You did not select a valid song"
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'music/detail.html',{'album' : album})
"""