# Generated by Django 3.2.7 on 2023-10-08 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_addtocart_category_contact_item_order_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='addtocart',
        ),
    ]