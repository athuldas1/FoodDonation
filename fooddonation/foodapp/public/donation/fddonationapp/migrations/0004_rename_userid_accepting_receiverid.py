# Generated by Django 4.2.3 on 2023-10-14 03:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fddonationapp", "0003_rename_bookingdate_accepting_acceptingdate_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="accepting",
            old_name="userid",
            new_name="receiverid",
        ),
    ]