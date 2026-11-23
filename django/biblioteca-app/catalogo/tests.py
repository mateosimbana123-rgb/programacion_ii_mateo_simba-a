from django.test import SimpleTestCase
from django.urls import reverse

from catalogo.forms import AutorForm


class CatalogoUrlTests(SimpleTestCase):
    def test_main_pages_have_named_routes(self):
        routes = {
            'home': '/',
            'login': '/login/',
            'logout': '/logout/',
            'libro_list': '/libros/',
            'categoria_list': '/categorias/',
            'autor_list': '/autores/',
        }

        for route_name, expected_path in routes.items():
            with self.subTest(route_name=route_name):
                self.assertEqual(reverse(route_name), expected_path)


class AutorFormTests(SimpleTestCase):
    def test_form_accepts_all_required_author_fields(self):
        form = AutorForm(data={
            'nombre': 'Gabriel',
            'apellido': 'Garcia Marquez',
            'fecha_nacimiento': '1927-03-06',
            'nacionalidad': 'Colombiana',
        })

        self.assertTrue(form.is_valid(), form.errors)
