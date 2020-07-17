import logging

from bitfield import BitField
from django.db import transaction
from django.db.models import PositiveIntegerField
from django.forms import model_to_dict

from isc_common import delAttr, setAttr
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsQuerySet, CommonManagetWithLookUpFieldsManager
from isc_common.models.base_ref import Hierarcy
from isc_common.number import DelProps
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.ckk.models.item import Item
from kaf_pas.production.models.launch_item_view import Launch_item_viewManager
from kaf_pas.production.models.launches import Launches
from kaf_pas.production.models.operations import Operations
from kaf_pas.production.models.operations_item import Operations_item

logger = logging.getLogger(__name__)


class Launch_operations_itemQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def create(self, **kwargs):
        if kwargs.get('props') == None:
            setAttr(kwargs, 'props', Launch_operations_item.props.created)
        return super().create(**kwargs)

    def update(self, **kwargs):
        if kwargs.get('props') == None:
            setAttr(kwargs, 'props', Launch_operations_item.props.updated)
        return super().update(**kwargs)

    def get_range_rows1(self, request, function=None, distinct_field_names=None, remove_fields=None):
        request = DSRequest(request=request)
        data = request.json.get('data')

        launch_id = data.get('launch_id')
        if launch_id != None:
            parent = Launches.objects.get(id=launch_id).parent
            if parent == None:
                launch_id = [launch.id for launch in Launches.objects.filter(parent_id=launch_id)]
                setAttr(data, 'launch_id', launch_id)
                request.set_data(data=data)

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
        return res


class Launch_operations_itemManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def props():
        return BitField(flags=(
            ('created', 'Операция добавлена'),  # 1
            ('updated', 'Операция изменена'),  # 2
        ), default=0, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'launch_id': record.launch.id,
            'launch__code': record.launch.code,
            'launch__date': record.launch.date,
            'operation_id': record.operation.id,
            'operationitem_id': record.operationitem.id if record.operationitem else None,
            'operation__code': record.operation.code,
            'operation__name': record.operation.name,
            'operation__full_name': record.operation.full_name,
            'operation__description': record.operation.description,
            'ed_izm_id': record.ed_izm.id if record.ed_izm else None,
            'ed_izm__code': record.ed_izm.code if record.ed_izm else None,
            'ed_izm__name': record.ed_izm.name if record.ed_izm else None,
            'ed_izm__description': record.ed_izm.description if record.ed_izm else None,
            'qty': record.qty,
            'num': record.num,
            'description': record.description,
            'item_id': record.item.id,
            'parent_id': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Launch_operations_itemQuerySet(self.model, using=self._db)

    def _rec_def_resources(self, launch_operationitem):
        from kaf_pas.production.models.operation_def_resources import Operation_def_resources
        from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources

        for operation_def_resource in Operation_def_resources.objects.filter(operation=launch_operationitem.operation):
            Launch_operation_resources.objects.get_or_create(
                launch_operationitem=launch_operationitem,
                resource=operation_def_resource.resource,
                location=operation_def_resource.location,
                location_fin=operation_def_resource.location_fin,
            )

    def createFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()

        Launch_item_viewManager.check_launch(launch=Launches.objects.get(id=data.get('launch_id')))
        _data = data.copy()
        delAttr(_data, 'operation__full_name')

        oparations = _data.get('operation')
        item_id = _data.get('item_id')
        delAttr(_data, 'operation')
        res = []
        if isinstance(oparations, list):
            with transaction.atomic():
                if isinstance(item_id, int):
                    for oparation in oparations:
                        setAttr(_data, 'operation_id', oparation)
                        _res, created = super().get_or_create(**_data)
                        if created:
                            self._rec_def_resources(_res)
                            res1 = model_to_dict(_res)
                            setAttr(res1, 'operation__full_name', _res.operation.full_name)
                            res.append(DelProps(res1))
                elif isinstance(item_id, list):
                    delAttr(_data, 'item_id')
                    for oparation in oparations:
                        for item in item_id:
                            setAttr(_data, 'operation_id', oparation)
                            setAttr(_data, 'item_id', item)
                            _res, created = super().get_or_create(**_data)
                            if created:
                                self._rec_def_resources(_res)
                                res1 = model_to_dict(_res)
                                setAttr(res1, 'operation__full_name', _res.operation.full_name)
                                res.append(DelProps(res1))

        return res

    def updateFromRequest(self, request, removed=None, function=None):
        request = DSRequest(request=request)
        data = request.get_data()
        Launch_item_viewManager.check_launch(launch=Launches.objects.get(id=data.get('launch_id')))
        _data = data.copy()

        delAttr(_data, 'operation__full_name')
        delAttr(_data, 'enabled')
        delAttr(_data, 'id')
        res = super().filter(id=data.get('id')).update(**_data)

        return data

    def deleteFromRequest(self, request, removed=None, ):
        request = DSRequest(request=request)
        res = 0
        tuple_ids = request.get_tuple_ids()
        with transaction.atomic():
            for id, mode in tuple_ids:
                if mode == 'hide':
                    super().filter(id=id).soft_delete()
                else:
                    Launch_item_viewManager.check_launch(launch=Launch_operations_item.objects.get(id=id).launch)
                    qty, _ = super().filter(id=id).delete()
                res += qty
        return res


class Launch_operations_item(Hierarcy):
    description = DescriptionField()
    ed_izm = ForeignKeyProtect(Ed_izm, null=True, blank=True)
    item = ForeignKeyProtect(Item)
    launch = ForeignKeyProtect(Launches)
    num = PositiveIntegerField(db_index=True, default=None)
    old_num = PositiveIntegerField(db_index=True, null=True, blank=True)
    operation = ForeignKeyProtect(Operations)
    operationitem = ForeignKeyProtect(Operations_item)
    props = Launch_operations_itemManager.props()
    qty = PositiveIntegerField(null=True, blank=True, db_index=True)

    objects = Launch_operations_itemManager()

    def __str__(self):
        return f"ID:{self.id}, " \
               f"old_num: {self.old_num}, " \
               f"num: {self.num}, " \
               f"operation: [{self.operation}], " \
               f"operationitem: [{self.operationitem}], " \
               f"qty: {self.qty}, " \
               f"props: {self.props}"


        # return f"ID:{self.id}, \n" \
        #        f"item: [{self.item}], \n" \
        #        f"id_izm: [{self.ed_izm}], \n" \
        #        f"item: [{self.item}], \n" \
        #        f"operation: [{self.operation}], \n" \
        #        f"operationitem: [{self.operationitem}], \n" \
        #        f"qty: {self.qty}, \n" \
        #        f"props: {self.props}, \n" \
        #        f"old_num: {self.old_num}, \n" \
        #        f"num: {self.num}"

    def __repr__(self):
        return self.operation.full_name

    class Meta:
        verbose_name = 'Кросс таблица'
        unique_together = (('item', 'launch', 'operation', 'num', 'operationitem'),)
