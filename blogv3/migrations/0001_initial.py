# Generated by Django 2.0.4 on 2018-04-27 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False, verbose_name='文章id')),
                ('article_title', models.CharField(max_length=100, verbose_name='标题')),
                ('article_auth', models.CharField(default='elloit', max_length=64, verbose_name='作者')),
                ('article_date', models.DateField(verbose_name='发布日期')),
                ('article_commentnum', models.IntegerField(default=0, verbose_name='评论数')),
                ('article_scannum', models.IntegerField(default=0, verbose_name='浏览量')),
                ('article_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('com_content', models.TextField(verbose_name='内容')),
                ('com_ip', models.CharField(max_length=15, verbose_name='IP')),
                ('com_date', models.DateTimeField(verbose_name='时间')),
                ('com_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogv3.Article', verbose_name='文章')),
            ],
        ),
        migrations.CreateModel(
            name='StayMessage',
            fields=[
                ('stay_id', models.AutoField(primary_key=True, serialize=False)),
                ('stay_content', models.TextField(verbose_name='留言内容')),
                ('stay_ip', models.CharField(max_length=15, verbose_name='IP')),
                ('stay_date', models.DateTimeField(verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=100, verbose_name='github登录名')),
                ('avatar_url', models.URLField()),
                ('url', models.URLField(verbose_name='主页地址')),
                ('name', models.CharField(max_length=100, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email')),
                ('blog', models.URLField(null=True, verbose_name='blog')),
            ],
        ),
        migrations.AddField(
            model_name='staymessage',
            name='stay_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogv3.User', verbose_name='留言者'),
        ),
        migrations.AddField(
            model_name='comment',
            name='com_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogv3.Type', verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='comment',
            name='com_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogv3.User', verbose_name='评论者'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogv3.Type', verbose_name='类型'),
        ),
    ]
