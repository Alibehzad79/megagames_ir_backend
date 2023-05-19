# Generated by Django 4.2.1 on 2023-05-19 17:29

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0005_article_active_alter_article_id_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog_app.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_created',
            field=models.DateTimeField(verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='article',
            name='id_post',
            field=models.CharField(blank=True, default='kICQYBe', help_text='دست نزن مَردَک', max_length=7, null=True, unique=True, verbose_name='آیدی پست'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/posts/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog_app.tag', verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog_app.article', verbose_name='مقاله'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_send',
            field=models.DateTimeField(verbose_name='تاریخ ارسال'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='متن نظر'),
        ),
        migrations.AlterField(
            model_name='downloadbox',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog_app.article', verbose_name='مقاله'),
        ),
        migrations.AlterField(
            model_name='downloadbox',
            name='title',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='downloadbox',
            name='url',
            field=models.URLField(verbose_name='لینک دانلود فایل'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog_app.article', verbose_name='مقاله'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='images/galleries/<django.db.models.fields.related.ForeignKey>/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='نام تگ'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='اسلاگ'),
        ),
    ]
