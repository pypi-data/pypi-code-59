from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Audit(models.Model):
    """Audit Model
    AuditModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created_at (DateTime): Stores the datetime the object was created.
        + modified_at (DateTime): Stores the last datetime the object was modified.
        + created_by (ForeignKey): Stores the user who created the object.
        + modified_by (ForeignKey): Stores the user who modified the object.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('creation date'),
        help_text=_("date when the object was created"),
        blank=True, null=True
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('update date'),
        help_text=_("date when the object was modified"),
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='%(class)s_created_by',
        null=True, blank=True,
        verbose_name=_('creation user'),
        help_text=_("user who created the object"),
    )
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='%(class)s_modified_by',
        null=True, blank=True,
        verbose_name=_('update user'),
        help_text=_("user who performed the update"),
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if self.created_at is None and not user.is_anonymous:
            self.created_by = user
            self.modified_by = user
        elif not user.is_anonymous:
            self.modified_by = user

        super(Audit, self).save(*args, **kwargs)

class City(Audit):
    STATES = (
        ("", "---------"),
        ("Amazonas", "Amazonas"),
        ("Antioquia", "Antioquia"),
        ("Arauca", "Arauca"),
        ("Atlántico", "Atlántico"),
        ("Bolívar", "Bolívar"),
        ("Boyacá", "Boyacá"),
        ("Caldas", "Caldas"),
        ("Caquetá", "Caquetá"),
        ("Casanare", "Casanare"),
        ("Cauca", "Cauca"),
        ("Cesar", "Cesar"),
        ("Chocó", "Chocó"),
        ("Córdoba", "Córdoba"),
        ("Cundinamarca", "Cundinamarca"),
        ("Guainía", "Guainía"),
        ("Guaviare", "Guaviare"),
        ("Huila", "Huila"),
        ("La Guajira", "La Guajira"),
        ("Magdalena", "Magdalena"),
        ("Meta", "Meta"),
        ("Nariño", "Nariño"),
        ("Norte de Santander", "Norte de Santander"),
        ("Putumayo", "Putumayo"),
        ("Quindío", "Quindío"),
        ("Risaralda", "Risaralda"),
        ("San Andrés y Providencia", "San Andrés y Providencia"),
        ("Santander", "Santander"),
        ("Sucre", "Sucre"),
        ("Tolima", "Tolima"),
        ("Valle del Cauca", "Valle del Cauca"),
        ("Vaupés", "Vaupés"),
        ("Vichada", "Vichada"),
        ("Bogotá d C.", "Bogotá d C."),
    )
    name = models.CharField(_('name'), max_length=100)
    state = models.CharField(_('state'), max_length=100, choices=STATES)

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __str__(self):
        return f'{self.name} - {self.state}'