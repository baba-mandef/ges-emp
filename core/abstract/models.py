from django.db import models
from core.extras.tools import generate_uuid
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class GesObjectManager(models.Manager):

    def get_by_public_key(self, public_key, **kwargs):

        error = f"{self.model.__name__} does not exist"

        if public_key == "undefined":
            raise ObjectDoesNotExist(error)
        qs = self.filter(**kwargs)

        try:
            instance = qs.get(public_key=public_key)
        except (ObjectDoesNotExist, ValidationError, ValueError):
            raise ObjectDoesNotExist(error)
        return instance


class GesObject(models.Model):
    id = models.BigAutoField(
        primary_key=True, unique=True, db_index=True, blank=False)
    public_key = models.UUIDField(default=generate_uuid, unique=True, db_index=True)

    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = GesObjectManager()

    class Meta:
        abstract = True
