# Generated by Django 3.0.5 on 2020-04-13 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
        ('administrators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bc_negotiation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_negotiation', models.DateField(default='', null=True)),
                ('amount', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brokerage_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gross_total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_net_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('average_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('bc_admin_type_investiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administrators.bc_admin_type_investiment')),
                ('bc_admin_type_negotiation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administrators.bc_admin_type_negotiation')),
                ('bc_company_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.bc_company_code')),
                ('bc_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'negotiation',
                'verbose_name_plural': 'negotiations',
            },
        ),
    ]
