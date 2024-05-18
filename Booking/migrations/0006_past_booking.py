# Generated by Django 5.0.4 on 2024-05-18 02:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0005_alter_book_phone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Past_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[('9:30-10:30', '9:30-10:30'), ('10:30-11:30', '10:30-11:30'), ('11:30-12:30', '11:30-12:30'), ('12:30-1:30', '12:30-1:30'), ('1:30-2:30', '1:30-2:30'), ('2:30-3:30', '2:30-3:30'), ('3:30-4:30', '3:30-4:30'), ('4:30-5:30', '4:30-5:30'), ('5:30-6:30', '5:30-6:30'), ('6:30-7:30', '6:30-7:30')])),
                ('date', models.DateField()),
                ('Phone', models.BigIntegerField(blank=True, null=True)),
                ('Name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]