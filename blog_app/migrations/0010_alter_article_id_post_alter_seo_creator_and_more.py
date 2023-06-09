# Generated by Django 4.2.1 on 2023-05-20 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0009_seo_creator_alter_article_id_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id_post',
            field=models.CharField(blank=True, default='EUpczRI', help_text='دست نزن مَردَک', max_length=7, null=True, unique=True, verbose_name='آیدی پست'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='SEO نویسنده'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='refresh',
            field=models.CharField(blank=True, default=None, help_text='e.g: 3;url=https://www.mozilla.org --> میتواند خالی بماند', max_length=100, null=True, verbose_name='Refresh'),
        ),
    ]
