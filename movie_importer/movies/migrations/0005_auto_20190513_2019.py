# Generated by Django 2.2.1 on 2019-05-13 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20190513_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='movies.Name'),
        ),
    ]
