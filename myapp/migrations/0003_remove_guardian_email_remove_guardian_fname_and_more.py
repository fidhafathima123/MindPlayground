# Generated by Django 4.2.17 on 2025-02-09 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_guardian_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="guardian",
            name="email",
        ),
        migrations.RemoveField(
            model_name="guardian",
            name="fname",
        ),
        migrations.RemoveField(
            model_name="guardian",
            name="lname",
        ),
    ]
