from django.db import models


# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, null=True)
    password = models.URLField(max_length=32, null=True)
    my_email = models.EmailField(max_length=64, db_column='email', null=True)

    # python manage.py makemigrations                   创建sql语句
    # python manage.py migrate                          执行sql语句
    # python manage.py sqlmigrate login 0001            查看sql语句

    def __str__(self):
        return "result:({},{},{},{})".format(self.u_id, self.username, self.password, self.my_email)
