# Generated by Django 4.1.2 on 2022-10-12 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("image_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="hotel",
            old_name="hotel_Main_Img",
            new_name="img",
        ),
    ]
