from django.contrib.auth.models import Group, Permission, User
from django.core.management.base import BaseCommand

from taller.models import Categoria, Cliente, Mueble, Pedido


class Command(BaseCommand):
    def handle(self, *args, **options):
        administradores, _ = Group.objects.get_or_create(name='administradores')
        consultores, _ = Group.objects.get_or_create(name='consultores')
        models = [Categoria, Cliente, Mueble, Pedido]
        for model in models:
            permissions = Permission.objects.filter(
                content_type__app_label='taller',
                codename__in=[
                    f'add_{model._meta.model_name}',
                    f'change_{model._meta.model_name}',
                    f'delete_{model._meta.model_name}',
                    f'view_{model._meta.model_name}',
                ],
            )
            administradores.permissions.add(*permissions)
        consultores.permissions.set(Permission.objects.filter(
            content_type__app_label='taller',
            codename__in=[
                'view_categoria', 'view_cliente', 'view_mueble', 'view_pedido',
                'add_mueble', 'change_mueble', 'delete_mueble',
                'add_pedido', 'change_pedido', 'delete_pedido',
            ],
        ))

        admin_user, _ = User.objects.get_or_create(username='admin_carpinteria')
        admin_user.email = 'admin@carpinteria.local'
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.set_password('Admin123!')
        admin_user.save()

        administrador, _ = User.objects.get_or_create(username='administrador')
        administrador.email = 'administrador@carpinteria.local'
        administrador.set_password('Administrador123!')
        administrador.save()
        administrador.groups.set([administradores])

        consultor, _ = User.objects.get_or_create(username='consultor')
        consultor.email = 'consultor@carpinteria.local'
        consultor.set_password('Consultor123!')
        consultor.save()
        consultor.groups.set([consultores])

        categorias = [
            ('Sillas', 'Asientos fabricados en madera'),
            ('Mesas', 'Mesas para interiores y exteriores'),
            ('Estanterías', 'Almacenamiento modular'),
            ('Armarios', 'Muebles cerrados de madera'),
            ('Camas', 'Bases y cabeceros'),
        ]
        categoria_objetos = []
        for nombre, descripcion in categorias:
            objeto, _ = Categoria.objects.get_or_create(
                nombre=nombre,
                defaults={'descripcion': descripcion},
            )
            categoria_objetos.append(objeto)

        clientes = [
            ('Ana', 'Torres', '0991111111', 'ana@example.com', 'Centro'),
            ('Luis', 'Mora', '0992222222', 'luis@example.com', 'Norte'),
            ('Sofía', 'Paz', '0993333333', 'sofia@example.com', 'Sur'),
            ('Carlos', 'Vega', '0994444444', 'carlos@example.com', 'Este'),
            ('Elena', 'Ríos', '0995555555', 'elena@example.com', 'Oeste'),
        ]
        cliente_objetos = []
        for nombre, apellido, telefono, email, direccion in clientes:
            objeto, _ = Cliente.objects.get_or_create(
                nombre=nombre,
                apellido=apellido,
                defaults={'telefono': telefono, 'email': email, 'direccion': direccion},
            )
            cliente_objetos.append(objeto)

        muebles = [
            ('Silla colonial', 'Silla de madera maciza', 75, 10),
            ('Mesa comedor', 'Mesa para seis personas', 320, 5),
            ('Estantería Roble', 'Estantería de tres niveles', 180, 8),
            ('Armario clásico', 'Armario de dos puertas', 450, 3),
            ('Cama matrimonial', 'Cama con cabecero tallado', 390, 4),
        ]
        mueble_objetos = []
        for index, (nombre, descripcion, precio, stock) in enumerate(muebles):
            objeto, _ = Mueble.objects.get_or_create(
                nombre=nombre,
                defaults={
                    'descripcion': descripcion,
                    'precio': precio,
                    'stock': stock,
                    'categoria': categoria_objetos[index],
                    'creado_por': administrador,
                },
            )
            mueble_objetos.append(objeto)

        estados = ['pendiente', 'en_proceso', 'entregado', 'cancelado', 'pendiente']
        for index in range(5):
            Pedido.objects.get_or_create(
                cliente=cliente_objetos[index],
                mueble=mueble_objetos[index],
                defaults={
                    'cantidad': index + 1,
                    'estado': estados[index],
                    'observaciones': 'Pedido de prueba',
                    'creado_por': consultor,
                },
            )

        self.stdout.write(self.style.SUCCESS('Datos, grupos y usuarios cargados'))
