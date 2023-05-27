# Generated by Django 4.2.1 on 2023-05-27 08:16

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'تبلیغ',
                'verbose_name_plural': 'تبلیغات',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('text', models.TextField(verbose_name='متن نظر')),
                ('date_sent', models.DateTimeField(verbose_name='تاریخ ارسال')),
                ('accept', models.BooleanField(default=False, verbose_name='تایید کردن')),
            ],
            options={
                'verbose_name': 'تماس',
                'verbose_name_plural': 'تماس های کاربران',
                'ordering': ['-date_sent'],
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=50, verbose_name='عنوان سایت')),
                ('site_logo', models.ImageField(upload_to='images/logos/', verbose_name='لوگوی سایت')),
                ('site_url', models.URLField(help_text='https://meytisgame.ir', verbose_name='آدرس سایت')),
                ('site_copyright', models.CharField(max_length=50, verbose_name='قانون کپی رایت')),
                ('site_creator', models.CharField(max_length=50, verbose_name='نام صاحب سایت')),
                ('site_description', models.TextField(verbose_name='توضیحات سایت')),
                ('site_keywords', models.TextField(verbose_name='کلمات کلیدی سایت')),
            ],
            options={
                'verbose_name': 'تنظیم',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='e.g: instagram', max_length=50, verbose_name='نام شبکه اجتماعی')),
                ('url', models.URLField(help_text='e.g: https://instagram.com/username/', verbose_name='لینک')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='socials', to='settings_app.setting', verbose_name='تنظیم')),
            ],
            options={
                'verbose_name': 'شبکه اجتماعی',
                'verbose_name_plural': 'شبکه های اجتماعی',
            },
        ),
    ]
