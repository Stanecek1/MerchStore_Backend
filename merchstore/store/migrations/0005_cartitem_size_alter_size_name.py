# Generated by Django 4.2 on 2023-07-24 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='store.size'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('N/A', 'N/A')], max_length=10),
        ),
    ]