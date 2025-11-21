import json

from django.views import View
from django.http import HttpRequest, JsonResponse

from .models import User


class AccountView(View):

    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())
        
        try:
            User.objects.get(username=data['username'])
            return JsonResponse(data={'message': 'user exists.'}, status=400)
        
        except User.DoesNotExist:
            user = User(
                username=data['username'],
                password=data['password'],
                email=data.get('email'),
                phone=data.get('phone'),
            )
            user.save()

            return JsonResponse(data={'message': 'user created.'}, status=201)
        
    def get(self, request: HttpRequest, username: str) -> JsonResponse:
        try:
            user = User.objects.get(username=username)

            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'password': user.password,
                'email': user.email,
                'phone': user.phone,
                'profile': {
                    'id': user.profile.id,
                    'first_name': user.profile.first_name,
                    'last_name': user.profile.last_name,
                    'bio': user.profile.bio,
                    'avatar': user.profile.avatar.url,
                }
            })
        
        except User.DoesNotExist:
            return JsonResponse(data={'messsage': 'user does not exists.'}, status=400)


class ProfileView(View):

    def post(self, request: HttpRequest) -> JsonResponse:
        username = request.POST.get('username')
        avatar = request.FILES.get('avatar')

        try:
            user = User.objects.get(username=username)

            user.profile.avatar = avatar
            user.profile.save()

            return JsonResponse(data={'message': 'avatar created.'}, status=201)
        
        except User.DoesNotExist:
            return JsonResponse(data={'messsage': 'user does not exists.'}, status=400)
        

    def put(self, request: HttpRequest) -> JsonResponse:
        pass


    