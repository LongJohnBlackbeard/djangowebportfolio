# Generated by Django 4.0.6 on 2022-08-03 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Daniel', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]