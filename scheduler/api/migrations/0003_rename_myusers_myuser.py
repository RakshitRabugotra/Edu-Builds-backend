# Generated by Django 4.1.5 on 2023-01-07 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_course_delete_courses"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MyUsers",
            new_name="MyUser",
        ),
    ]
