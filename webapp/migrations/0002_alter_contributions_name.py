# Generated by Django 3.2 on 2021-04-23 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributions',
            name='name',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.member'),
        ),
    ]