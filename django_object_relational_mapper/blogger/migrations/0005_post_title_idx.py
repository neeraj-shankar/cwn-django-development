# Generated by Django 4.2.3 on 2023-10-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0004_alter_category_name_alter_post_title'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['title'], name='title_idx'),
        ),
    ]
