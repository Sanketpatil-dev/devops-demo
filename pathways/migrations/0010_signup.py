# Generated by Django 2.1.15 on 2022-11-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0009_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=30)),
                ('phnum', models.CharField(max_length=13)),
                ('emailid', models.CharField(max_length=20)),
                ('pswd', models.CharField(max_length=20)),
            ],
        ),
    ]
