from django.shortcuts import render
from .models import User, Post, Comment
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        data = []

        for user in users:
            data.append(
                {
                    'id' : user.pk,
                    'name' : user.name,
                    'school' : user.school,
                }
            )
        return JsonResponse(data=data, safe=False, status=200) # 200 - OK

@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        data = []

        for post in posts:
            data.append(
                {
                    'id' : post.pk,
                    'title' : post.title,
                    'content' : post.content,
                    'user_id' : post.user_id.pk,
                }
            )
        return JsonResponse(data=data, safe=False, status=200) # 200 - OK

@csrf_exempt
def create_post(request, user_id):
    if request.method == "POST":
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        
        # user_id = request.POST['user_id']
        try:
            user = User.objects.get(pk=user_id)
            post.user_id = user
        except User.DoesNotExist:
            raise Http404("User does not exist")
        
        post.save()

        return JsonResponse({"success" : "Post has been saved"}, status=201) # 201 - Created