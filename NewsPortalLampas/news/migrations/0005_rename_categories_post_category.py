# Generated by Django 4.2 on 2023-04-23 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_alter_category_subscribers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="categories",
            new_name="category",
        ),
    ]
