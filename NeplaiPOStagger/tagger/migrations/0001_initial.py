# Generated by Django 2.2.2 on 2019-06-29 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='please give title', max_length=100)),
                ('description', models.TextField(max_length=20000)),
            ],
        ),
    ]
