# Generated by Django 5.1.4 on 2024-12-15 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0030_alter_addamount_amount_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addamount',
            name='account_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bankapp.bankupload'),
        ),
    ]
