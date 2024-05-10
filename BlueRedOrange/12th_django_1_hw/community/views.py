from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse, Http404
from .models import User, Post, Comment
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts=Post.objects.all()
        data = []

        for post in posts:
            data.append(
                {
                    'title': post.title,
                    'content': post.content,
                    'user': post.user.name
                }
            )

        return JsonResponse(data=data, safe=False, status=200)
    
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        user_name = request.POST['user']

        try:
            user = User.objects.get(name=user_name)
            post.user = user
        except User.DoesNotExist:
            raise Http404('user does not exist')
        post.save()

        return JsonResponse({"success":"post has been saved"}, status=201)
