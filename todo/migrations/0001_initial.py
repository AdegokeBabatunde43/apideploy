# Generated by Django 4.1 on 2022-08-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('imageUrl', models.URLField()),
                ('status', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
