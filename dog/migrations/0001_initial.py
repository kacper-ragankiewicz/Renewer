# Generated by Django 4.0.2 on 2022-02-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=120)),
                ('opis', models.TextField()),
                ('gotowe', models.BooleanField(default=False)),
            ],
        ),
    ]
