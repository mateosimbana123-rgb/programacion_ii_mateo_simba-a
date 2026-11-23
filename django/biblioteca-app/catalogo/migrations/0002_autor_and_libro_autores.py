from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(blank=True, related_name='libros', to='catalogo.autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
