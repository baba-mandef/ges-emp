# Generated by Django 5.1.5 on 2025-02-03 10:23

import core.extras.tools
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("grade", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Agent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "public_key",
                    models.UUIDField(
                        db_index=True,
                        default=core.extras.tools.generate_uuid,
                        unique=True,
                    ),
                ),
                ("deleted", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "code_mat",
                    models.CharField(
                        db_index=True,
                        default=core.extras.tools.generate_unique_code,
                        max_length=10,
                        unique=True,
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=50)),
                ("birth_date", models.DateField()),
                ("base_salary", models.IntegerField()),
                ("family_aid", models.IntegerField()),
                ("children", models.IntegerField()),
                ("is_active", models.BooleanField()),
            ],
            options={
                "verbose_name": "Agent",
                "verbose_name_plural": "Agents",
                "ordering": ["last_name"],
            },
        ),
        migrations.CreateModel(
            name="AgentGrade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "public_key",
                    models.UUIDField(
                        db_index=True,
                        default=core.extras.tools.generate_uuid,
                        unique=True,
                    ),
                ),
                ("deleted", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("start_at", models.DateField(auto_now_add=True)),
                ("end_at", models.DateField(null=True)),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="grades",
                        to="agent.agent",
                    ),
                ),
                (
                    "grade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="grade.grade"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
