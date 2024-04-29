from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import User, Post, Comment
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = []

        for post in posts:
            data.append(
                {
                    'id': post.pk,
                    'title': post.title,
                    'content': post.content,
                    'user_id': post.user_id.pk
                }
            )

        return JsonResponse(data=data, safe=False, status=200)
    
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        user_id = request.POST.get('user_id')  
        user = User.objects.get(pk=user_id)  
        post.user_id = user 

        post.save()

        return JsonResponse({"success":"post has been saved"}, status=201)