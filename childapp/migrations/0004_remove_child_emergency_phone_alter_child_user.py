# Generated by Django 4.2.17 on 2025-02-19 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("childapp", "0003_alter_child_options_remove_child_first_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="child",
            name="emergency_phone",
        ),
        migrations.AlterField(
            model_name="child",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
