from django.db import models
import skills.models as skills
#TODO trocar ForeignKeys to ManyToManys
#TODO string em todos os models

class User_Profile(models.Model):
    name = models.CharField(max_length=128)
    profile_image = models.URLField(max_length=256)
    profile_header = models.URLField(max_length=256)
    description = models.CharField(max_length=512)
    wiki_link = models.URLField(max_length=256)
    date_of_creation = models.DateField()
    date_of_last_edit = models.DateField()
    birthday = models.DateField()
    pronouns = models.CharField(max_length=32)
    languages = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    twitter = models.CharField(max_length=50)
    discord = models.CharField(max_length=50)
    skills_known = models.ForeignKey(skills.Skill, null=True, on_delete=models.CASCADE, related_name="skills_known")
    skills_to_learn = models.ForeignKey(skills.Skill, null=True, on_delete=models.CASCADE, related_name="skills_to_learn")
    def __str__(self):
        return self.name

#TODO - GRUPOS DE USUARIOS
