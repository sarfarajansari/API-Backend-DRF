# Generated by Django 3.2.4 on 2021-06-16 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludo', '0004_coordinates_reached'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='ended',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='loser',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='game',
            name='runnerup1',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='game',
            name='runnerup1r',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='game',
            name='winnerId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.CharField(default='', max_length=40),
        ),
    ]