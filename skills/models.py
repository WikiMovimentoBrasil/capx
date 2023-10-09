from django.db import models

class Skill_Family(models.Model):
    name = models.CharField(max_length=128)
    profile_image = models.URLField(max_length=256)
    profile_header = models.URLField(max_length=256)
    description = models.CharField(max_length=512)
    wiki_link = models.URLField(max_length=256)
    date_of_creation = models.DateField()
    date_of_last_edit = models.DateField()
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=128)
    profile_image = models.URLField(max_length=256)
    profile_header = models.URLField(max_length=256)
    description = models.CharField(max_length=512)
    wiki_link = models.URLField(max_length=256)
    date_of_creation = models.DateField()
    date_of_last_edit = models.DateField()
    self_learning = models.URLField(max_length=256)
    family = models.ForeignKey(Skill_Family, null=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
