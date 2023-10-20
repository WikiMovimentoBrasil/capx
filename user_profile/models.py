from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from skills.models import Skill


class Affiliation(models.Model):
    organization_name = models.CharField(verbose_name=_("Organization name"), max_length=256, unique=True,
                                         error_messages={"unique": _("There's another organization with that name.")})
    organization_code = models.CharField(verbose_name=_("Organization code"), max_length=20, null=True, blank=True)
    organization_website = models.URLField(verbose_name=_("Organization website"), unique=True,
                                           error_messages={
                                               "unique": _("This website is already used by another organization.")})

    def __str__(self):
        if self.organization_code:
            return self.organization_name + " (" + self.organization_code + ")"
        else:
            return self.organization_name


class Region(models.Model):
    region_name = models.CharField(verbose_name=_("Region name"), max_length=128, unique=True)
    parent_region = models.ManyToManyField("self", verbose_name=_("Parent region"), symmetrical=False,
                                           related_name="region_parent", blank=True)

    def __str__(self):
        return self.region_name


class Language(models.Model):
    language_name = models.CharField(verbose_name=_("Language name"), max_length=128)
    language_code = models.CharField(verbose_name=_("Language code"), max_length=10, unique=True)

    def __str__(self):
        return self.language_name


class WikimediaProject(models.Model):
    wikimedia_project_name = models.CharField(verbose_name=_("Wikimedia project name"), max_length=128)
    wikimedia_project_code = models.CharField(verbose_name=_("Wikimedia project code"), max_length=40, unique=True)

    def __str__(self):
        return self.wikimedia_project_name


class AreaOfInterest(models.Model):
    area_name = models.CharField(verbose_name=_("Area name"), max_length=128)

    def __str__(self):
        return self.area_name


class UserProfile(models.Model):
    PRONOUN = (
        ("he-him", _("He/Him")),
        ("she-her", _("She/Her")),
        ("they-them", _("They/Them"))
    )

    CONTACT_METHOD = (
        ("email", _("Email")),
        ("wiki", _("Discussion page")),
    )

    # PERSONAL INFORMATION
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    groups = models.JSONField(verbose_name=_("Groups"), null=True, blank=True)
    username = models.CharField(verbose_name=_("Username"), max_length=150, unique=True, blank=True,
                                error_messages={"unique": _("A user with that username already exists.")})
    pronoun = models.CharField(verbose_name=_("Pronoun"), max_length=20, choices=PRONOUN, null=True, blank=True)
    profile_image = models.URLField(verbose_name=_("Profile image"), null=True, blank=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=128, null=True, blank=True)
    middle_name = models.CharField(verbose_name=_("Middle name"), max_length=128, null=True, blank=True)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=128, null=True, blank=True)
    display_name = models.CharField(verbose_name=_("Display name"), max_length=387, null=True, blank=True)
    birthday = models.DateField(verbose_name=_("Birthday"), null=True, blank=True)

    # SOCIAL MEDIA
    twitter = models.CharField(verbose_name=_("Twitter handle"), max_length=128, null=True, blank=True)
    facebook = models.CharField(verbose_name=_("Facebook handle"), max_length=128, null=True, blank=True)
    instagram = models.CharField(verbose_name=_("Instagram handle"), max_length=128, null=True, blank=True)

    # CONTACT
    email = models.EmailField(null=True, unique=True, blank=True,
                              error_messages={"unique": _("This email is already in use.")})
    contact_method = models.CharField(verbose_name=_("Preferred contact method"), max_length=10,
                                      choices=CONTACT_METHOD, null=True, blank=True)

    # LOCALIZATION
    region = models.ManyToManyField(Region, verbose_name=_("Region"), related_name="user_region", blank=True)
    language = models.ManyToManyField(Language, verbose_name=_("Language"), related_name="user_language", blank=True)
    affiliation = models.ManyToManyField(Affiliation, verbose_name=_("Affiliation"),
                                         related_name="user_affiliation", blank=True)
    wikimedia_project = models.ManyToManyField(WikimediaProject, verbose_name=_("Wikimedia project"),
                                               related_name="user_wikimedia_project", blank=True)
    area_of_interest = models.ManyToManyField(AreaOfInterest, verbose_name=_("Area of interest"),
                                              related_name="user_area_of_interest", blank=True)

    # SKILLS
    skills_known = models.ManyToManyField(Skill, verbose_name=_("Skill known"), related_name="user_skils", blank=True)
    skills_wanted = models.ManyToManyField(Skill, verbose_name=_("Skill desired"), related_name="user_desired_skils",
                                           blank=True)

    def __str__(self):
        if self.first_name:
            if self.last_name:
                if self.middle_name:
                    return self.first_name + " " + self.middle_name[0] + ". " + self.last_name
                else:
                    return self.first_name + " " + self.last_name
            else:
                return self.first_name
        else:
            return self.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
