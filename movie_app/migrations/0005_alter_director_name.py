# Generated by Django 4.0.3 on 2022-03-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
