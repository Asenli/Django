from django.db import models


class User(models.Model):
    #用户Id,
    # u_id = models.CharField(max_length=6)
    #用户名字
    u_name = models.CharField(max_length=32)
    #电话号码
    u_iphone = models.CharField(max_length=11)
    #密码
    u_password = models.CharField(max_length=256)
    #创建时间
    u_time = models.DateTimeField(auto_now_add=True)



    class Meta:
        db_table = 'user_info'


class UserTicketModel(models.Model):
    user = models.ForeignKey(User)  # 关联用户
    u_name = models.CharField(max_length=32)
    ticket = models.CharField(max_length=256)   # 密码
    out_time = models.DateTimeField()  # 过期时间

    class Meta:
        db_table = 'users_ticket'