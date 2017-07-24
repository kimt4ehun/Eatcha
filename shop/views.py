from django.shortcuts import get_object_or_404,  render
from django.http import Http404
from .models import Photo
# Create your views here.
#def post_list(request,id):
#    photo = get_object_or_404(Photo, id=id)
#
#
#    return render(request, 'shop/post_list.html', {'photo': photo})

def all(request):

    qs = Photo.objects.all()
    return render(request, 'shop/index.html', {'img': qs})

#def post_detail(request, id):
#    #try:
#
#    #    post = Post.object.get(id=id)
#    #except Post.DoesNotExist:
#    #    raise Http404   ->아래코드 하나랑 같음
#    post = get_object_or_404(Photo, id=id)
#    return render(request, 'shop/post_detail.html',{
#        'x': post,})
