# Generated by Django 3.1.2 on 2021-01-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='stars',
            new_name='year',
        ),
        migrations.AddField(
            model_name='movies',
            name='cast',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='trailer',
            field=models.TextField(null=True),
        ),
    ]
