# Generated by Django 4.2.1 on 2023-05-31 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0017_article_slug_alter_article_id_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id_post',
            field=models.CharField(blank=True, default='ZacCIYA', help_text='دست نزن مَردَک', max_length=7, null=True, unique=True, verbose_name='آیدی پست'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='اسلاگ'),
        ),
    ]
