# Generated by Django 3.0.8 on 2020-08-21 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0006_auto_20200821_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='imgprincipal',
            field=models.ImageField(default='gallery/static/images/no-img.jpg', upload_to='galeria', verbose_name='Principal'),
        ),
        migrations.CreateModel(
            name='ImagenesPrincipales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.ImageField(default='gallery/static/images/no-img.jpg', upload_to='inicio', verbose_name='Principal')),
                ('servicio', models.CharField(max_length=64)),
                ('descripcion', models.TextField()),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inicioServicio', to='servicios.Servicios')),
            ],
        ),
    ]