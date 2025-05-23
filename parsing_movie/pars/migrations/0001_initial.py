# Generated by Django 5.1.7 on 2025-03-30 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('anime_id', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_number', models.IntegerField()),
                ('episode_id', models.CharField(max_length=50, unique=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='pars.anime')),
            ],
        ),
        migrations.CreateModel(
            name='VideoServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=100)),
                ('video_url', models.URLField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_servers', to='pars.episode')),
            ],
        ),
    ]
