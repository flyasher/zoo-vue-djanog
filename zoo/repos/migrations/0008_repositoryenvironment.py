# Generated by Django 2.2.19 on 2021-04-30 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("repos", "0007_endpoint"),
    ]

    operations = [
        migrations.CreateModel(
            name="RepositoryEnvironment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("external_url", models.CharField(max_length=300, null=True)),
                (
                    "repository",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="repository_environments",
                        related_query_name="repository_environment",
                        to="repos.Repository",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "unique_together": {("repository", "name")},
            },
        ),
    ]