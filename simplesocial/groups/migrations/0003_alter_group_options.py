# Generated by Django 4.0.2 on 2022-02-25 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_rename_memebers_group_members'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
    ]