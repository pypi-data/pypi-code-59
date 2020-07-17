import logging

from django.contrib.postgres.fields import ArrayField
from django.db import transaction
from django.db.models import DecimalField, DateTimeField, TextField, PositiveIntegerField, SmallIntegerField, BigIntegerField
from django.db.models.query import EmptyResultSet

from isc_common import delAttr, Wrapper, NotImplement
from isc_common.auth.models.user import User
from isc_common.fields.code_field import CodeField
from isc_common.fields.related import ForeignKeyProtect, ForeignKeySetNull
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_manager import CommonQuerySet, CommonManager
from isc_common.models.audit import AuditModel
from isc_common.number import DelProps, DecimalToStr
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.ckk.models.locations import Locations
from kaf_pas.ckk.models.locations_users import Locations_users
from kaf_pas.planing.models.operation_operation import Operation_operation
from kaf_pas.planing.models.operation_types import Operation_types
from kaf_pas.planing.models.production_ext import Production_ext
from kaf_pas.production.models.launches import Launches
from kaf_pas.production.models.resource import Resource

logger = logging.getLogger(__name__)


class Production_order_opersQuerySet(CommonQuerySet):

    def get_range_rows(self, start=None, end=None, function=None, json=None, distinct_field_names=None, user=None, *args, **kwargs):
        child_launch_id = json.get('data').get('child_launch_id')
        if child_launch_id and child_launch_id == json.get('data').get('launch_id'):
            child_launch_id = None

        delAttr(json.get('data'), 'child_launch_id')
        queryResult = self._get_range_rows(*args, start=start, end=end, function=function, json=json, distinct_field_names=distinct_field_names)

        try:
            logger.debug(f'\n\n{queryResult.query}\n')
        except EmptyResultSet:
            pass

        res = [function(record, user) for record in queryResult]
        return res


class Production_order_opersManager(CommonManager):
    @staticmethod
    def getRecord(record, user):
        location_ids = [location_user.location.id for location_user in Locations_users.objects.filter(user_id=user)]
        res = {
            # 'location_sector_id': record.location_sector.id,
            'date': record.date,
            'parent_id': record.parent_id,
            'description': record.description,
            'edizm__code': record.edizm.code,
            'edizm__name': record.edizm.name,
            'edizm_id': record.edizm.id,
            'enabled': user.is_develop or user.is_admin or record.resource.location.id in location_ids if record.resource else False,
            'id': record.id,
            'launch_id': record.launch.id,
            'location_id': record.location.id,
            'location__code': record.location.code,
            'location__full_name': record.location.full_name,
            'location__name': record.location.name,
            'location_fin_id': record.location_fin.id if record.location_fin else None,
            'location_fin__code': record.location_fin.code if record.location_fin else None,
            'location_fin__full_name': record.location_fin.full_name if record.location_fin else None,
            'location_fin__name': record.location_fin.name if record.location_fin else None,
            'num': record.id,
            'production_operation__full_name': record.operation_operation.production_operation.full_name if record.operation_operation else None,
            'production_operation__name': record.operation_operation.production_operation.name if record.operation_operation else None,
            'production_operation_attrs': record.production_operation_attrs,
            'production_operation_colors': record.production_operation_colors,
            'production_operation_edizm__name': record.operation_operation.ed_izm.name if record.operation_operation and record.operation_operation.ed_izm else None,
            'production_operation_edizm_id': record.operation_operation.ed_izm.id if record.operation_operation and record.operation_operation.ed_izm else None,
            'production_operation_id': record.operation_operation.production_operation.id if record.operation_operation else None,
            'production_operation_num': record.operation_operation.num if record.operation_operation else None,
            'production_operation_qty': record.operation_operation.qty if record.operation_operation else None,
            'resource__code': record.resource.code,
            'resource__description': record.resource.description,
            'resource__name': record.resource.name,
            'resource_id': record.resource.id,
            'value_sum': DecimalToStr(record.value_sum),
            'value_made': DecimalToStr(record.value_made),
            'value1_sum': ' / '.join([DecimalToStr(v) for v in record.value1_sum]),
            'value1_sum_len': len(record.value1_sum),
            'value_start': DecimalToStr(record.value_start),
        }
        return DelProps(res)

    def createFromRequest(self, request):
        from isc_common.common import create
        raise NotImplement()

        request = DSRequest(request=request)
        production_ext = Production_ext()

        print(f'data={request.get_data()}')

        data = Wrapper(**request.get_data())

        production_ext.update_operation(data=data, user=request.user)

        return data

    def deleteFromRequest(self, request):
        request = DSRequest(request=request)
        raise NotImplement()
        ids = request.get_old_ids()
        res = 0

        with transaction.atomic():
            for id in ids:
                print(id)

        return res

    def updateFromRequest(self, request):
        request = DSRequest(request=request)
        raise NotImplement()
        production_ext = Production_ext()

        print(f'data={request.get_data()}')
        print(f'old_data={request.get_oldValues()}')

        data = Wrapper(**request.get_data())
        old_data = Wrapper(**request.get_oldValues())

        return production_ext.update_operation(data=data, old_data=old_data, user=request.user)

    def get_queryset(self):
        return Production_order_opersQuerySet(self.model, using=self._db)


class Production_order_opers(AuditModel):
    from kaf_pas.planing.models.status_operation_types import Status_operation_types
    from kaf_pas.planing.models.operation_refs import Operation_refsManager

    date = DateTimeField(default=None)
    description = TextField(null=True, blank=True)
    opertype = ForeignKeyProtect(Operation_types, related_name='Production_order_opers_opertype')
    creator = ForeignKeyProtect(User, related_name='Production_order_opers_creator')
    status = ForeignKeyProtect(Status_operation_types)
    operation_operation = ForeignKeySetNull(Operation_operation, null=True, blank=True)
    num = CodeField()
    parent_id = BigIntegerField()
    operation_operation_num = PositiveIntegerField()
    production_operation_num = PositiveIntegerField()
    production_operation_attrs = ArrayField(CodeField(null=True, blank=True))
    production_operation_colors = ArrayField(SmallIntegerField(null=True, blank=True))

    launch = ForeignKeyProtect(Launches)
    location = ForeignKeyProtect(Locations, related_name='Production_order_opers_location')
    location_fin = ForeignKeySetNull(Locations, related_name='Production_order_opers_location_fib', null=True, blank=True)
    resource = ForeignKeyProtect(Resource)
    edizm = ForeignKeyProtect(Ed_izm)
    value_sum = DecimalField(decimal_places=4, max_digits=19)
    value1_sum = ArrayField(DecimalField(decimal_places=4, max_digits=19))
    value_made = DecimalField(decimal_places=4, max_digits=19, null=True, blank=True)
    value_start = DecimalField(decimal_places=4, max_digits=19, null=True, blank=True)
    value_odd = DecimalField(decimal_places=4, max_digits=19)

    props = Operation_refsManager.props()

    objects = Production_order_opersManager()

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return self.__str__()

    class Meta:
        managed = False
        db_table = 'planing_production_order_opers_view'
        verbose_name = 'Операции Заказа на производство'
