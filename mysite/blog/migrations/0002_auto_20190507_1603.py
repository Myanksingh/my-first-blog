# Generated by Django 2.2.1 on 2019-05-07 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish_date',
            new_name='published_date',
        ),
    ]
