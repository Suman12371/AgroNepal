# Generated by Django 5.1.7 on 2025-05-02 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0032_remove_message_conversation_remove_message_sender_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BusinessChat',
        ),
    ]
