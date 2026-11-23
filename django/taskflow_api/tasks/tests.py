from django.test import TestCase
from django.urls import reverse

from .models import Project, Task


class TaskFlowViewsTests(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name="Proyecto de prueba")

    def test_home_displays_projects_and_tasks(self):
        task = Task.objects.create(project=self.project, title="Preparar entrega")

        response = self.client.get(reverse("tasks:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.name)
        self.assertContains(response, task.title)

    def test_project_can_be_created(self):
        response = self.client.post(
            reverse("tasks:project-create"),
            {"name": "Proyecto nuevo", "description": "Descripción"},
        )

        self.assertRedirects(response, reverse("tasks:project-list"))
        self.assertTrue(Project.objects.filter(name="Proyecto nuevo").exists())

    def test_invalid_project_submission_shows_errors(self):
        response = self.client.post(reverse("tasks:project-create"), {})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors)
        self.assertEqual(Project.objects.count(), 1)

    def test_project_can_be_updated(self):
        response = self.client.post(
            reverse("tasks:project-update", args=[self.project.pk]),
            {"name": "Proyecto actualizado", "description": "Nueva descripción"},
        )

        self.assertRedirects(response, reverse("tasks:project-list"))
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "Proyecto actualizado")

    def test_project_delete_requires_post_and_deletes_its_tasks(self):
        task = Task.objects.create(project=self.project, title="Tarea asociada")
        delete_url = reverse("tasks:project-delete", args=[self.project.pk])

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 405)
        self.assertTrue(Project.objects.filter(pk=self.project.pk).exists())

        response = self.client.post(delete_url)

        self.assertRedirects(response, reverse("tasks:project-list"))
        self.assertFalse(Project.objects.filter(pk=self.project.pk).exists())
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_task_can_be_created_updated_and_deleted(self):
        create_response = self.client.post(
            reverse("tasks:task-create"),
            {
                "project": self.project.pk,
                "title": "Primera tarea",
                "description": "",
                "status": Task.Status.TODO,
                "due_date": "",
            },
        )
        task = Task.objects.get(title="Primera tarea")
        self.assertRedirects(create_response, reverse("tasks:home"))

        update_response = self.client.post(
            reverse("tasks:task-update", args=[task.pk]),
            {
                "project": self.project.pk,
                "title": "Tarea actualizada",
                "description": "",
                "status": Task.Status.IN_PROGRESS,
                "due_date": "",
            },
        )
        self.assertRedirects(update_response, reverse("tasks:home"))
        task.refresh_from_db()
        self.assertEqual(task.title, "Tarea actualizada")
        self.assertEqual(task.status, Task.Status.IN_PROGRESS)

        delete_response = self.client.post(
            reverse("tasks:task-delete", args=[task.pk])
        )
        self.assertRedirects(delete_response, reverse("tasks:home"))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_task_delete_requires_post(self):
        task = Task.objects.create(project=self.project, title="No borrar por GET")

        response = self.client.get(
            reverse("tasks:task-delete", args=[task.pk])
        )

        self.assertEqual(response.status_code, 405)
        self.assertTrue(Task.objects.filter(pk=task.pk).exists())

    def test_invalid_task_submission_shows_errors(self):
        response = self.client.post(reverse("tasks:task-create"), {})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors)
        self.assertFalse(Task.objects.exists())

    def test_first_template_receives_its_context(self):
        response = self.client.get(reverse("tasks:my-first-template"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Organiza tus proyectos y tareas")
