# Generated by Django 5.1.5 on 2025-02-11 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_webapp', '0003_members'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]
