# Generated by Django 3.1.4 on 2020-12-29 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0002_auto_20201229_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='assists',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo_app.team'),
        ),
    ]
