from django.db import models


class Story(models.Model):
    heading = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    story_text = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.heading


