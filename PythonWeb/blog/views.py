from django.shortcuts import render


from .models import Post1
def list(request):
    Data = {'Posts': Post1.objects.all().order_by('-date')}

    return render(request,'blog/blog.html',Data)


def post(request,id):
    post = Post1.objects.get(id=id)
    
    return render(request,'blog/post.html',{'post':post})
    

# Create your views here.
