# Generated by Django 5.1.1 on 2024-09-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_tbl_news_news_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_news',
            name='posted_date',
            field=models.DateField(null=True),
        ),
    ]
