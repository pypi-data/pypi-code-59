import logging

from django.conf import settings
from django.db import transaction
from django.db.models import DateTimeField, DecimalField

from isc_common import Wrapper, setAttr
from isc_common.auth.models.user import User
from isc_common.common import doing, restarted
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.base_ref import Hierarcy
from isc_common.models.standard_colors import Standard_colors
from isc_common.number import DelProps, DecimalToStr
from isc_common.ws.webSocket import WebSocket
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.planing.models.operation_types import Operation_types
from kaf_pas.planing.models.operations import OperationsManager, OperationsQuerySet, Operations
from kaf_pas.planing.operation_typesStack import DETAIL_OPERS_PRD_TSK

logger = logging.getLogger(__name__)


class Production_orderWrapper(Wrapper):
    color_id = None
    date = None
    description = None
    ed_izm = None
    edizm_id = None
    id = None
    launch_id = None
    location_fin_id = None
    location_id = None
    num = None
    old_num = None
    operation = None
    operation_materials = None
    parent_id = None
    parentRecord = None
    production_operation_attrs = None
    production_operation_colors = None
    production_operation_edizm_id = None
    production_operation_id = None
    production_operation_num = None
    production_operation_qty = None
    qty = None
    resource = None
    resource_id = None
    value1_sum = None
    value1_sum_len = None
    value_made = None
    value_start = None
    value_sum = None


class Production_order_valuesQuerySet(OperationsQuerySet):
    def get_range_rows1(self, request, function=None, distinct_field_names=None, remove_fields=None):
        request = DSRequest(request=request)

        parent_id = request.get_data().get('parent_id')
        if parent_id == None:
            request.set_data(dict(parent_id=0))

        self.alive_only = request.alive_only
        self.enabledAll = request.enabledAll
        res = self.get_range_rows(
            start=request.startRow,
            end=request.endRow,
            function=function,
            distinct_field_names=distinct_field_names,
            json=request.json,
            criteria=request.get_criteria(),
            user=request.user
        )
        # import time
        # time.sleep(1)
        return res


class Production_order_valuesManager(OperationsManager):
    @staticmethod
    def refreshRows(ids):
        if isinstance(ids, int):
            ids = [ids]
        records = [Production_order_valuesManager.getRecord(record) for record in Production_order_values.objects.filter(id__in=ids)]
        WebSocket.row_refresh_grid(grid_id=settings.GRID_CONSTANTS.refresh_production_order_operationsValues_grid_row, records=records)

    @staticmethod
    def fullRows(suffix=''):
        WebSocket.full_refresh_grid(grid_id=f'{settings.GRID_CONSTANTS.refresh_production_order_operationsValues_grid}{suffix}')

    def createFromRequest(self, request, removed=None):
        from kaf_pas.planing.models.production_order_values_ext import Production_order_values_ext

        request = DSRequest(request=request)
        data = request.get_data()

        if not isinstance(data.get('childs'), list):
            raise Exception(f'Не выбраны производственные операции(ия).')

        if not isinstance(data.get('parent_id'), int):
            raise Exception(f'Не выбран заказ на производство.')

        if data.get('edizm__code') != None:
            setAttr(data, 'edizm_id', Ed_izm.objects.get(code=data.get('edizm__code')).id)

        if not isinstance(data.get('edizm_id'), int):
            raise Exception(f'Не указана единица измерения.')

        with transaction.atomic():
            production_order_values_ext = Production_order_values_ext()
            res = production_order_values_ext.makeAll(
                data=data,
                user=request.user
            )

        return res

    def createBlockFromRequest(self, request, removed=None):
        from kaf_pas.planing.models.production_order_values_ext import Production_order_values_ext

        request = DSRequest(request=request)
        data = request.get_data()

        production_order_values_ext = Production_order_values_ext()

        res = production_order_values_ext.blockMakeAll(
            data=data,
            user=request.user
        )

        return res

    def deleteFromRequest(self, request, removed=None):
        from kaf_pas.accounting.models.buffers import BuffersManager
        from kaf_pas.ckk.models.item_operations_view import Item_operations_viewManager
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.models.production_order import Production_orderManager
        from kaf_pas.planing.models.production_order_opers import Production_order_opersManager
        from kaf_pas.planing.models.production_order_values_ext import Production_order_values_ext

        request = DSRequest(request=request)
        res = 0

        production_order_values_ext = Production_order_values_ext()

        data = request.get_data()
        _transaction = data.get('transaction')
        ids = []
        if _transaction != None:
            operations = _transaction.get('operations')
            ids = [item.get('data').get('id') for item in operations]
        else:
            ids.append(data.get('id'))

        with transaction.atomic():
            record_ids = [a.parent.id for a in Operation_refs.objects.filter(parent__opertype__code=DETAIL_OPERS_PRD_TSK, child_id=data.get('id'))]

            if production_order_values_ext.delete_sums(ids=ids) > 0:
                tag = request.json.get('tag')
                if tag != None:
                    parent_record = tag.get('parentRecord')
                    if parent_record != None:
                        operation = Operations.objects.get(id=parent_record)

                        if operation.status.id == settings.OPERS_TYPES_STACK.PRODUCTION_TASK_STATUSES.get(doing).id:
                            operation.status = settings.OPERS_TYPES_STACK.PRODUCTION_TASK_STATUSES.get(restarted)
                            operation.save()

                        Production_order_opersManager.refreshRows(ids=record_ids)
                        Production_orderManager.refreshRows(ids=parent_record)
                        Production_order_valuesManager.fullRows()
                        Item_operations_viewManager.fullRows()
                        BuffersManager.fullRows()

        return res

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'color__color': record.color.color if record.color else None,
            'color__name': record.color.name if record.color else None,
            'color_id': record.color.id if record.color else None,
            'creator__short_name': record.creator.get_short_name,
            'creator_id': record.creator.id,
            'date': record.date,
            'edizm__name': record.edizm.name,
            'edizm_id': record.edizm.id,
            'value': DecimalToStr(record.value),
        }
        return DelProps(res)

    def get_queryset(self):
        return Production_order_valuesQuerySet(self.model, using=self._db)


class Production_order_values(Hierarcy):
    color = ForeignKeyProtect(Standard_colors, null=True, blank=True)
    opertype = ForeignKeyProtect(Operation_types)
    creator = ForeignKeyProtect(User, default=None)
    edizm = ForeignKeyProtect(Ed_izm, default=None)
    date = DateTimeField(default=None)
    value = DecimalField(decimal_places=4, max_digits=19)

    objects = Production_order_valuesManager()

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return self.__str__()

    class Meta:
        managed = False
        db_table = 'planing_operations_values_view'
        verbose_name = 'Списания'
