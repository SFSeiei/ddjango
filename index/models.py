from django.db import models


# Create your models here.
# 车辆平台部分
# 用户
class UserInfo(models.Model):
    User_id = models.AutoField(primary_key=True)
    # 自增主键
    User_name = models.CharField(max_length=20, unique=True, null=False)
    # 索引
    User_pwd = models.CharField(max_length=32, null=False)
    User_phone = models.BigIntegerField(null=False, unique=True)
    # 大整数
    User_date = models.DateTimeField(null=False)

    # 日期时间

    class Meta:
        db_table = "users"
        # 表名


# 车辆
class Vehicle(models.Model):
    Veh_id = models.AutoField(primary_key=True)
    Veh_User = models.ForeignKey(to=UserInfo, related_name='Veh_User', on_delete=models.CASCADE)
    # 会生成名为Veh_User_id的字段，是users表主键（id）的外键
    Veh_name = models.CharField(max_length=45, null=False)
    Veh_status = models.IntegerField(default=0)
    Veh_mile = models.FloatField(default=0)

    # 浮点数

    class Meta:
        db_table = "vehicles"
        unique_together = ("Veh_User", "Veh_name")
        # 联合主键，用户车名不能重复
