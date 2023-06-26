# Generated by Django 4.2.2 on 2023-06-26 10:46

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст новости')),
                ('dc', models.DateTimeField(auto_now_add=True, verbose_name='Дата новости')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.users',
                                             verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Текст комментария')),
                ('dc', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users', verbose_name='Автор')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.news',
                                           verbose_name='Новость')),
            ],
        ),
    ]