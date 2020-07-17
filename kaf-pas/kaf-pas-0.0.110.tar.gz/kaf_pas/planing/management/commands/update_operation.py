import logging

from django.core.management import BaseCommand

from isc_common.auth.models.user import User
from kaf_pas.planing.models.production_ext import Production_ext, WrapperProductionOrder

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 1 -> Конец

        # data = {'date': '2020-07-14T09:02:02.998', 'parent_id': 238845, 'description': None, 'edizm__code': 'шт', 'edizm__name': 'шт.', 'edizm_id': 7, 'enabled': True, 'id': 238847, 'launch_id': 143, 'location_id': 68, 'location__code': '515',
        #         'location__full_name': '/Завод/Цех №5/Участок мелочевки №1(робот, медники)', 'location__name': 'Участок мелочевки №1(робот, медники)', 'location_fin_id': None, 'location_fin__code': None, 'location_fin__full_name': None, 'location_fin__name': None, 'num': 238847,
        #         'production_operation__full_name': '/Цех №5/Слесарно-сборочные/Сварка ЧПУ', 'production_operation__name': 'Сварка ЧПУ', 'production_operation_attrs': None, 'production_operation_colors': None, 'production_operation_edizm__name': 'Секунда', 'production_operation_edizm_id': 4,
        #         'production_operation_id': 131, 'production_operation_num': 2, 'production_operation_qty': 33, 'resource__code': '2K-V5', 'resource__description': 'Станок вертикально-сверлильный', 'resource__name': 'HAAS VF-2DHE', 'resource_id': 12, 'value_sum': '19', 'value_made': '0',
        #         'value1_sum': '1 / 3', 'value1_sum_len': 2, 'value_start': ''}
        #
        # old_data = {'date': '2020-07-14T09:02:02.998', 'parent_id': 238845, 'description': None, 'edizm__code': 'шт', 'edizm__name': 'шт.', 'edizm_id': 7, 'enabled': True, 'id': 238847, 'launch_id': 143, 'location_id': 68, 'location__code': '515',
        #             'location__full_name': '/Завод/Цех №5/Участок мелочевки №1(робот, медники)', 'location__name': 'Участок мелочевки №1(робот, медники)', 'location_fin_id': None, 'location_fin__code': None, 'location_fin__full_name': None, 'location_fin__name': None, 'num': 238847,
        #             'production_operation__full_name': '/Цех №5/Слесарно-сборочные/Сварка ЧПУ', 'production_operation__name': 'Сварка ЧПУ', 'production_operation_attrs': None, 'production_operation_colors': None, 'production_operation_edizm__name': None, 'production_operation_edizm_id': None,
        #             'production_operation_id': 131, 'production_operation_num': 4, 'production_operation_qty': None, 'resource__code': '2K-V5', 'resource__description': 'Станок вертикально-сверлильный', 'resource__name': '2К-В5', 'resource_id': 8, 'value_sum': '19', 'value_made': '0',
        #             'value1_sum': '1 / 3', 'value1_sum_len': 2, 'value_start': ''}


        data = data={'parentRecord': {'creator__short_name': 'Юдин А Г', 'date': '2020-07-14T12:02:02.793', 'description': None, 'edizm_id': 7, 'edizm__name': 'шт.', 'id': 238845, 'item_id': 3171174, 'parent_item_id': 3183262, 'item__STMP_1__value_str': 'Уголок', 'item__STMP_2__value_str': 'К4310.51.01.080', 'launch_id': 143, 'launch__code': '2020 / 07 / 1', 'launch__date': '2020-07-14T07:14:31.000', 'location_id': 12, 'location__name': 'Цех №5', 'location_sector_full_name': '/ Завод / Цех №5 / Участок мелочевки №1(робот, медники)', 'location_sector_id': 68, 'num': '238844', 'isFolder': False, 'cnt_opers': 5, 'value_sum': '19', 'value1_sum': '1 / 3', 'value1_sum_len': 2, 'value_made': '4', 'value_made_str': '<b><div><strong><font color="blue"</font>4</strong></div></b>(21.05%)', 'value_start': '55', 'value_odd': '51', 'opertype__full_name': '/Задание на производство', 'opertype_id': 2, 'parent_id': None, 'status__code': 'restarted', 'status__name': '<div><strong><font color="green"</font>Запущен (повторно)</strong></div>', 'status_id': 31, 'creator_id': None, '_recordComponents_isc_ListGrid_1': {'_rowNumberField': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, '_expansionField': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'launch__code': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'launch__date': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'num': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'date': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'status__name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'item__STMP_1__value_str': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'item__STMP_2__value_str': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'location_sector_full_name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'cnt_opers': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'value_sum': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'value1_sum': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'value_start': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'value_made_str': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'edizm__name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'creator__short_name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'description': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}}, '_selection_30': True, '_embeddedComponents_isc_ListGrid_1': ['isc_ListGrid_1_expansionLayout'], '_expanded_isc_ListGrid_1': True, '_hasExpansionComponent_isc_ListGrid_1': True}, 'production_operation__full_name': '/Цех №5/Нанесение покрытий/Фосфатирование', 'production_operation_edizm__name': None, 'location__full_name': '/Завод/Цех №5/Токарный участок', 'location_fin__full_name': None, 'resource__name': 'XP26S', 'production_operation_id': 87, 'production_operation_qty': 55, 'production_operation_num': 4, 'location_id': 64, 'resource_id': 36}


        old_data = None

        data = WrapperProductionOrder(**data)
        old_data = WrapperProductionOrder(**old_data) if old_data != None else None

        production_ext = Production_ext()
        production_ext.update_operation(data=data, old_data=old_data, user=User.objects.get(id=2))

        print('Done.')
