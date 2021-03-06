# Generated by Django 2.2 on 2020-03-27 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorHealthSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('health_tips', models.TextField()),
                ('is_disable', models.BooleanField(default=False)),
                ('created_doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_suggestion_by_me', to=settings.AUTH_USER_MODEL)),
                ('suggestion_patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_suggestion_for_me', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'doctor_health_suggestion',
            },
        ),
    ]
