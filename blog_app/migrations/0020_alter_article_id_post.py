# Generated by Django 4.2.1 on 2023-06-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0019_alter_comment_options_remove_seo_redirect_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id_post',
            field=models.CharField(blank=True, default='G318LWT', help_text='دست نزن مَردَک', max_length=7, null=True, unique=True, verbose_name='آیدی پست'),
        ),
    ]
