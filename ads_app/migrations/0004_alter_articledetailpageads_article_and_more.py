# Generated by Django 4.2 on 2023-06-03 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0023_alter_article_author_alter_article_category_and_more'),
        ('ads_app', '0003_homepageads_searchpageads_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articledetailpageads',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='blog_app.article', verbose_name='مقاله'),
        ),
        migrations.AlterField(
            model_name='categorypageads',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='blog_app.category', verbose_name='تگ'),
        ),
        migrations.AlterField(
            model_name='tagpageads',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='blog_app.tag', verbose_name='تگ'),
        ),
    ]
