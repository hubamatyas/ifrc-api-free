# Generated by Django 4.1.6 on 2023-02-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampling', '0007_alter_option_child_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='term',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
