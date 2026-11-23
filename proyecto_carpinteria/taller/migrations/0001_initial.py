# Generated for the taller application.

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={'ordering': ['nombre']},
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('direccion', models.CharField(blank=True, max_length=200)),
            ],
            options={'ordering': ['apellido', 'nombre']},
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='muebles', to='taller.categoria')),
            ],
            options={'ordering': ['nombre']},
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20)),
                ('fecha_pedido', models.DateField(auto_now_add=True)),
                ('observaciones', models.TextField(blank=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pedidos', to='taller.cliente')),
                ('mueble', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pedidos', to='taller.mueble')),
            ],
            options={'ordering': ['-fecha_pedido']},
        ),
    ]
