# Generated by Django 5.1.4 on 2024-12-29 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myquizz', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='brith_date',
            new_name='birth_date',
        ),
    ]