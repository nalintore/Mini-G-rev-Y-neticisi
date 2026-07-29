from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 255)
    descripton = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Task(models.Mpdel):
    class StatusChoices(models.TextChoices):
        TODO = 'TODO', 'todo'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        DONE = 'DONE', 'Done'

        title = models.CharField(max_length=255)
        description = models.TextField(blank = True, null = True)
        status = models.CharField(
            max_length=20,
            choices = StatusChoices.choices,
            default = StatusChoices.TODO

        )

        project = models.ForeignKey(
            Project,
            on_delete = models.CASCADE,
            related_name = 'tasks'
        )

        def __str__(self):
            return f"{self.title} ({self.project.name})"
