# Generated by Django 3.1.2 on 2021-02-15 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20210215_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='user_avatar',
            field=models.CharField(choices=[('avatar1', 'avatar1'), ('avatar2', 'avatar2'), ('avatar3', 'avatar3'), ('avatar4', 'avatar4'), ('avatar5', 'avatar5'), ('avatar6', 'avatar6'), ('avatar7', 'avatar7'), ('avatar8', 'avatar8'), ('avatar9', 'avatar9')], default='avatar1', max_length=20, null=True),
        ),
    ]
