# Generated by Django 2.2.2 on 2019-06-29 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paragraph',
            old_name='description',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='paragraph',
            name='title',
        ),
    ]