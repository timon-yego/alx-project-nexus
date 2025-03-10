# Generated by Django 5.1.6 on 2025-03-04 21:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecoactions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='carbonimpact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carbon_impacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ecoaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reward',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to=settings.AUTH_USER_MODEL),
        ),
    ]
