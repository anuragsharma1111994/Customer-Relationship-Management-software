# Generated by Django 3.0.5 on 2021-05-23 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20210523_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='organisation',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='leads.UserProfile'),
            preserve_default=False,
        ),
    ]