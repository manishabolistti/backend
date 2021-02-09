# Generated by Django 3.1.4 on 2021-01-05 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Total', models.IntegerField()),
                ('CreatedAt', models.DateField(auto_now_add=True)),
                ('UpdatedAt', models.DateField(auto_now=True)),
                ('Status', models.CharField(choices=[('new', 'new'), ('paid', 'paid')], max_length=5)),
                ('mode_of_payment', models.CharField(choices=[('cash', 'cash'), ('paytm', 'paytm'), ('card', 'card')], max_length=10)),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('ImageLink', models.ImageField(upload_to='')),
                ('Price', models.FloatField()),
                ('CreatedAt', models.DateField(auto_now_add=True)),
                ('UpdatedAt', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
                ('Price', models.FloatField()),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecore.order')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecore.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecore.product'),
        ),
    ]