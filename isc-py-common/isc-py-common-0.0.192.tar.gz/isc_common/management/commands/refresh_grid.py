import logging

from django.conf import settings
from django.core.management import BaseCommand

from isc_common.ws.webSocket import WebSocket

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):

        record = {'creator__short_name': 'Юдин А Г', 'description': None, 'edizm_id': 7, 'edizm__name': 'шт.', 'id': 237989, 'item_id': 3370530, 'parent_item_id': 3175828, 'item__STMP_1__value_str': 'Домкрат гидравлический', 'item__STMP_2__value_str': None, 'launch_id': 143, 'launch__code': '2020 / 07 / 1', 'launch__date': '2020-07-14T07:14:31.000', 'location_id': 17, 'location__name': 'ОМТС', 'location_sector_full_name': '/ Завод / ОМТС / Общий склад', 'location_sector_id': 117, 'num': '237988', 'isFolder': False, 'cnt_opers': 1, 'value_sum': '14', 'value1_sum': '1', 'value1_sum_len': 1, 'value_made': '', 'value_made_str': '<b><div><strong><font color="blue"</font></strong></div></b>(0.00%)', 'value_start': 51, 'value_odd': '99', 'opertype__full_name': '/Задание на производство', 'opertype_id': 2, 'parent_id': None, 'status__code': 'started', 'status__name': '<div><strong><font color="green"</font>Запущен</strong></div>', 'status_id': 14, 'creator_id': None, 'deleted_at': None, 'editing': False, 'deliting': False, 'parent': None, 'creator': 2, 'opertype': 2, 'status': 31}
        WebSocket.row_refresh_grid(settings.GRID_CONSTANTS.refresh_production_order_grid_row, record)
