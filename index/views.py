from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse, reverse
import json


# Create your views here.

def img(request):
    # return redirect(reverse("index:login1"))
    return HttpResponse("This is img function ！")


def xyz(request):
    return HttpResponse("This is xyz function ！")


def get_file(request):
    # content = request.FILES.get('aaa')
    # print(content.read().decode('utf-8'))
    # print(aaa)
    # print('request:' + str(request))
    # print('\n')
    # print('request.body:' + str(request.body))
    # print('\n')
    # print('request.meta:' + str(request.META))
    # print('\n')
    # print('ip:' + request.META.get("COMMONPROGRAMFILES(X86)"))
    print('post:' + str(request.POST.get('name')))
    return HttpResponse('True')


def set_cookie(request):
    response = render(request, 'bji.html')
    content = '这是一个cookie'
    response.set_cookie("content", json.dumps(content), 5000)  # 中文转json
    return response


def get_cookie(request):
    content = json.loads(request.COOKIES.get("content", ""))  # json转回原内容
    print(content)
    return HttpResponse("True")


# 这个是全局变量，只要不重启服务，能够一直保存从后面加来的数据。
USER_LIST = [
    {'username': 'tom', 'email': "15@qq.com"}
]


def add_user(request):
    if request.method == "POST":
        user = request.POST.get("username", None)
        pwd = request.POST.get("password", None)
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        print(user, pwd, name, email)
        if user == "Tom":
            new_user = {
                'username': user, 'email': email, 'name': name, 'password': pwd
            }
            USER_LIST.append(new_user)
            print(type(USER_LIST))
            return render(request, 'bjiuser.html', {'user_list': USER_LIST})
            # return render(request, 'bjiuser.html', context=USER_LIST[0])
            # return HttpResponse({'user_list': USER_LIST})
    else:
        print(request.method)
        return render(request, 'bjiuser.html')


def url_param(request, id):
    return HttpResponse("The param of url_param is :" + str(id))


def request_param(request):
    r = request.GET.get('username')
    return HttpResponse("The param of request_param is :" + str(r))
