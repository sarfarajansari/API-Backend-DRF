# Generated by Django 3.2.4 on 2021-06-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210530_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.CharField(default=models.ImageField(blank=True, null=True, upload_to=''), max_length=400),
        ),
    ]
