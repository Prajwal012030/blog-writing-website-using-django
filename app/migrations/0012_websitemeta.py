# Generated by Django 5.0.7 on 2024-07-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('about', models.TextField()),
            ],
        ),
    ]
