# Generated by Django 5.1.4 on 2024-12-17 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0035_addamount_id_alter_addamount_account_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addamount',
            name='account_number',
        ),
    ]
