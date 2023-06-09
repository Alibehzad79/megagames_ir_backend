# Generated by Django 4.2.1 on 2023-05-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_alter_article_id_post_seo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id_post',
            field=models.CharField(blank=True, default='o7pIByq', help_text='دست نزن مَردَک', max_length=7, null=True, unique=True, verbose_name='آیدی پست'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت'),
        ),
    ]
