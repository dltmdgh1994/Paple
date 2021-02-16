from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=20, default='group_name_d')
    group_img = models.ImageField(upload_to='group_image/', blank=True)
    group_code = models.CharField(max_length=20, default='default', primary_key=True)

    def __str__(self):
        return self.group_code


class Member(models.Model):
    user_email = models.EmailField(max_length=50, primary_key=True)
    group_code = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_code', blank=True, default='default')
    user_name = models.CharField(max_length=20)
    user_pw1 = models.CharField(max_length=20)
    user_pw2 = models.CharField(max_length=20)
    user_birth = models.DateField('date_published')
    user_status = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.user_email



