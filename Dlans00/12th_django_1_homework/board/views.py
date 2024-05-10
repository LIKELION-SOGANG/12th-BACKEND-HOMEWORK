from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import User, Post, Comment
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        data = []
        # image_url = ""
        # try:
        #     image_url = request.build_absolute_url(item.image.url)
        # except:
        #     image_url = ""

        for user in users:
            data.append(
                {
                    'id': user.id,
                    'name': user.name,
                    'school': user.school
                }
            )

        return JsonResponse(data=data, safe=False, status=200)
    
    # if request.method == 'POST':
    #     post = Post()
    #     post.title = request.POST['title']
    #     post.content = request.POST['content']
    #     post.user_id = request.POST['user_id']

    #     # try:
    #     #     store = User.objects.get(id=store_name)
    #     #     item.store = store
    #     # except Store.DoesNotExist:
    #     #     raise Http404('store does not exist')
    #     post.save()

    #     return JsonResponse({"success":"post has been saved"}, status=201)


@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = []
        image_url = ""
        try:
            image_url = request.build_absolute_url(item.image.url)
        except:
            image_url = ""

        for post in posts:
            data.append(
                {
                    'id': post.id,
                    'title': post.title,
                    'content': post.content,
                    'user_id': post.user_id.id
                }
            )

        return JsonResponse(data=data, safe=False, status=200)
    
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        user_id = request.POST['user_id']

        try:
            user = User.objects.get(id=user_id)
            post.user_id = user
        except User.DoesNotExist:
            raise Http404('user does not exist')
        post.save()

        return JsonResponse({"success":"post has been saved"}, status=201)


@csrf_exempt
def post(request, pk):
    if request.method == 'GET':
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404('post does not exist')
        
        data = {
            'id': post.pk,
            'title': post.title,
            'content': post.content,
            'user_id': post.user_id
        }

        return JsonResponse(data=data, safe=False, status=200)
    