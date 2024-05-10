from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import Post, User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_post(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = []

        for post in posts:
            data.append({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'user_id': post.user_id.id
            })

        return JsonResponse(data, safe=False, status=200)

@csrf_exempt
def set_post(request):    
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        id = request.POST['user_id']
        
        try:
            user = User.objects.get(id=id)
            post.user_id = user
        except User.DoesNotExist:
            return JsonResponse({'User does not exist'}, status=400)
        
        post.save()

        return JsonResponse({'success': 'Post has been saved'}, status=201)