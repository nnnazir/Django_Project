from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_product_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='id',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
