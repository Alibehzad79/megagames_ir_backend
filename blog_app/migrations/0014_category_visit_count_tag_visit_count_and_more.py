# Generated by Django 4.2.1 on 2023-05-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_alter_article_options_article_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='visit_count',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
        migrations.AddField(
            model_name='tag',
            name='visit_count',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
        migrations.AlterField(
            model_name='article',
            name='id_post',
            field=models.CharField(blank=True, default='aA0tUT2', help_text='دست نزن مَردَک', max_length=7, null=True, unique=True, verbose_name='آیدی پست'),
        ),
    ]