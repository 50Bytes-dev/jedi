# Generated by Django 3.0.3 on 2020-02-07 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jedi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_table', to='jedi.Candidate'),
        ),
    ]