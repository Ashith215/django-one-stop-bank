# Generated by Django 5.1.4 on 2025-01-02 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0046_rename_addamount_amounttransfer_amountadded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amountadded',
            name='user',
        ),
    ]
