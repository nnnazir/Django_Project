from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_blogpost_id_alter_blogpost_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.FloatField(verbose_name='Номер версии')),
                ('version_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Название версии')),
                ('version_features', models.TextField(blank=True, null=True, verbose_name='Признаки версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
