# Generated by Django 2.1.7 on 2019-07-07 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0007_auto_20190707_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='ownere',
            new_name='owner',
        ),
    ]
