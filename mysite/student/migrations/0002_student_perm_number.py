# Generated by Django 3.0.3 on 2020-02-24 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='perm_number',
            field=models.CharField(default=1234566, help_text='Enter your perm number', max_length=200),
            preserve_default=False,
        ),
    ]
