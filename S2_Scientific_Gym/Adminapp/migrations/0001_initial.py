# Generated by Django 4.1.2 on 2023-02-11 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Location', models.CharField(max_length=500)),
                ('Message', models.TextField()),
            ],
            options={
                'db_table': 'Register',
            },
        ),
    ]
