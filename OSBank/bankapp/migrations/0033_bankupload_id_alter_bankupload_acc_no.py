# Generated by Django 5.1.4 on 2024-12-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0032_addamount_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankupload',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bankupload',
            name='acc_no',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
