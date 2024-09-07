# Generated by Django 4.2.8 on 2024-01-17 16:52

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                ("email", models.EmailField(max_length=256, unique=True, verbose_name="Email")),
                ("first_name", models.CharField(max_length=256, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=256, verbose_name="Фамилия")),
                ("patronymic", models.CharField(max_length=256, verbose_name="Отчество")),
                ("age", models.CharField(blank=True, max_length=10, null=True, verbose_name="Возраст")),
                ("date", models.DateField(verbose_name="Дата рождения")),
                (
                    "type",
                    models.CharField(choices=[("П", "Пациент"), ("С", "Сотрудник")], max_length=1, verbose_name="Тип"),
                ),
                (
                    "gender",
                    models.CharField(choices=[("М", "Мужской"), ("Ж", "Женский")], max_length=1, verbose_name="Пол"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.CreateModel(
            name="Agreement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("start", models.TimeField(verbose_name="Начало")),
                ("end", models.TimeField(verbose_name="Конец")),
            ],
            options={
                "verbose_name": "Договор",
                "verbose_name_plural": "Договоры",
            },
        ),
        migrations.CreateModel(
            name="Cabinet",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256, verbose_name="Название")),
                ("number", models.CharField(max_length=10, verbose_name="Номер")),
            ],
            options={
                "verbose_name": "Кабинет",
                "verbose_name_plural": "Кабинеты",
            },
        ),
        migrations.CreateModel(
            name="PatientType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256, verbose_name="Название")),
                ("sale", models.CharField(max_length=10, verbose_name="Скидка")),
            ],
            options={
                "verbose_name": "Тип пациента",
                "verbose_name_plural": "Типы пациентов",
            },
        ),
        migrations.CreateModel(
            name="Position",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256, verbose_name="Название")),
                ("functions", models.TextField(verbose_name="Функции")),
                ("salary", models.DecimalField(decimal_places=0, max_digits=10, verbose_name="Зарплата")),
            ],
            options={
                "verbose_name": "Должность",
                "verbose_name_plural": "Должности",
            },
        ),
        migrations.CreateModel(
            name="ServiceType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128, unique=True, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Специализация",
                "verbose_name_plural": "Специализации",
            },
        ),
        migrations.CreateModel(
            name="Shift",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.CharField(max_length=10, verbose_name="Номер смены")),
                ("start", models.TimeField(verbose_name="Старт смены")),
                ("end", models.TimeField(verbose_name="Конец смены")),
            ],
            options={
                "verbose_name": "Смена",
                "verbose_name_plural": "Смены",
            },
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("cabinet", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.cabinet")),
                ("position", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.position")),
            ],
            options={
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
            },
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("address", models.CharField(max_length=256, verbose_name="Адрес")),
                ("oms", models.CharField(max_length=16, unique=True, verbose_name="ОМС")),
                ("snils", models.CharField(max_length=16, unique=True, verbose_name="СНИЛС")),
                ("inn", models.CharField(max_length=12, unique=True, verbose_name="ИНН")),
                ("passport", models.CharField(max_length=128, unique=True, verbose_name="Паспорт")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("patient_type", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.patienttype")),
            ],
            options={
                "verbose_name": "Пациент",
                "verbose_name_plural": "Пациенты",
            },
        ),
        migrations.CreateModel(
            name="Talon",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("result", models.TextField(verbose_name="Результат")),
                ("agreement", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.agreement")),
            ],
            options={
                "verbose_name": "Талон",
                "verbose_name_plural": "Талоны",
            },
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128, unique=True, verbose_name="Название")),
                ("price", models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name="Цена")),
                ("service_type", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.servicetype")),
                ("employee", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.employee")),
            ],
            options={
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
        migrations.CreateModel(
            name="PatientCart",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("diagnose", models.CharField(blank=True, max_length=256, null=True, verbose_name="Диагноз")),
                ("date_visit", models.DateField(verbose_name="Дата визита")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Дата")),
                (
                    "status",
                    models.CharField(
                        choices=[("0", "Черновик"), ("1", "Обслуживание"), ("2", "Архив")],
                        default="0",
                        max_length=1,
                        verbose_name="Статус",
                    ),
                ),
                ("service", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.service")),
                ("patient", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.patient")),
            ],
            options={
                "verbose_name": "Амбулаторная карта",
                "verbose_name_plural": "Амбулаторные карты",
                "ordering": ["-created"],
            },
        ),
        migrations.AddField(
            model_name="agreement",
            name="patient_cart",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.patientcart"),
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField(verbose_name="Дата графика работы")),
                ("shift", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.shift")),
                ("employee", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.employee")),
            ],
            options={
                "verbose_name": "График работы",
                "verbose_name_plural": "График работы",
            },
        ),
        migrations.CreateModel(
            name="PatientSignature",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("signature", models.CharField(max_length=128, unique=True, verbose_name="Открытый ключ")),
                ("patient", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.patient")),
            ],
            options={
                "verbose_name": "ЭЦП",
                "verbose_name_plural": "ЭЦП",
            },
        ),
        migrations.CreateModel(
            name="PatientPhone",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("phone", models.CharField(max_length=20, verbose_name="Телефон")),
                ("patient", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.patient")),
            ],
            options={
                "verbose_name": "Телефон",
                "verbose_name_plural": "Телефоны",
            },
        ),
        migrations.AddIndex(
            model_name="patientcart",
            index=models.Index(fields=["-created"], name="api_patient_created_d9af61_idx"),
        ),
    ]
