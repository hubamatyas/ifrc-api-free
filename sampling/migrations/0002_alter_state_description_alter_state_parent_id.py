# Generated by Django 4.1.6 on 2023-02-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='description',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='parent_id',
            field=models.IntegerField(null=True),
        ),
    ]
