from django.db import models

class UserManager(models.Manager):
    def increase(self,name,password):
        user = User1Info()
        user.uname = name
        user.upasswd = password
        user.save()
    def checkname(self,name):
        try:
            user = User1Info.userset.get(uname = name)
            return 1
        except Exception, e:
            return 0

    def login(self,name,password):
        try:
            user = User1Info.userset.get(uname = name)
            if user.upasswd == password:
                return 1
            else:
                return 2
        except Exception, e:
            return 3
    # def checkpasswd(self,passwd):
    #     try:
    #         user = User1Info.userset.get(upasswd = passwd)
    #         return 1
    #     except Exception, e:
    #         return 0

class User1Info(models.Model):
    uname = models.CharField(max_length=20)
    upasswd = models.CharField(max_length=40)
    userset = UserManager()
