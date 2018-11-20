# Generated by Django 2.0.1 on 2018-03-05 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("services", "0004_auto_20171108_1032")]

    operations = [
        migrations.CreateModel(
            name="Objective",
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
                (
                    "indicator_source",
                    models.CharField(
                        choices=[("datadog", "datadog"), ("pingdom", "pingdom")],
                        max_length=100,
                    ),
                ),
                ("indicator_query", models.CharField(max_length=10000)),
                ("target", models.DecimalField(decimal_places=4, max_digits=12)),
                (
                    "target_type",
                    models.CharField(
                        blank=True,
                        choices=[("above", "above"), ("below", "below")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="services.Service",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ObjectiveSnapshot",
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
                ("timestamp", models.DateTimeField()),
                (
                    "indicator_value",
                    models.DecimalField(decimal_places=4, max_digits=12),
                ),
                (
                    "objective",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="objectives.Objective",
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="objectivesnapshot", unique_together={("objective", "timestamp")}
        ),
        migrations.AlterUniqueTogether(
            name="objective",
            unique_together={("service", "indicator_source", "indicator_query")},
        ),
    ]
