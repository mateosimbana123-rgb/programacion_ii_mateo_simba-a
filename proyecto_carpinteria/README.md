# Taller de Carpintería

Aplicación Django para gestionar categorías, clientes, muebles y pedidos de un taller de carpintería.

## Modelos y relaciones

- Categoría: contiene muchos muebles.
- Cliente: puede tener muchos pedidos y mantiene una relación muchos a muchos con muebles a través de Pedido.
- Mueble: pertenece a una categoría, tiene muchos pedidos y registra su creador.
- Pedido: relaciona un cliente con un mueble, usa estado como opciones y registra su creador.

Relaciones principales: Categoria 1:N Mueble, Cliente 1:N Pedido y Mueble 1:N Pedido.

## Instalación

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos
python manage.py runserver
```

## Usuarios de prueba

| Usuario | Contraseña | Grupo |
|---|---|---|
| admin_carpinteria | Admin123! | Superusuario |
| administrador | Administrador123! | administradores |
| consultor | Consultor123! | consultores |
