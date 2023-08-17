# Generated by Django 4.2.1 on 2023-06-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("toko", "0003_rename_produkitem_order_produk_items_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produkitem",
            name="kategori",
            field=models.CharField(
                choices=[("T", "Tops"), ("B", "Bottoms"), ("D", "Dresses")],
                max_length=2,
            ),
        ),
    ]