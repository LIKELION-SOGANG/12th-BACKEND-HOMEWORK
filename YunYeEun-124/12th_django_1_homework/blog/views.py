#from django.shortcuts import render
from django.http import JsonResponse,Http404
from .models import User,Comment,Post
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = []
        for post in posts:
            data.append(
                {
                    'title':post.title,
                    'content':post.content,
                    'user_id':post.user_id.name
                    #질문하기 user_id 가 fk일때 받아오는 방법
                    #우선 title로 대체 추후 수정 
                    
                }
            )
        return JsonResponse(data=data,safe=False,status=200)

    if request.method == 'POST':
        post = Post()
        post.content = request.POST['content']
        post.title = request.POST['title']
        user_id = request.POST['user']
        
        try:
            user = User.objects.get(name=user_id)
            post.user_id = user
        except User.DoesNotExist:
            raise Http404("user doesn't exist")
        post.save()
    return JsonResponse({"success":"post upload"},status=201)