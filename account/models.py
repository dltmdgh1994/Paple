from django.db import models
from .validators import validate_pw

class Group(models.Model):
    # group_id = models.BigAutoField(primary_key=True)
    group_name = models.CharField(max_length=20, default='group_name_d', primary_key=True)
    group_img = models.ImageField(upload_to='', blank=True)
    group_link = models.URLField(blank=True)

    def __str__(self):
        return self.group_name


class Member(models.Model):
    user_email = models.EmailField(max_length=50, primary_key=True)
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_name', blank=True, default='group_name_d')
    user_name = models.CharField(max_length=20)
    user_pw1 = models.CharField(max_length=20, validators=[validate_pw])
    user_pw2 = models.CharField(max_length=20)
    user_birth = models.DateField('date_published')
    user_status = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.user_email



