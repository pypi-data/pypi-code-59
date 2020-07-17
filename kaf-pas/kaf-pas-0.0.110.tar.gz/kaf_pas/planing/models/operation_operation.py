import logging

from bitfield import BitField
from django.db.models import PositiveIntegerField, UniqueConstraint, Q

import kaf_pas
from isc_common import delAttr1, setAttr
from isc_common.auth.models.user import User
from isc_common.fields.related import ForeignKeyCascade, ForeignKeyProtect
from isc_common.models.audit import AuditManager, AuditQuerySet, AuditModel
from kaf_pas import planing, production
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.planing.models.operations import Operations
from kaf_pas.production.models.launch_operations_item import Launch_operations_item
from kaf_pas.production.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_operationQuerySet(AuditQuerySet):
    def create(self, **kwargs):
        from kaf_pas.planing.models.operation_operation_history import Operation_operation_history

        res = super().create(**kwargs)
        operation_operation_history = delAttr1(kwargs, 'id')
        setAttr(operation_operation_history, 'operation_operation', res)
        setAttr(operation_operation_history, 'hcreator', res.creator)
        Operation_operation_history.objects.create(**operation_operation_history)
        return res

    def update(self, **kwargs):
        from kaf_pas.planing.models.operation_operation_history import Operation_operation_history

        res = super().update(**kwargs)

        operation_operation_history = delAttr1(kwargs, 'id')
        setAttr(operation_operation_history, 'operation_operation', res)
        setAttr(operation_operation_history, 'hcreator', res.creator)
        Operation_operation_history.objects.create(**operation_operation_history)
        return res


class Operation_operationManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    @staticmethod
    def props():
        return BitField(flags=(
            ('direct_created', 'Зозданный после включения в производственную спецификацию'),  # 0-1
            ('updated', 'Обновленный'),  # 0-1
        ), default=0, db_index=True)

    def get_queryset(self):
        return Operation_operationQuerySet(self.model, using=self._db)


class Operation_operation(AuditModel):
    props = Operation_operationManager.props()
    ed_izm = ForeignKeyProtect(Ed_izm, null=True, blank=True)
    num = PositiveIntegerField(db_index=True)
    operation = ForeignKeyCascade(kaf_pas.planing.models.operations.Operations, related_name='planing_operation_2')
    production_operation = ForeignKeyCascade(kaf_pas.production.models.operations.Operations, related_name='production_operation_2')
    qty = PositiveIntegerField(null=True, blank=True, db_index=True)
    version = PositiveIntegerField(null=True, blank=True, db_index=True)
    creator = ForeignKeyProtect(User)

    objects = Operation_operationManager()

    def __str__(self):
        return f'ID:{self.id}, operation: [{self.operation}], production_operation: [{self.production_operation}]'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс-таблица'
        constraints = [
            UniqueConstraint(fields=['operation', 'production_operation'], condition=Q(version=None), name='Operation_operation_unique_constraint_0'),
            UniqueConstraint(fields=['operation', 'production_operation', 'version'], name='Operation_operation_unique_constraint_1'),
        ]
