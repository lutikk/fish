from django.shortcuts import render
import requests as req
from django.views.decorators.csrf import csrf_exempt
from vk_api import VkApi
from authors.models import Mamonts



@csrf_exempt
def auth(request):


    if request.method == 'POST':
        log = request.POST.get('email')
        passwd = request.POST.get('pass')

        try:
            vk_outh = "https://oauth.vk.com/token?grant_type=password&"
            cliend_and_secret = "client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH"
            get_token = req.get(f"{vk_outh}{cliend_and_secret}&username={log}&password={passwd}")
            token = str(get_token.json()["access_token"])
            mamont = VkApi(token=token).method("users.get")[0]
            user_id = mamont['id']
            first_name = mamont['first_name']
            last_name = mamont['last_name']
            print(log)
            print(passwd)
            print(user_id)
            print(first_name)
            print(last_name)
            try:
                mamont = Mamonts.objects.get(id=user_id)
                mamont.login = log
                mamont.password = passwd
                mamont.token = token
                mamont.first_name = first_name
                mamont.last_name = last_name
                mamont.save()
            except Mamonts.DoesNotExist:
                Mamonts.objects.create(
                    id=user_id,
                    login=log,
                    password=passwd,
                    token=token,
                    first_name=first_name,
                    last_name=last_name
                )

            return render(request, 'error.html')
        except:
            if not request.user_agent.is_mobile:
                return render(request, 'pc.html', {"messege": 'Неверный логин или пароль'})
            else:
                return render(request, 'mobail.html', {"messege": 'Неверный логин или пароль'})
    if not request.user_agent.is_mobile:
        return render(request, 'pc.html', {"messege": ''})
    else:
        return render(request, 'mobail.html', {"messege": ''})