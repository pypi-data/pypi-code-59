import logging

from isc_common import Stack

logger = logging.getLogger(__name__)


class Item_refs_Stack(Stack):
    def add_parents(self, id, launch_id=None):
        from kaf_pas.ckk.models.item_refs import Item_refs
        from kaf_pas.production.models import p_id

        if launch_id == None:
            for item_ref in Item_refs.objects.raw(f'''WITH RECURSIVE r AS (
                                                        SELECT *, 1 AS level
                                                        FROM ckk_item_refs
                                                        WHERE child_id IN (%s)
                                                        and parent_id != %s

                                                        union all

                                                        SELECT ckk_item_refs.*, r.level + 1 AS level
                                                        FROM ckk_item_refs
                                                                 JOIN r
                                                                      ON ckk_item_refs.child_id = r.parent_id)

                                                    select  *
                                                    from r
                                                    where child_id != %s order by level desc''', [
                id,
                p_id,
                p_id
            ]):
                self.push(item_ref)
        else:
            for item_ref in Item_refs.objects.raw(f'''WITH RECURSIVE r AS (
                                                        SELECT *, 1 AS level
                                                        FROM production_launch_item_refs
                                                        WHERE child_id IN (%s)

                                                        union all

                                                        SELECT production_launch_item_refs.*, r.level + 1 AS level
                                                        FROM production_launch_item_refs
                                                                 JOIN r
                                                                      ON production_launch_item_refs.child_id = r.parent_id)

                                                    select  *
                                                    from r
                                                    where launch_id = %s order by level desc''', [
                id,
                launch_id
            ]):
                self.push(item_ref)

    @property
    def _get_full_path_obj(self):
        arr = []
        last = self.top()
        if last:
            arr.append(last)
        while True:
            if last.parent != None:
                last = [item for item in self.stack if item.child.id == last.parent.id]
                if len(last) > 0:
                    last = last[0]
                    arr.append(last)
                else:
                    break
            else:
                # arr.append(last)
                break

        arr = [item for item in reversed(arr)]
        return arr

    @property
    def get_full_path_obj(self):
        from kaf_pas.ckk.models.item_operations_view import Item_operations_view
        from kaf_pas.ckk.models.item_operations_view import Item_operations_viewManager
        arr = [Item_operations_viewManager.getRecord(Item_operations_view.objects.get(refs_id=item.id)) for item in self._get_full_path_obj]
        return arr

    @property
    def get_full_path(self):
        arr = self._get_full_path_obj
        # arr = [item for item in arr if arr.parent != None]
        res = ' / '.join([item.child.item_name for item in arr])
        return '/ ' + res


class Ready_2_launch_ext:
    def make(self, demand_id, user, ready_2_launch=None, props=32):

        from django.conf import settings
        from django.db import transaction
        from isc_common import Stack
        from isc_common.auth.models.user import User
        from isc_common.bit import IsBitOn, TurnBitOn
        from isc_common.datetime import DateToStr
        from isc_common.progress import managed_progress, ProgressDroped, progress_deleted
        from kaf_pas.ckk.models.item_line import Item_line
        from kaf_pas.ckk.models.item_refs import Item_refs
        from kaf_pas.production.models import p_id
        from kaf_pas.production.models.operation_material import Operation_material
        from kaf_pas.production.models.operation_resources import Operation_resources
        from kaf_pas.production.models.operations_item import Operations_item
        from kaf_pas.production.models.ready_2_launch import Ready_2_launch
        from kaf_pas.production.models.ready_2_launch_detail import Ready_2_launch_detail
        from kaf_pas.sales.models.demand import Demand

        if not isinstance(demand_id, int):
            raise Exception(f'demand must be int')

        if isinstance(user, int):
            user = User.objects.get(id=user)
        elif not isinstance(user, User):
            raise Exception(f'user must be a User instance or int')

        for demand in Demand.objects.filter(id=demand_id):
            cnt = 0
            cnt_not = 0

            all_notes = Stack()
            options = Stack()

            if IsBitOn(props, 0):
                options.push('Включена опция проверки наличия у операции длительности выполнения.')

            if IsBitOn(props, 1):
                options.push('Включена опция проверки наличия у операции № п/п.')

            if IsBitOn(props, 2):
                options.push('Включена опция проверки наличия у операции материалов или стандартных изделий.')

            if IsBitOn(props, 3):
                options.push('Включена опция проверки наличия у операции ресурса либо места выполнения.')

            if IsBitOn(props, 4):
                options.push('Включена опция проверки наличия у операции единицы измерения.')

            if IsBitOn(props, 5):
                options.push('Включена опция проверки наличия операций.')

            if IsBitOn(props, 6):
                options.push('Включена опция проверки количества.')

            demand_str = f'<h3>Оценка готовности к запуску: Заказ № {demand.code} от {DateToStr(demand.date)}</h3>'

            key = f'Ready_2_launchManager.make_{demand.id}'
            settings.LOCKS.acquire(key)
            qty = Item_refs.objects.get_descendants_count(
                id=demand.precent_item.item.id,
            )
            logger.debug(f'Counted: {qty}')
            with managed_progress(
                    id=f'demand_{demand.id}_{ready_2_launch.props}_{user.id}',
                    qty=qty,
                    user=user,
                    message=demand_str,
                    title='Выполнено',
                    props=TurnBitOn(0, 0)

            ) as progress:
                with transaction.atomic():
                    def except_func():
                        settings.LOCKS.release(key)

                    progress.except_func = except_func

                    if not ready_2_launch:
                        ready_2_launch, _ = Ready_2_launch.objects.get_or_create(demand=demand.id)

                    items_refs_stack = Item_refs_Stack()
                    items_refs_stack.add_parents(demand.precent_item.item.id)

                    for item_ref in Item_refs.objects.get_descendants(
                            id=demand.precent_item.item.id,
                    ):

                        if item_ref.parent and item_ref.parent.id == p_id:
                            continue

                        notes = Stack()

                        # items_refs_stack.push(item_ref, lambda stack, item: len([it for it in stack if it.id != item_ref.id]) == 0)
                        items_refs_stack.push(item_ref)

                        operations_cnt = Operations_item.objects.filter(item=item_ref.child).count()
                        section = None
                        item_full_name = None
                        item_full_name_obj = None
                        cnt_not1 = 0

                        try:
                            item_line = Item_line.objects.get(parent=item_ref.parent, child=item_ref.child)
                            section = item_line.section

                            if section and section != 'Документация':
                                if item_ref.props.used.is_set == False:
                                    notes.push(f'Позиция не используется.')
                                    if not item_full_name:
                                        item_full_name_obj = items_refs_stack.get_full_path_obj
                                        item_full_name = items_refs_stack.get_full_path

                                elif IsBitOn(props, 6) and not item_line.qty:
                                    cnt_not1 += 1
                                    notes.push(f'Не указано количество.')
                                    if not item_full_name:
                                        item_full_name_obj = items_refs_stack.get_full_path_obj
                                        item_full_name = items_refs_stack.get_full_path
                            else:
                                notes.push(f'Найдена документация, требует проверки правильности принадлежности.')
                                if not item_full_name:
                                    item_full_name_obj = items_refs_stack.get_full_path_obj
                                    item_full_name = items_refs_stack.get_full_path

                        except Item_line.DoesNotExist:
                            cnt_not += 1
                            notes.push(f'Не входит в детализацию.')
                            if not item_full_name:
                                item_full_name_obj = items_refs_stack.get_full_path_obj
                                item_full_name = items_refs_stack.get_full_path

                        if item_ref.props.used.is_set == True:
                            if section and section != 'Документация':
                                if operations_cnt == 0:
                                    if IsBitOn(props, 5):
                                        cnt_not += 1
                                        notes.push(f'Не указаны операции.')
                                        item_full_name_obj = items_refs_stack.get_full_path_obj
                                        item_full_name = items_refs_stack.get_full_path
                                else:
                                    for operation in Operations_item.objects.filter(item=item_ref.child):
                                        if IsBitOn(props, 0) and not operation.qty:
                                            cnt_not1 = 1
                                            notes.push(f'Операция: {operation.operation.full_name} не указана длительность.')
                                            if not item_full_name:
                                                item_full_name_obj = items_refs_stack.get_full_path_obj
                                                item_full_name = items_refs_stack.get_full_path

                                        if IsBitOn(props, 1) and not operation.num:
                                            cnt_not1 = 1
                                            notes.push(f'Операция: {operation.operation.full_name} не указан № п/п.')
                                            if not item_full_name:
                                                item_full_name_obj = items_refs_stack.get_full_path_obj
                                                item_full_name = items_refs_stack.get_full_path

                                        if IsBitOn(props, 2):
                                            operation_material_cnt = Operation_material.objects.filter(operationitem=operation).count()
                                            if operation_material_cnt == 0:
                                                cnt_not1 = 1
                                                notes.push(f'Операция: {operation.operation.full_name} не указаны материалы или стандартные изделия.')
                                                if not item_full_name:
                                                    item_full_name_obj = items_refs_stack.get_full_path_obj
                                                    item_full_name = items_refs_stack.get_full_path

                                        if IsBitOn(props, 3):
                                            operation_resources_cnt = Operation_resources.objects.filter(operationitem=operation).count()
                                            if operation_resources_cnt == 0:
                                                cnt_not1 = 1
                                                notes.push(f'Операция: {operation.operation.full_name} не указан ресурс либо место выполнения.')
                                                if not item_full_name:
                                                    item_full_name_obj = items_refs_stack.get_full_path_obj
                                                    item_full_name = items_refs_stack.get_full_path

                                        if IsBitOn(props, 4) and not operation.ed_izm:
                                            cnt_not1 = 1
                                            notes.push(f'Операция: {operation.operation.full_name} не указана единица измерения.')
                                            if not item_full_name:
                                                item_full_name_obj = items_refs_stack.get_full_path_obj
                                                item_full_name = items_refs_stack.get_full_path

                        if notes.size() > 0:
                            notes_str = "\n".join(notes)
                            Ready_2_launch_detail.objects.get_or_create(
                                ready=ready_2_launch,
                                notes=notes_str,
                                item_full_name=item_full_name,
                                item_full_name_obj=item_full_name_obj,
                            )
                        cnt_not += cnt_not1
                        cnt += 1
                        if progress.step() != 0:
                            settings.LOCKS.release(key)
                            raise ProgressDroped(progress_deleted)

                    ready = round(100 - cnt_not / cnt * 100, 2)
                    all_notes.push(f'{ready}%')
                    notes_str = "\n".join(all_notes)
                    ready_2_launch.notes = f'<pre>{notes_str}</pre>'
                    ready_2_launch.save()

                    options_str = "\n" + "\n".join(options)
                    settings.EVENT_STACK.EVENTS_PRODUCTION_READY_2_LAUNCH.send_message(f'Выполнена {demand_str} <h3>готовность: {ready} </h3>{options_str}<p/>')
            settings.LOCKS.release(key)
