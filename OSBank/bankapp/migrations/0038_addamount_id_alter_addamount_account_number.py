# Generated by Django 5.1.4 on 2024-12-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0037_addamount_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='addamount',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addamount',
            name='account_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
