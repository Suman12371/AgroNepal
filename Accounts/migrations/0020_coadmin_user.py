# Generated by Django 5.1.7 on 2025-03-24 07:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0019_delete_sitesetting_alter_coadmin_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='coadmin',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coadmin_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
