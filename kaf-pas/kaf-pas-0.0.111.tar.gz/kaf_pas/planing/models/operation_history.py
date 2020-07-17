import logging

from django.db.models import TextField

from isc_common.auth.models.user import User
from isc_common.fields.code_field import CodeStrictField
from isc_common.fields.date_time_field import DateTimeField
from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade
from isc_common.models.audit_history import AuditHistory, AuditHistoryManager, AuditHistoryQuerySet
from kaf_pas.planing.models.operation_types import Operation_types
from kaf_pas.planing.models.operations import Operations
from kaf_pas.planing.models.status_operation_types import Status_operation_types

logger = logging.getLogger(__name__)


class Operation_historyQuerySet(AuditHistoryQuerySet):
    pass


class Operation_historyManager(AuditHistoryManager):

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
        return Operation_historyQuerySet(self.model, using=self._db)


class Operation_history(AuditHistory):
    date = DateTimeField()
    description = TextField(null=True, blank=True)
    num = CodeStrictField()
    operation = ForeignKeyCascade(Operations)
    opertype = ForeignKeyProtect(Operation_types)
    status = ForeignKeyProtect(Status_operation_types)
    creator = ForeignKeyProtect(User,related_name='Operation_history_creator')

    objects = Operation_historyManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'История операций'
