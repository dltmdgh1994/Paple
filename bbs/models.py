from django.db import models
from account.models import Member, Group


# class Group(models.Model):
#     group_id = models.BigAutoField(primary_key=True)
#     group_name = models.CharField(max_length=20)
#     group_img = models.ImageField(upload_to='')
#     group_link = models.URLField()
#
#     def __str__(self):
#         return self.group_name
#
#
# class User(models.Model):
#     user_email = models.CharField(max_length=50, primary_key=True)
#     group_id = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id')
#     user_name = models.CharField(max_length=20)
#     user_pw = models.CharField(max_length=20)
#     user_birth = models.DateTimeField()
#     user_status = models.BooleanField()
#
#     def __str__(self):
#         return self.user_email


class Question(models.Model):
    q_id = models.BigAutoField(primary_key=True)
    q_content = models.CharField(max_length=200)
    q_date = models.DateTimeField()

    def __str__(self):
        return self.q_content

    def as_dict(self):
        question_date = self.q_date.strftime('%Y-%m-%d')
        return {'q_content': self.q_content, 'q_date': question_date}


class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user_email = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='user_email')
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_name')
    post_date = models.DateTimeField()
    post_name = models.CharField(max_length=30)
    post_content = models.CharField(max_length=200)

    def __str__(self):
        return self.post_name


class Comment(models.Model):
    c_id = models.BigAutoField(primary_key=True)
    user_email = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='user_email')
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_name')
    c_content = models.CharField(max_length=200)

    def __str__(self):
        return self.c_content


# DB 수정사항 반영
# python manage.py migrate <app_name> zero
# python manage.py makemigrations <app_name>
# python manage.py migrate
