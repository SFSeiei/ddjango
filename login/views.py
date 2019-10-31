from django.shortcuts import render
from django.db import connection
from . import models
# Create your views here.
from django.shortcuts import redirect, reverse, HttpResponse
from login.models import User


def abc(request):
    return redirect(reverse("login:login1"))


def cde(request):
    return HttpResponse("This is def function!")


def opertation(request, nid):
    ########增########
    models.User.objects.create(username='root3', password='666')
    # 对User类进行操作，增加一行username=root3&password=666的数据
    obj = models.User(username='root2', password='111')
    obj.save()  # 这两句合起来效果和上面那个一样，都是增加数据

    #######删#########
    models.User.objects.filter(username='root').delete()
    # 删除数据，不用filter()就把所有数据删了

    ########改#########
    models.User.objects.all().update(password='666')  # 对所有数据密码改成666
    models.User.objects.filter(username='root2').update(password='777')  # 修改对应数据密码

    ########查########
    result = models.User.objects.all()  # 查询到所有数据
    for row in result:
        print(row.u_id, row.username, row.password)
    found = models.User.objects.filter(username='root3', password='666')
    # 查找对应条件的数据
    print(found.count())  # 查询到的行数
    for each in found:
        print(each.u_id)
    return HttpResponse('ok')


def get_user_connection(request):
    cursor = connection.cursor()
    cursor.execute("select * from login_user")
    result = cursor.fetchall()
    return HttpResponse(result)


def add_user(request):
    user1 = User(username="Tom", password="123456", my_email="156@qq.com")
    user2 = User(username="Tommy", password="123456", my_email="156@qq.com")
    user3 = User(username="Toshiba", password="123456", my_email="156@qq.com")
    user1.save()
    user2.save()
    user3.save()
    return HttpResponse("Add user successfully!")


def get_all_user(request):
    user = User.objects.all()
    user1 = User.objects.filter(username="Tom").first()
    print(user1)
    return HttpResponse(user)


def ger_user(request):
    user1 = User.objects.filter(username__exact='Tom')
    user2 = User.objects.filter(username__iexact='To')
    user3 = User.objects.filter(username__contains='To')
    print('user1:' + str(user1) + '\n' + 'user2:' + str(user2) + '\n' + 'user3:' + str(user3))
    return HttpResponse('user1:' + str(user1) + '\n' + 'user2:' + str(user2) + '\n' + 'user3:' + str(user3))


def q_get_user(request):
    from django.db.models import Q
    user1 = User.objects.filter(Q(username="Tom"))
    user2 = User.objects.filter(~Q(username="Tom"))
    print("user1:" + str(user1) + "\n" + "user2:" + str(user2))
    return HttpResponse("user1:" + str(user1) + "\n" + "user2:" + str(user2))


def delete_user(request):
    user1 = User.objects.filter(username="Tom")
    user1.delete()
    return HttpResponse('Delete user successfully!')


def update_user(request):
    user1 = User.objects.filter(username="Tommy")
    user1.username = "Tommy1"
    user1.save()
    return HttpResponse("Update user successfully!")


def get_sql(request):
    user1 = User.objects.filter(username__exact="Toshiba").all()
    user2 = User.objects.filter(username__exact="Toshiba").first()
    print(connection.queries)
    return HttpResponse("first:" + str(user1.query) + "\n" + "second:" + str(connection.queries))


def aggregate(request):
    from django.db import models
    user = User.objects.aggregate(models.Avg('u_id'))
    print(user)
    return HttpResponse("user:" + str(user))
