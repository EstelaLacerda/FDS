# Generated by Django 4.2 on 2023-04-16 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='descricao',
            new_name='description',
        ),
    ]
