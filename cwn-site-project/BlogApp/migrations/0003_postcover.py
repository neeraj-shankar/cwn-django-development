# Generated by Django 3.2.8 on 2021-11-17 07:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_alter_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200, verbose_name='Heading')),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('img', models.ImageField(upload_to='post_pics/', verbose_name='Cover Photo')),
            ],
        ),
    ]
