# Generated by Django 4.0.4 on 2022-05-27 20:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_bookitem_rent_alter_bookitem_reserve_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('f08eb51d-7d49-4912-9c9e-641915b6ef3d'), editable=False),
        ),
    ]
