# Generated by Django 2.2.6 on 2019-11-09 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemStatement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('statement', models.TextField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.ProblemCategory')),
            ],
        ),
        migrations.CreateModel(
            name='HackathonTeam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=128)),
                ('college_name', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('team_members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
