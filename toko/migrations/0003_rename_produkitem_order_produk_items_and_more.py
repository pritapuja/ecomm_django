# Generated by Django 4.2.1 on 2023-05-28 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("toko", "0002_alter_produkitem_label"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="produkItem",
            new_name="produk_items",
        ),
        migrations.RenameField(
            model_name="orderprodukitem",
            old_name="produkItem",
            new_name="produk_item",
        ),
        migrations.AlterField(
            model_name="produkitem",
            name="label",
            field=models.CharField(
                choices=[("NEW", "primary"), ("SALE", "info"), ("BEST", "danger")],
                max_length=4,
            ),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_option",
                    models.CharField(
                        choices=[("P", "Paypal"), ("S", "Stripe")], max_length=1
                    ),
                ),
                ("charge_id", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Payment",
            },
        ),
        migrations.CreateModel(
            name="AlamatPengiriman",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("alamat_1", models.CharField(max_length=100)),
                ("alamat_2", models.CharField(max_length=100)),
                ("negara", models.CharField(max_length=100)),
                ("kode_pos", models.CharField(max_length=20)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "AlamatPengiriman",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="alamat_pengiriman",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="toko.alamatpengiriman",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="payment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="toko.payment",
            ),
        ),
    ]
