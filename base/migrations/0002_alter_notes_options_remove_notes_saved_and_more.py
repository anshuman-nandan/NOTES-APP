# Generated by Django 4.1.2 on 2022-10-21 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['-lastedit']},
        ),
        migrations.RemoveField(
            model_name='notes',
            name='saved',
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]