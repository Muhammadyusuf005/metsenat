# Generated by Django 5.1.5 on 2025-02-02 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeals', '0005_alter_appeal_amount_alter_appeal_available_balance_and_more'),
        ('sponsors', '0003_alter_studentsponsor_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsponsor',
            name='appeal',
            field=models.ForeignKey(limit_choices_to={'status': 'approved'}, on_delete=django.db.models.deletion.PROTECT, related_name='sponsored_students', to='appeals.appeal'),
        ),
        migrations.AlterField(
            model_name='studentsponsor',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student_sponsors', to=settings.AUTH_USER_MODEL),
        ),
    ]
