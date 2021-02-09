# Generated by Django 2.2.5 on 2021-02-09 01:04

import account.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_name', models.CharField(default='group_name_d', max_length=20, primary_key=True, serialize=False)),
                ('group_img', models.ImageField(blank=True, upload_to='')),
                ('group_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_pw1', models.CharField(max_length=20, validators=[account.validators.validate_pw])),
                ('user_pw2', models.CharField(max_length=20)),
                ('user_birth', models.DateField(verbose_name='date_published')),
                ('user_status', models.BooleanField(blank=True, default=False)),
                ('group_name', models.ForeignKey(blank=True, db_column='group_name', default='group_name_d', on_delete=django.db.models.deletion.CASCADE, to='account.Group')),
            ],
        ),
    ]
