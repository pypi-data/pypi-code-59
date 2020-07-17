from django.utils.translation import ugettext_lazy as _

import logging

from isc_common.auth.models.user import User
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet

logger = logging.getLogger(__name__)


class AuditHistoryQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def soft_delete(self):
        return super().soft_delete()

    def soft_restore(self):
        return super().soft_restore()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class AuditHistoryManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'description': record.description,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return AuditHistoryQuerySet(self.model, using=self._db)


class AuditHistory(AuditModel):
    hcreator = ForeignKeyProtect(User)

    objects = AuditHistoryManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'История изменений'
        abstract = True
