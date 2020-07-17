import logging

from bitfield import BitField
from django.db.models import CheckConstraint, Q, F, UniqueConstraint

from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel
from isc_common.models.tree_audit import TreeAuditModelManager, TreeAuditModelQuerySet
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_refsQuerySet(TreeAuditModelQuerySet):
    def delete(self):
        self.check_dliting = False

        return super().delete()

    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class Operation_refsManager(TreeAuditModelManager):

    @staticmethod
    def props():
        return BitField(flags=(
            ('inner_routing', 'Связь операций внутри товарной позиции'),  # 0-1
            ('outer_routing', 'Связь операций между товарными позициями'),  # 1-2
            ('product_order_routing', 'Связи в блоке задания на производство'),  # 2-4
            ('product_making', 'Связи выпуска'),  # 3-8
            ('product_making_block', 'Блок операций выпуска, удаляется как одно целое для правильного удаления релизов'),  # 4-16
        ), default=0, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'parent': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_refsQuerySet(self.model, using=self._db)


class Operation_refs(AuditModel):
    parent = ForeignKeyProtect(Operations, related_name='operation_parent', blank=True, null=True)
    child = ForeignKeyProtect(Operations, related_name='operation_child')
    props = Operation_refsManager.props()

    objects = Operation_refsManager()

    def __str__(self):
        return f"ID:{self.id},\n " \
               f"props: [{self.props}],\n " \
               f"child: [{self.child}],\n " \
               f"parent: [{self.parent}]"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица операций планирования'
        constraints = [
            CheckConstraint(check=~Q(child=F('parent')), name='Operation_refs_not_circulate_refs'),
            UniqueConstraint(fields=['child', 'props'], condition=Q(deleted_at=None) & Q(parent=None), name='Operation_refs_unique_constraint_0'),
            UniqueConstraint(fields=['child', 'parent', 'props'], condition=Q(deleted_at=None), name='Operation_refs_unique_constraint_1'),
            UniqueConstraint(fields=['child', 'deleted_at', 'props'], condition=Q(parent=None), name='Operation_refs_unique_constraint_2'),
            UniqueConstraint(fields=['child', 'deleted_at', 'parent', 'props'], name='Operation_refs_unique_constraint_3'),

        ]
