# Generated by Django 3.0.4 on 2020-09-04 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_delete_samplemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='cotent',
            new_name='content',
        ),
    ]
