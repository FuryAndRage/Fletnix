# Generated by Django 3.1.2 on 2021-02-14 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_remove_userprofile_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_age', models.CharField(choices=[('1', 'Adult'), ('2', 'Child')], default='1', max_length=1)),
                ('user_gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], default='1', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='accounts.userprofile')),
            ],
        ),
    ]