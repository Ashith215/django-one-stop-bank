# Generated by Django 5.1.4 on 2024-12-14 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_addamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addamount',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bankapp.bankupload'),
        ),
    ]
