# Generated by Django 5.2 on 2025-04-12 07:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0003_alter_skills_skill_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="skills",
            name="icon",
            field=models.ImageField(blank=True, null=True, upload_to="skills/icons/"),
        ),
    ]
