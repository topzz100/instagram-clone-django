# Generated by Django 4.2.6 on 2023-12-01 23:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0011_alter_profile_bio_alter_profile_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('postImg', models.ImageField(default='demo-image-default', upload_to='profile_images')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
