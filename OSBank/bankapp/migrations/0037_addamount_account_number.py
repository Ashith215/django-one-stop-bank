# Generated by Django 5.1.4 on 2024-12-17 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0036_remove_addamount_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='addamount',
            name='account_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bankapp.bankupload'),
        ),
    ]
