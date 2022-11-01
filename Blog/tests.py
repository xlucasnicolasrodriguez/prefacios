from django.test import TestCase
from Blog.models import Usuario, Posteo, Comentario

# Create your tests here.


class ViewTestCase(TestCase):
    def test_crear_posteo(self):
        Posteo.objects.create(autor="Lucas", email="lucas@l.com")
        todos_los_posteos = Posteo.objects.all()

        assert len(todos_los_posteos) == 1
        assert todos_los_posteos[0].autor == "Lucas"

    def test_crear_2_usuario(self):
        Usuario.objects.create(nombre="Lionel", apellido="Messi", dni=12345678)
        Usuario.objects.create(nombre="Juan", apellido="Roman", dni=87654321)
        todos_los_usuarios = Usuario.objects.all()

        assert len(todos_los_usuarios) == 2

    def test_crear_comentario(self):
        Comentario.objects.create(
            autor="Harry", email="harry@potter.com", cuerpo="Soy mago!"
        )
        todos_los_comentarios = Comentario.objects.all()

        assert todos_los_comentarios[0].cuerpo == "Soy mago!"
