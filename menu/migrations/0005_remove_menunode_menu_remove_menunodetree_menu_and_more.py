# Generated by Django 4.1.7 on 2023-03-08 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menu_menunode_menu_menunodetree_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menunode',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='menunodetree',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
