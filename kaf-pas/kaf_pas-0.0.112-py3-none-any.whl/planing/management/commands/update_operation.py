import logging

from django.core.management import BaseCommand

from isc_common import NotImplement
from isc_common.auth.models.user import User
from kaf_pas.planing.models.production_ext import Production_ext

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 1 -> Конец

        # data = {'date': '2020-07-18T12:51:04.422', 'parent_id': 236827, 'description': None, 'edizm__code': 'шт', 'edizm__name': 'шт.', 'edizm_id': 7, 'enabled': True, 'id': 236831, 'launch_id': 135, 'location_id': 68, 'location__code': '515',
        #         'location__full_name': '/Завод/Цех №5/Участок мелочевки №1(робот, медники)', 'location__name': 'Участок мелочевки №1(робот, медники)', 'location_fin_id': None, 'location_fin__code': None, 'location_fin__full_name': None, 'location_fin__name': None, 'num': 236831,
        #         'production_operation__full_name': '/Цех №5/Слесарно-сборочные/Зачистка', 'production_operation__name': 'Зачистка', 'production_operation_attrs': None, 'production_operation_colors': None, 'production_operation_edizm__name': 'Минута', 'production_operation_edizm_id': 5,
        #         'production_operation_id': 17, 'production_operation_num': 2, 'production_operation_qty': 12, 'resource__code': 'none', 'resource__description': None, 'resource__name': '7523', 'resource_id': 25, 'value_sum': '19', 'value_made': '20', 'value1_sum': '1 / 3', 'value1_sum_len': 2,
        #         'value_start': '50'}
        #
        # old_data = {'date': '2020-07-18T12:51:04.422', 'parent_id': 236827, 'description': None, 'edizm__code': 'шт', 'edizm__name': 'шт.', 'edizm_id': 7, 'enabled': True, 'id': 236831, 'launch_id': 135, 'location_id': 68, 'location__code': '515',
        #             'location__full_name': '/Завод/Цех №5/Участок мелочевки №1(робот, медники)', 'location__name': 'Участок мелочевки №1(робот, медники)', 'location_fin_id': None, 'location_fin__code': None, 'location_fin__full_name': None, 'location_fin__name': None, 'num': 236831,
        #             'production_operation__full_name': '/Цех №5/Слесарно-сборочные/Зачистка', 'production_operation__name': 'Зачистка', 'production_operation_attrs': None, 'production_operation_colors': None, 'production_operation_edizm__name': None, 'production_operation_edizm_id': None,
        #             'production_operation_id': 17, 'production_operation_num': 2, 'production_operation_qty': None, 'resource__code': 'none', 'resource__description': None, 'resource__name': 'Не определен', 'resource_id': 197, 'value_sum': '19', 'value_made': '20', 'value1_sum': '1 / 3',
        #             'value1_sum_len': 2, 'value_start': '50'}

        # data = {
        #     'parentRecord': {'creator__short_name': 'Юдин А Г', 'date': '2020-07-19T16:21:43.070', 'description': None, 'edizm_id': 7, 'edizm__name': 'шт.', 'id': 231157, 'item_id': 3171174, 'parent_item_id': 3183262, 'item__STMP_1__value_str': 'Уголок', 'item__STMP_2__value_str': 'К4310.51.01.080',
        #                      'launch_id': 140, 'launch__code': '2020 / 07 / 1', 'launch__date': '2020-07-19T16:07:46.000', 'location_id': 12, 'location__name': 'Цех №5', 'location_sector_full_name': '/ Завод / Цех №5 / Участок мелочевки №1(робот, медники)', 'location_sector_id': 68, 'num': '231156',
        #                      'isFolder': False, 'cnt_opers': 5, 'value_sum': '19', 'value1_sum': '1 / 3', 'value1_sum_len': 2, 'value_made': '', 'value_made_str': '<b><div><strong><font color="blue"</font></strong></div></b>(0.00%)', 'value_start': '', 'value_odd': '0',
        #                      'opertype__full_name': '/Задание на производство', 'opertype_id': 2, 'parent_id': None, 'status__code': 'new', 'status__name': '<div><strong><font color="blue"</font>Новый (с)</strong></div>', 'status_id': 3, 'creator_id': None,
        #                      '_recordComponents_isc_ListGrid_0': {'_rowNumberField': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}, '_expansionField': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1},
        #                                                           'launch__code': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}, 'launch__date': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1},
        #                                                           'num': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}, 'date': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1},
        #                                                           'status__name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}, 'item__STMP_1__value_str': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1},
        #                                                           'item__STMP_2__value_str': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}, 'location_sector_full_name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1},
        #                                                           'cnt_opers': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}, 'value_sum': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1},
        #                                                           'value1_sum': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}, 'value_start': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1},
        #                                                           'value_made_str': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}, 'edizm__name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1},
        #                                                           'creator__short_name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}, 'description': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_0_body', '_recordComponentBatch': 1}},
        #                      '_selection_48': True, '_embeddedComponents_isc_ListGrid_0': ['isc_ListGrid_0_expansionLayout'], '_expanded_isc_ListGrid_0': True, '_hasExpansionComponent_isc_ListGrid_0': True}, 'production_operation__full_name': '/Цех №5/Обработка давлением/Галтовка',
        #     'production_operation_edizm__name': None, 'location__full_name': None, 'location_fin__full_name': None, 'resource__name': 'KGB 25', 'production_operation_qty': 32, 'production_operation_num': 3, 'resource_id': 24, 'production_operation_id': 197}
        #
        # old_data = None

        production_ext = Production_ext()
        # production_ext.update_operation(data=data, old_data=old_data, user=User.objects.get(id=2))

        production_ext.delete_operation(ids=231535, user=User.objects.get(id=2))
        # production_ext.delete_operation(ids=231159)
        raise NotImplement()

        print('Done.')
