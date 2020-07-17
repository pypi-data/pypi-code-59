import logging
from datetime import datetime

import kaf_pas
from events.events_manager import Event
from isc_common import Stack, StackElementNotExist, NotImplement, setAttr, Wrapper
from isc_common.auth.models.user import User
from isc_common.common import blinkString
from isc_common.ws.webSocket import WebSocket
from kaf_pas.planing.models.rouning_ext import Routing_ext

logger = logging.getLogger(__name__)


class Operation_executor_message():
    def __init__(self, executor, message):
        self.executor = executor
        self.message = message

    def __str__(self):
        return f'executor : {self.executor}, message: {self.message}'


class Operation_executor_stack(Stack):
    len = 0

    def push(self, item: Operation_executor_message, logger=None):
        from isc_common.auth.models.user import User
        if not isinstance(item.executor, User):
            raise Exception(f'executor mast be User instance')

        try:
            executor = self.find_one(lambda _item: _item.executor.id == item.executor.id)
            if executor.messages.push(item.message, lambda _: executor.messages.exists(lambda _item: item == item.message), logger):
                self.len += 1
        except StackElementNotExist:
            super().push(Operation_executor_messages(executor=item.executor, message=item.message))
            self.len += 1


class OperationEvent(Event):
    def send_message(self, message=None, users_array=None, progress=None, len=None):
        from isc_common.auth.models.user import User
        if isinstance(users_array, User):
            users_array = [users_array]
        super().send_message(message=message, users_array=users_array, progress=progress)

    def send_message1(self, operation_executor_stack: Operation_executor_stack, progress=None):
        for operation_executor_messages in operation_executor_stack.stack:
            for message in operation_executor_messages.messages.stack:
                super().send_message(message=message, users_array=[operation_executor_messages.executor], progress=progress)


class Operation_executor_messages():
    def __init__(self, executor, message):
        self.executor = executor
        self.messages = Stack([message])


class OperationPlanItem:
    # Определить цех ресурса
    def get_resource_workshop(self, resource):
        from kaf_pas.ckk.models.locations import Locations
        from django.conf import settings

        res = None
        for location in Locations.objects_tree.get_parents(id=resource.location.id, child_id='id', include_self=False):
            if location.props.isWorkshop == True:
                res, _ = settings.OPERS_STACK.NOT_UNDEFINED_WORKSHOP(location)
                return res

        if res == None:
            raise Exception(f'Не обнаружен цех, с признаком "Уровень цеха" для : Location ID: {resource.location.id} {resource.location.full_name}, Resource ID: {resource.id}: {resource.name}')
        return res

    def get_locations_users_query(self, resource):
        from kaf_pas.ckk.models.locations_users import Locations_users
        from isc_common.common import blinkString

        locations_users_query = Locations_users.objects.filter(location=resource.location, parent__isnull=True)
        if locations_users_query.count() == 0:
            raise Exception(blinkString(text=f'Не обнаружен ответственный исполнитель для : {resource.location.full_name}', bold=True))

        return locations_users_query

    def __init__(self, *args, **kwargs):
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.production.models.resource import Resource
        from kaf_pas.production.models.operations_item import Operations_item
        from kaf_pas.production.models.operation_resources import Operation_resources
        from kaf_pas.production.models.operation_material import Operation_material
        from django.db import connection
        from django.conf import settings

        class OperationsItem:
            def __init__(self, operation_item):
                operation_resources = Operation_resources.objects.get(operationitem=operation_item)
                self.operation_item = operation_item
                self.operation_resource = operation_resources
                self.ed_izm = operation_item.ed_izm
                self.num = operation_item.num
                self.operation = operation_item.operation
                self.old_num = operation_item.old_num
                self.qty = operation_item.qty
                self.resource = operation_resources.resource
                self.location_fin = operation_resources.location_fin
                if self.resource == None:
                    self.resource, _ = Resource.objects.get_or_create(location=self.operation_resource.location, code='none')
                self.operation_materials = Stack([operation_material for operation_material in Operation_material.objects.filter(operationitem=operation_item)])

            def __str__(self):
                return f'''\n\noperation_item: [\n\n{self.operation_item}] \n operation_resource: [{self.operation_resource}] \n operation_materials: [[{", ".join([operation_material for operation_material in self.operation_materials])}]]'''

        class LaunchSumValue:
            def __init__(self, sum_value, sum_value1, edizm_id, launch_id, item_id):
                from kaf_pas.production.models.launches import Launches

                self.sum_value = sum_value
                self.sum_value1 = sum_value1
                self.edizm_id = edizm_id
                self.item_id = item_id
                self.launch = Launches.objects.get(id=launch_id)

            def __str__(self):
                return f'sum: {self.sum}, launch: [{self.launch}]'

        class LaunchSumValues(Stack):
            def __init__(self, item, launch_ids):
                self.stack = []
                with connection.cursor() as cursor:
                    sql_str = f'''select sum(distinct pov.value),
                                           sum(distinct pov1.value),
                                           pol.launch_id,
                                           pov.edizm_id 
                                    from planing_operation_launches as pol
                                             join planing_operations as po on po.id = pol.operation_id
                                             join planing_operation_item as poit on po.id = poit.operation_id
                                             join planing_operation_value pov on pov.operation_id = po.id
                                             join planing_operation_value pov1 on pov1.operation_id = po.id
                                    where pol.launch_id in %s
                                      and po.opertype_id = %s
                                      and poit.item_id = %s
                                      and is_bit_on(pov.props::integer, 0) = false
                                      and is_bit_on(pov1.props::integer, 0) = true
                                    group by pol.launch_id, pov.edizm_id'''

                    cursor.execute(sql_str, [launch_ids, settings.OPERS_TYPES_STACK.ROUTING_TASK.id, item.id])
                    rows = cursor.fetchall()

                    for row in rows:
                        sum_value, sum_value1, launch_id, edizm_id = row
                        l = LaunchSumValue(sum_value=sum_value, sum_value1=sum_value1, edizm_id=edizm_id, launch_id=launch_id, item_id=item.id)
                        self.push(l)

            def __str__(self):
                return '\n\n'.join([f'[{elem}]' for elem in self.stack])

        if len(kwargs) == 0:
            raise Exception(f'{self.__class__.__name__} kwargs is empty')

        for k, v in kwargs.items():
            setattr(self, k, v() if callable(v) else v)

        if isinstance(self.item_id, int):
            self.item = Item.objects.get(id=self.item_id)

        if self.item == None:
            raise Exception(f'self.item not determined')

        with connection.cursor() as cursor:
            self.operations_item = Stack([OperationsItem(operation_item) for operation_item in Operations_item.objects.filter(item=self.item).order_by('num')])

            self.resources_location_fin_arr = [(operation_item.resource, operation_item.location_fin) for operation_item in self.operations_item.stack]

            operation_item = self.operations_item.stack[0].operation_item
            resource = Operation_resources.objects.get(operationitem=operation_item)
            top_resource = self.get_resource_workshop(resource)

            self.locations_users = [location_user for location_user in self.get_locations_users_query(resource=top_resource)]

        self.launchSumValues = LaunchSumValues(item=self.item, launch_ids=self.launch_ids)

    def __str__(self):
        # return f'item: {self.item} \n value_sum: {self.value}\n value_per_one: {self.value1}\n\n launchSumValues: [\n{self.launchSumValues.stack}\n] \n\n operations_item: [\n{", ".join([f"[{elem}]" for elem in self.operations_item])}]'
        return f'item: {self.item} \n value_sum: {self.value}\n  launchSumValues: [\n{self.launchSumValues.stack}\n] \n\n operations_item: [\n{", ".join([f"[{elem}]" for elem in self.operations_item])}]'


class WrapperProductionOrder(Wrapper):
    description = None
    edizm_id = None
    id = None
    launch_id = None
    location_fin_id = None
    location_id = None
    production_operation_edizm_id = None
    production_operation_id = None
    production_operation_num = None
    production_operation_qty = None
    qty = None
    resource_id = None


class Production_ext:
    routing_ext = Routing_ext()

    def start(self, qty, _data, user, lock=True):
        from django.conf import settings
        from django.db import connection
        from django.forms import model_to_dict
        from isc_common.common import new
        from isc_common.common import restarted
        from isc_common.common.functions import ExecuteStoredProc
        from kaf_pas.planing.models.operation_launches import Operation_launches
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.models.operation_value import Operation_value
        from kaf_pas.planing.models.operations import Operations
        from kaf_pas.planing.models.operations_view import Operations_view

        _res = []
        key = f'''get_setStartStatus_{_data.get('id')}'''
        if lock:
            settings.LOCKS.acquire(key)
        try:
            value_made = ExecuteStoredProc('get_value_made', [_data.get('id'), _data.get('launch_id')])

            if value_made > qty:
                if lock:
                    settings.LOCKS.release(key)
                raise Exception('Количество выпуска больше введенной суммы.')

            parent = Operations.objects.get(id=_data.get('id'))

            operation_refs = Operation_refs.objects.filter(
                parent=parent,
                child__opertype_id=settings.OPERS_TYPES_STACK.LAUNCH_TASK.id
            )

            if operation_refs.count() > 0:
                if qty == 0:
                    Operation_value.objects.filter(operation=operation_refs[0].child).delete()
                    Operation_launches.objects.filter(operation=operation_refs[0].child).delete()
                    parent.status = settings.OPERS_TYPES_STACK.PRODUCTION_TASK_STATUSES.get(new)
                    operation_refs.delete()

                else:
                    Operation_value.objects.update_or_create(operation=operation_refs[0].child, defaults=dict(value=qty))
                    Operation_launches.objects.get_or_create(
                        operation=operation_refs[0].child,
                        launch=Operations_view.objects.get(id=operation_refs[0].child.id).launch
                    )
                    parent.status = settings.OPERS_TYPES_STACK.PRODUCTION_TASK_STATUSES.get(restarted)

                parent.creator = user
                parent.save()

                if qty != 0:
                    res = model_to_dict(operation_refs[0].parent)
                    # _data.update(res)
                    _res.append(_data)

                setAttr(_data, 'value_start', qty)

            else:
                if qty == 0:
                    if lock:
                        settings.LOCKS.release(key)
                    return _res

                res = Operations.objects.create(
                    opertype=settings.OPERS_TYPES_STACK.LAUNCH_TASK,
                    date=datetime.now(),
                    status=settings.OPERS_TYPES_STACK.LAUNCH_TASK_STATUSES.get('new'),
                    creator=user
                )

                parent = Operations.objects.get(id=_data.get('id'))
                parent.status = settings.OPERS_TYPES_STACK.PRODUCTION_TASK_STATUSES.get('started')
                parent.creator = user
                parent.save()

                Operation_refs.objects.create(parent=parent, child=res)
                Operation_value.objects.create(operation=res, edizm_id=_data.get('edizm_id'), value=qty)
                Operation_launches.objects.get_or_create(operation=res, launch_id=_data.get('launch_id'))

                with connection.cursor() as cursor:
                    cursor.execute(f'''select distinct clu.user_id
                                    from planing_operation_refs porf
                                             join planing_operation_resources pors on pors.operation_id = porf.child_id
                                             join production_resource prdrs on pors.resource_id = prdrs.id
                                             join ckk_locations_users clu on clu.location_id = prdrs.location_id
                                             join isc_common_user icu on clu.user_id = icu.id
                                    where get_opertype_code(porf.child_id) = 'DETAIL_OPERS_PRD_TSK'
                                      and porf.parent_id = %s''', [parent.id])
                    rows = cursor.fetchall()

                    self.set_executors(executors=[row for row, in rows], operation_id=parent.id)

                res = model_to_dict(res)
                # _data.update(res)
                setAttr(_data, 'value_start', qty)
                _res.append(_data)

            if lock:
                settings.LOCKS.release(key)

                WebSocket.row_refresh_grid(grid_id=settings.GRID_CONSTANTS.refresh_production_order_grid_row, records=[_data])
                WebSocket.full_refresh_grid(grid_id=f'''{settings.GRID_CONSTANTS.refresh_operationsGrid}_{_data.get('id')}''')
            return _res
        except Exception as ex:
            if lock:
                settings.LOCKS.release(key)
            raise ex

    def set_executors(self, executors, operation_id, user=None):
        from kaf_pas.planing.models.operation_executor import Operation_executor
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_resources import Operation_resources
        from kaf_pas.planing.models.operations import Operations
        from django.conf import settings
        from isc_common.auth.models.user import User

        if isinstance(executors, list):
            if user != None:
                operation_executor = Operation_executor.objects.get(operation_id=operation_id, executor=user)
                operation_executor.props |= Operation_executor.props.rearrange
                operation_executor.save()

            for executor_id in executors:
                operation_executor, created = Operation_executor.objects.get_or_create(operation_id=operation_id, executor_id=executor_id)

                main_oper_production_order = Operations.objects.get(id=operation_id)
                operation_item = Operation_item.objects.get(operation=main_oper_production_order)

                settings.EVENT_STACK.EVENTS_PRODUCTION_ORDER_CREATE.send_message(
                    message=blinkString(f'<h4>Вам направлено: {Operation_resources.objects.filter(operation_id=operation_id).distinct().count()} новых заданий на производство.</h4>', bold=True),
                    users_array=User.objects.get(id=executor_id),
                )

    def rec_operation(self, launch, status, operations_item, item, operation, opertype, user, props=0):
        from datetime import datetime
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_launches import Operation_launches
        from kaf_pas.planing.models.operation_material import Operation_material
        from kaf_pas.planing.models.operation_operation import Operation_operation
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.models.operation_resources import Operation_resources
        from kaf_pas.planing.models.operations import Operations
        from kaf_pas.production.models.launches import Launches

        if isinstance(launch, int):
            launch = Launches.objects.get(id=launch)

        if isinstance(item, int):
            item = Item.objects.get(id=item)

        if isinstance(operation, int):
            operation = Operations.objects.get(id=operation)

        production_order_operation_opers = Operations.objects.create(
            date=datetime.now(),
            opertype=opertype,
            status=status,
            creator=user,
            editing=False,
            deliting=False
        )

        operation_launches = Operation_launches.objects.create(
            operation=production_order_operation_opers,
            launch=launch
        )
        logger.debug(f'Created operation_launches :  {operation_launches}')

        if operations_item.resource != None:
            operation_resources = Operation_resources.objects.create(
                operation=production_order_operation_opers,
                resource=operations_item.resource,
                location_fin=operations_item.location_fin
            )
            logger.debug(f'Created operation_resources :  {operation_resources}')

        for operation_material in operations_item.operation_materials:
            operation_material = Operation_material.objects.create(
                operation=production_order_operation_opers,
                material=operation_material.material,
                material_askon=operation_material.material_askon,
                edizm=operation_material.edizm,
                qty=operation_material.qty,
            )
            logger.debug(f'Created operation_material :  {operation_material}')

        operation_operation = Operation_operation.objects.create(
            ed_izm=operations_item.ed_izm,
            num=operations_item.num,
            operation=production_order_operation_opers,
            production_operation=operations_item.operation,
            qty=operations_item.qty,
            creator=user,
            props=props
        )
        logger.debug(f'Created operation_operation :  {operation_operation}')

        operation_item, created = Operation_item.objects.get_or_create(
            operation=production_order_operation_opers,
            item=item,
        )
        if created:
            logger.debug(f'Created operation_item :  {operation_item}')

        operation_refs = Operation_refs.objects.create(
            parent=operation,
            child=production_order_operation_opers,
            props=Operation_refs.props.product_order_routing
        )
        logger.debug(f'Created operation_refs :  {operation_refs}')
        return production_order_operation_opers.id

    def rec_operations(self, launch, status, operationPlanItem, operation, opertype, user):

        for operations_item in operationPlanItem.operations_item:
            self.rec_operation(
                launch=launch,
                status=status,
                operations_item=operations_item,
                item=operationPlanItem.item,
                operation=operation,
                opertype=opertype,
                user=user
            )

    def rec_item(self, item_id, launch_childs_ids, launch_parent, user, operation_executor_stack, route_opers_lunch):
        from datetime import datetime
        from django.conf import settings
        from kaf_pas.planing.models.operation_executor import Operation_executor
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_launches import Operation_launches
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.models.operation_resources import Operation_resources
        from kaf_pas.planing.models.operation_value import Operation_value
        from kaf_pas.planing.models.operations import Operations
        from isc_common.datetime import DateTimeToStr

        route_oparation_item = dict(
            item_id=item_id,
            launch_ids=launch_childs_ids,
            launch_parent_id=launch_parent.id
        )

        operationPlanItem = OperationPlanItem(**route_oparation_item)

        # Головная операция заказа
        production_order_operation = Operations.objects.create(
            date=datetime.now(),
            opertype=settings.OPERS_TYPES_STACK.PRODUCTION_TASK,
            status=settings.OPERS_TYPES_STACK.PRODUCTION_TASK_STATUSES.get('new'),
            creator=user,
            editing=False,
            deliting=False
        )
        logger.debug(f'Created operation :  {production_order_operation}')

        operation_launches = Operation_launches.objects.create(
            operation=production_order_operation,
            launch=launch_parent
        )
        logger.debug(f'Created operation_launches :  {operation_launches}')

        operation_item = Operation_item.objects.create(
            operation=production_order_operation,
            item=operationPlanItem.item,
        )
        logger.debug(f'Created operation_item :  {operation_item}')

        for launch_child_id in launch_childs_ids:
            for route_oper_lunch in route_opers_lunch:
                if route_oper_lunch[1] == launch_child_id:
                    for item_id in route_oper_lunch[0]:
                        operation_refs = Operation_refs.objects.create(
                            child=production_order_operation,
                            parent_id=item_id,
                            props=Operation_refs.props.product_order_routing
                        )
                        logger.debug(f'Created operation_refs :  {operation_refs}')

        for resources_location_fin in operationPlanItem.resources_location_fin_arr:
            operation_resources, created = Operation_resources.objects.get_or_create(
                operation=production_order_operation,
                resource=resources_location_fin[0],
                location_fin=resources_location_fin[1]
            )
            if created:
                logger.debug(f'Created operation_resources :  {operation_resources}')

        self.rec_operations(
            launch=launch_parent,
            status=settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_OPERS_TASK_STATUSES.get('new'),
            operationPlanItem=operationPlanItem,
            operation=production_order_operation,
            opertype=settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_OPERS_TASK,
            user=user
        )

        for launchSumValue in operationPlanItem.launchSumValues.stack:
            production_order_operation_launch = Operations.objects.create(
                date=datetime.now(),
                opertype=settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_SUM_TASK,
                status=settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_SUM_TASK_STATUSES.get('new'),
                creator=user,
                editing=False,
                deliting=False
            )
            logger.debug(f'Created operation :  {production_order_operation}')

            operation_launches = Operation_launches.objects.create(
                operation=production_order_operation_launch,
                launch=launchSumValue.launch
            )
            logger.debug(f'Created operation_launches :  {operation_launches}')

            operation_value = Operation_value.objects.create(
                operation=production_order_operation_launch,
                edizm_id=launchSumValue.edizm_id,
                value=launchSumValue.sum_value
            )
            logger.debug(f'Created operation_value :  {operation_value}')

            operation_value = Operation_value.objects.create(
                operation=production_order_operation_launch,
                edizm_id=launchSumValue.edizm_id,
                value=launchSumValue.sum_value1,
                props=Operation_value.props.perone
            )
            logger.debug(f'Created operation_value :  {operation_value}')

            operation_refs = Operation_refs.objects.create(
                child=production_order_operation_launch,
                parent=production_order_operation,
                props=Operation_refs.props.product_order_routing
            )
            logger.debug(f'Created operation_refs :  {operation_refs}')

        for location_user in operationPlanItem.locations_users:
            operation_executor = Operation_executor.objects.create(
                operation=production_order_operation,
                executor=location_user.user,
            )
            logger.debug(f'Created operation_executor :  {operation_executor}')
            message = f'<h3>Размещен новый заказ на производство ' \
                      f'№{production_order_operation.num} от {DateTimeToStr(production_order_operation.date, hours=3)}.' \
                      '<p/>' \
                      f'{operation_item.item.item_name}' \
                      '<p/>' \
                      f'{location_user.location.full_name}' \
                      '<p/>'

            operation_executor_stack.push(
                Operation_executor_message(executor=location_user.user, message=message),
                logger
            )

    def make_production_order(self, data):
        from django.conf import settings
        from django.db import transaction
        from isc_common.bit import TurnBitOn
        from isc_common.common import blinkString
        from isc_common.datetime import DateToStr
        from isc_common.progress import managed_progress
        from isc_common.progress import progress_deleted
        from isc_common.progress import ProgressDroped
        from isc_common.ws.webSocket import WebSocket
        from kaf_pas.production.models.launches import Launches
        from kaf_pas.production.models.launches import LaunchesManager

        user = data.get('user')
        if isinstance(user, int):
            from isc_common.auth.models.user import User
            user = User.objects.get(id=user)

        class Launch_pair:
            def __init__(self, child, parent):
                self.child = Launches.objects.get(id=child)
                self.parent = Launches.objects.get(id=parent)

            def __str(self):
                return f'child: [{self.child}], parent: [{self.parent}]'

        class Launch_pairs(Stack):
            def get_parents(self):
                res = set()
                for item in self.stack:
                    for item1 in item:
                        res.add(item1.parent)

                return list(res)

            def get_childs(self, parent):
                res = set()
                for item in self.stack:
                    res1 = [i.child for i in item if i.parent == parent]
                    for r in res1:
                        res.add(r)
                return list(res)

        launch_pairs = Launch_pairs()

        launches_head = []
        for launch_id in data.get('data'):
            l = Launches.objects.filter(parent_id=launch_id)
            if l.count() > 0:
                launch_pairs.push([Launch_pair(parent=launch_id, child=item.id) for item in l])
                launches_head.append(Launches.objects.get(id=launch_id))
            else:
                launch_pairs.push([Launch_pair(parent=item.id, child=item.id) for item in Launches.objects.filter(id=launch_id)])

        for launch_parent in launch_pairs.get_parents():
            if launch_parent.status == settings.PROD_OPERS_STACK.IN_PRODUCTION:
                continue

            key = f'OperationsManager.make_production_order_{launch_parent.id}'
            settings.LOCKS.acquire(key)

            launch_childs = launch_pairs.get_childs(parent=launch_parent)
            launch_childs_ids = tuple([launch.id for launch in launch_childs])

            operation_executor_stack = Operation_executor_stack()

            sql_items = '''select poit.item_id
                                 from planing_operation_item as poit
                                   join planing_operation_launches as pol on poit.operation_id = pol.operation_id
                                   join planing_operations as po on po.id = pol.operation_id
                                 where pol.launch_id in %s
                                   and po.opertype_id = %s
                                 group by poit.item_id'''

            sql_items_launch = '''select array_agg(poit_det.operation_id)
                                       from planing_operation_item as poit_det
                                                join planing_operation_launches as pol on poit_det.operation_id = pol.operation_id
                                                join planing_operations as po on po.id = pol.operation_id
                                       where pol.launch_id = %s
                                         and po.opertype_id = %s
                                         and poit_det.item_id = %s
                                       group by pol.launch_id'''

            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute(f'''select count(*)
                                           from ({sql_items}) as s''', [launch_childs_ids, settings.OPERS_TYPES_STACK.ROUTING_TASK.id])
                qty, = cursor.fetchone()
                logger.debug(f'qty: {qty}')

                message = [f'<h3>Создание заданий на производство ({qty} товарных позиций) <p/>']

                message.extend([blinkString(f'Запуск № {launch.code} от {DateToStr(launch.date)}', blink=False, bold=True, color='blue') for launch in launch_childs])
                message = '<br/>'.join(message)

                with managed_progress(
                        id=f'order_by_prod_launch_{launch_parent.id}_{user.id}',
                        qty=qty,
                        user=user,
                        message=message,
                        title='Выполнено',
                        props=TurnBitOn(0, 0)
                ) as progress:

                    with transaction.atomic():
                        def except_func():
                            settings.LOCKS.release(key)

                        progress.except_func = except_func

                        cursor.execute(sql_items, [launch_childs_ids, settings.OPERS_TYPES_STACK.ROUTING_TASK.id])
                        rows = cursor.fetchall()
                        for row in rows:
                            item_id, = row

                            route_opers_lunch = []
                            for launch_childs_id in launch_childs_ids:
                                cursor.execute(sql_items_launch, [launch_childs_id, settings.OPERS_TYPES_STACK.ROUTING_TASK.id, item_id])
                                rows_lunch = cursor.fetchall()
                                for row_lunch in rows_lunch:
                                    row_lunch, = row_lunch
                                    route_opers_lunch.append((row_lunch, launch_childs_id))

                            self.rec_item(
                                item_id=item_id,
                                launch_childs_ids=launch_childs_ids,
                                launch_parent=launch_parent,
                                user=user,
                                operation_executor_stack=operation_executor_stack,
                                route_opers_lunch=route_opers_lunch
                            )

                            if progress.step() != 0:
                                WebSocket.full_refresh_grid(grid_id=settings.GRID_CONSTANTS.refresh_production_launch_grid)
                                settings.LOCKS.release(key)
                                raise ProgressDroped(progress_deleted)

                        launch_parent.status = settings.PROD_OPERS_STACK.IN_PRODUCTION
                        launch_parent.save()

                        for launch_child in launch_childs:
                            launch_child.status = settings.PROD_OPERS_STACK.IN_PRODUCTION
                            launch_child.save()

                            WebSocket.row_refresh_grid(
                                grid_id=settings.GRID_CONSTANTS.refresh_production_launch_grid_row,
                                records=LaunchesManager.getRecord(launch_child)
                            )

                        WebSocket.row_refresh_grid(
                            grid_id=settings.GRID_CONSTANTS.refresh_production_launch_grid_row,
                            records=LaunchesManager.getRecord(launch_parent)
                        )

                        WebSocket.full_refresh_grid(grid_id=settings.GRID_CONSTANTS.refresh_production_order_grid)

                        settings.LOCKS.release(key)

                    for operation_executor in operation_executor_stack.stack:
                        settings.EVENT_STACK.EVENTS_PRODUCTION_ORDER_CREATE.send_message(
                            message=blinkString(f'<h4>Вам направлено: {operation_executor.messages.size()} новых заданий на производство.</h4>', bold=True),
                            users_array=[operation_executor.executor],
                            progress=progress,
                        )
        # refresh_mat_view('planing_production_order_mview')

    def delete_production_order(self, data):
        from django.conf import settings
        from django.db import transaction
        from isc_common.bit import TurnBitOn
        from isc_common.common import blinkString
        from isc_common.datetime import DateTimeToStr
        from isc_common.datetime import DateToStr
        from isc_common.progress import managed_progress
        from isc_common.progress import progress_deleted
        from isc_common.progress import ProgressDroped
        from isc_common.ws.webSocket import WebSocket
        from kaf_pas.planing.models.operation_executor import Operation_executor
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.models.operation_resources import Operation_resources
        from kaf_pas.planing.models.operations import Operations
        from kaf_pas.planing.models.operations_view import Operations_view
        from kaf_pas.planing.models.production_order_opers import Production_order_opers
        from kaf_pas.planing.models.production_order_values import Production_order_valuesManager
        from kaf_pas.production.models.launches import Launches
        from kaf_pas.production.models.launches import LaunchesManager
        from kaf_pas.production.models.launches_view import Launches_view

        user = data.get('user')
        launch_ids = data.get('data')

        if isinstance(user, int):
            from isc_common.auth.models.user import User
            user = User.objects.get(id=user)

        operation_executor_stack = Operation_executor_stack()

        launch_cnt = len(launch_ids)
        idx = 0
        for parent_launch_id in launch_ids:
            parent_launch = Launches.objects.get(id=parent_launch_id)
            key = f'OperationsManager.delete_production_order_{parent_launch.id}'
            settings.LOCKS.acquire(key)
            # print(model_to_dict(parent_launch))

            operations_order_prod = Operations_view.objects.filter(opertype=settings.OPERS_TYPES_STACK.PRODUCTION_TASK, launch=parent_launch)
            with managed_progress(
                    id=f'delete_order_by_prod_launch_{parent_launch.id}_{user.id}',
                    qty=operations_order_prod.count(),
                    user=user,
                    message=f'<h3>Удаление заданий на производство, Запуск № {parent_launch.code} от {DateToStr(parent_launch.date)}</h3>',
                    title='Выполнено',
                    props=TurnBitOn(0, 0)
            ) as progress:
                def except_func():
                    settings.LOCKS.release(key)

                progress.except_func = except_func

                with transaction.atomic():
                    logger.debug(f'Операции заданий на производство: {operations_order_prod.count()}')
                    for operation_order_prod in operations_order_prod:
                        # Операции сумм разбивки по запускам/ заказам на продажу
                        logger.debug(f'operation_order_prod: {operation_order_prod}')
                        operation_sums = Operations_view.objects.filter(parent_id=operation_order_prod.id, opertype=settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_SUM_TASK)
                        logger.debug(f'Операции сумм разбивки по запускам/ заказам на продажу: {operation_sums.count()}')
                        for production_sums in operation_sums:
                            qr = Operation_refs.objects.filter(parent_id=operation_order_prod.id, child_id=production_sums.id)
                            logger.debug(f'for delete: {qr.count()}')
                            deleted, _ = qr.delete()

                            qr = Operations.objects.filter(id=production_sums.id)
                            logger.debug(f'for delete: {qr.count()}')
                            deleted, _ = qr.delete()

                        # Техннологические операции
                        operations_det = Production_order_opers.objects.filter(
                            parent_id=operation_order_prod.id,
                            opertype=settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_OPERS_TASK). \
                            order_by('-production_operation_num')

                        logger.debug(f'Техннологические операции: {operations_det.count()}')
                        for operation_det in operations_det:
                            # Выполнение по этим технологическим операциям
                            maked_values = Operations_view.objects.filter(parent_id=operation_det.id, opertype=settings.OPERS_TYPES_STACK.MADE_OPERATIONS_TASK)
                            logger.debug(f'Выполнение по ({operation_det.production_operation_num}) : {maked_values.count()}')
                            ids = [operation.id for operation in maked_values]
                            if len(ids) > 0:
                                Production_order_valuesManager.delete_sums(ids=ids)

                            qr = Operation_refs.objects.filter(parent_id=operation_order_prod.id, child_id=operation_det.id)
                            logger.debug(f'for delete: {qr.count()}')
                            deleted, _ = qr.delete()

                            qr = Operation_refs.objects.filter(parent__isnull=True, child_id=operation_det.id)
                            logger.debug(f'for delete: {qr.count()}')
                            deleted, _ = qr.delete()

                            qr = Operations.objects.filter(id=operation_det.id)
                            logger.debug(f'for delete: {qr.count()}')
                            deleted, _ = qr.delete()

                        operation_executor_cnt = Operation_executor.objects.filter(operation_id=operation_order_prod.id, props=Operation_executor.props.relevant).count()
                        logger.debug(f'Техннологические operation_executor_cnt: {operation_executor_cnt}')

                        if operation_executor_cnt > 0:
                            user = Operation_executor.objects.filter(operation_id=operation_order_prod.id, props=Operation_executor.props.relevant)[0].executor

                            operation_item = Operation_item.objects.get(operation_id=operation_order_prod.id)
                            operation_resources = Operation_resources.objects.filter(operation_id=operation_order_prod.id).order_by('id')[0]

                            message = blinkString(
                                f'Удаление задания на производство № {operation_order_prod.num} '
                                f'от {DateTimeToStr(operation_order_prod.date, hours=3)}<p/>'
                                f'{operation_item.item.item_name}<p/>'
                                f'{operation_resources.resource.location.full_name}', bold=True, blink=False)

                            operation_executor_stack.push(
                                Operation_executor_message(
                                    executor=user,
                                    message=message
                                ),
                                logger
                            )

                        qr = Operation_refs.objects.filter(parent__isnull=True, child_id=operation_order_prod.id)
                        logger.debug(f'for delete: {qr.count()}')
                        deleted, _ = qr.delete()

                        qr = Operation_refs.objects.filter(parent__opertype=settings.OPERS_TYPES_STACK.ROUTING_TASK, child_id=operation_order_prod.id)
                        logger.debug(f'for delete: {qr.count()}')
                        deleted, _ = qr.delete()

                        qr = Operation_refs.objects.filter(parent_id=operation_order_prod.id, child__opertype=settings.OPERS_TYPES_STACK.LAUNCH_TASK)
                        logger.debug(f'for delete: {qr.count()}')
                        deleted, _ = qr.delete()

                        qr = Operations.objects.filter(id=operation_order_prod.id)
                        logger.debug(f'for delete: {qr.count()}')
                        qr.delete()

                        if progress.step() != 0:
                            WebSocket.full_refresh_grid(grid_id=settings.GRID_CONSTANTS.refresh_production_launch_grid)
                            settings.LOCKS.release(key)
                            raise ProgressDroped(progress_deleted)

                    for launch in Launches.objects.filter(parent=parent_launch):
                        # print(model_to_dict(launch))
                        launch.status = settings.PROD_OPERS_STACK.ROUTMADE
                        launch.save()

                        WebSocket.row_refresh_grid(
                            grid_id=settings.GRID_CONSTANTS.refresh_production_launch_grid_row,
                            records=LaunchesManager.getRecord(Launches_view.objects.get(id=launch.id))
                        )

                    idx += 1
                    if idx == launch_cnt:
                        parent_launch.status = settings.PROD_OPERS_STACK.ROUTMADE
                        parent_launch.save()

                        WebSocket.row_refresh_grid(
                            grid_id=settings.GRID_CONSTANTS.refresh_production_launch_grid_row,
                            records=LaunchesManager.getRecord(Launches_view.objects.get(id=parent_launch.id))
                        )
                        # progress.setContentsLabel('Обновление предстваления planing_production_order_mview')

                for operation_executor in operation_executor_stack.stack:
                    settings.EVENT_STACK.EVENTS_PRODUCTION_ORDER_CREATE.send_message(
                        message=blinkString(f'<h4>Удалиено: {operation_executor.messages.size()} заданий на производство.</h4>', bold=True),
                        users_array=[operation_executor.executor],
                        progress=progress,
                    )

            WebSocket.full_refresh_grid(grid_id=settings.GRID_CONSTANTS.refresh_production_order_grid)
            settings.LOCKS.release(key)

    def get_production_order_tmp_table(self, id, tmp_table_name=None):
        from isc_common.common.mat_views import create_tmp_table
        import uuid

        if tmp_table_name == None:
            tmp_table_name = f'''tmp_{str(uuid.uuid4()).upper().replace('-', '_')}'''

        create_tmp_table(
            on_commit=None,
            drop=False,
            sql_str=f'''SELECT distinct t.*
                                       FROM planing_operations po
                                                join planing_operation_item poi on po.id = poi.operation_id
                                                join planing_operation_item_add paoi on poi.item_id = paoi.item_id
                                                CROSS JOIN LATERAL
                                           json_to_recordset(paoi.item_full_name_obj::json) as t(
                                                                                                "confirmed" text,
                                                                                                "deliting" boolean,
                                                                                                "document__file_document" text,
                                                                                                "document_id" bigint,
                                                                                                "editing" boolean,
                                                                                                "id" bigint,
                                                                                                "isFolder" boolean,
                                                                                                "lastmodified" text,
                                                                                                "parent_id" bigint,
                                                                                                "props" bigint,
                                                                                                "qty_operations" int4,
                                                                                                "refs_id" bigint,
                                                                                                "refs_props" bigint,
                                                                                                "relevant" text,
                                                                                                "section" text,
                                                                                                "STMP_1_id" bigint,
                                                                                                "STMP_2_id" bigint,
                                                                                                "version" int4,
                                                                                                "where_from" text
                                           )
                                       where po.id = %s''',
            params=[id],
            table_name=tmp_table_name)
        return tmp_table_name

    def _create_tech_specification(self, data, user):
        from django.conf import settings
        from kaf_pas.planing.models.operation_operation import Operation_operation
        from kaf_pas.production.models.operation_def_material import Operation_def_material
        from kaf_pas.production.models.operation_material import Operation_material
        from kaf_pas.production.models.operation_resources import Operation_resources
        from kaf_pas.production.models.operations_item import Operations_item
        from kaf_pas.production.models.resource import Resource

        operations_item = Operations_item.objects.create(
            description=data.description,
            ed_izm_id=data.parentRecord.get('edizm_id'),
            item_id=data.parentRecord.get('item_id'),
            num=data.production_operation_num,
            old_num=data.production_operation_num,
            operation_id=data.production_operation_id,
            qty=data.production_operation_qty,
        )

        Operation_resources.objects.create(
            operationitem=operations_item,
            resource_id=data.resource_id,
            location_id=Resource.objects.get(id=data.resource_id).location.id if data.resource_id else data.location_id,
            location_fin_id=data.location_fin_id,
            batch_size=1
        )
        operations_item.resource = Resource.objects.get(id=data.resource_id) if data.resource_id else None
        operations_item.location_fin_id = data.location_fin_id

        for operation_def_material in Operation_def_material.objects.filter(operation_id=data.production_operation_id):
            Operation_material.objects.create(
                operationitem=operations_item,
                material=operation_def_material.material,
                material_askon=operation_def_material.material_askon,
                edizm=operation_def_material.edizm,
                qty=operation_def_material.qty
            )

        operations_item.operation_materials = Stack([operation_material for operation_material in Operation_material.objects.filter(operationitem=operations_item)])

        return self.rec_operation(
            launch=data.parentRecord.get('launch_id'),
            status=settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_OPERS_TASK_STATUSES.get('new'),
            operations_item=operations_item,
            item=data.parentRecord.get('item_id'),
            operation=data.parentRecord.get('id'),
            opertype=settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_OPERS_TASK,
            user=user,
            props=Operation_operation.props.direct_created
        )

    def _update_tech_specification(self, data, old_data, tmp_table_name):
        from isc_common.number import StrToNumber
        from kaf_pas.ckk.models.item_line import Item_line
        from kaf_pas.ckk.models.item_operations_view import Item_operations_view
        from kaf_pas.ckk.models.item_refs import Item_refs
        from kaf_pas.planing.models.operations_view import Operations_view
        from kaf_pas.production.models.operation_resources import Operation_resources
        from kaf_pas.production.models.operations_item import Operations_item

        # Изменяем параметры операции
        from kaf_pas.planing.models.operations import Operations
        operation = Operations.objects.get(id=data.id)

        # Опреция задания на производство
        parent_operation = Operations_view.objects.filter(id=data.parent_id)[0]

        # Мягкое удаление
        # operation.deleted_at = timezone.now()
        edited = False

        production_operation = kaf_pas.production.models.operations.Operations.objects.get(id=data.production_operation_id)

        operations_query = Operations_item.objects.filter(
            item=parent_operation.item,
            operation=production_operation
        )

        if operations_query.count() > 1:
            raise Exception(f'Для {parent_operation.item.item_name} существеет две одинаковых операции: {production_operation.full_name}')

        for operations_item in operations_query:
            logger.debug(f'==================================')
            logger.debug(f'\noperations_item: {operations_item}\n')

        operations_item = operations_query[0]
        # Нумерация в составе списка операций
        if data.production_operation_num != old_data.production_operation_num:
            aa = [a for a in Operations_item.objects.filter(item=parent_operation.item).order_by('num', '-lastmodified') if a.num == old_data.production_operation_num]
            if len(aa) > 0:
                aa = aa[0]
                bb = [a for a in Operations_item.objects.filter(item=parent_operation.item).order_by('num', '-lastmodified') if a.num != old_data.production_operation_num]
                bb.insert(data.production_operation_num - 1, aa)
                num = 1
                for _bb in bb:
                    _bb.old_num = _bb.num
                    _bb.num = num
                    _bb.save()
                    num += 1

                edited = True
                operations_item = bb[data.production_operation_num - 1]

            # Длительность операции
            if data.production_operation_qty != old_data.production_operation_qty:
                operations_item.qty = data.production_operation_qty
                edited = True

            # Еденица измерения длительности операции
            if data.production_operation_edizm_id != old_data.production_operation_edizm_id:
                operations_item.edizm_id = data.production_operation_edizm_id
                edited = True

            # Кол-во на еденицу продукции
            if data.value1_sum != old_data.value1_sum:
                for item_operations in Item_operations_view.objects.raw(raw_query=f'select * from {tmp_table_name} where id = %s', params=[parent_operation.item.id]):
                    item_refs = Item_refs.objects.get(id=item_operations.refs_id)
                    for item_line in Item_line.objects.filter(parent=item_refs.parent, child=item_refs.child):
                        item_line.SPC_CLM_COUNT.value_str = data.value1_sum
                        item_line.SPC_CLM_COUNT.value_int = StrToNumber(data.value1_sum)
                        item_line.save()
                        edited = True

            # Ед. изм. Кол-ва на еденицу продукции
            if data.edizm_id != old_data.edizm_id:
                for item_operations in Item_operations_view.objects.raw(raw_query=f'select * from {tmp_table_name} where id = %s', params=[parent_operation.item.id]):
                    item_refs = Item_refs.objects.get(id=item_operations.refs_id)
                    for item_line in Item_line.objects.filter(parent=item_refs.parent, child=item_refs.child):
                        item_line.edizm_id = data.edizm_id
                        item_line.save()
                        edited = True

            if edited:
                operations_item.save()

            edited_resource = False
            for operation_resources in Operation_resources.objects.filter(operationitem=operations_item):
                # Ресурс на котором выполняется данная операция
                if data.resource_id != old_data.resource_id:
                    operation_resources.resource_id = data.resource_id
                    edited_resource = True

                # Место выполнения данная операции
                if data.location_id != old_data.location_id:
                    operation_resources.location_id = data.location_id
                    edited_resource = True

                # Место окончания выполнения данной операции
                if data.location_fin_id != old_data.location_fin_id:
                    operation_resources.location_fin_id = data.location_fin_id
                    edited_resource = True

                if edited_resource:
                    operation_resources.save()

                if not edited:
                    edited = edited_resource

            if data.description != old_data.description:
                operation.description = data.description
                operation.save()

    def _update_prod_specifications_mat_res(self, launch_operations_item, operation_item):
        from kaf_pas.production.models.operation_resources import Operation_resources
        from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources
        from kaf_pas.production.models.launch_operation_material import Launch_operations_material
        from kaf_pas.production.models.operation_material import Operation_material
        # Изменяем ресурсы согласно технологической спецификации
        for operation_resource in Operation_resources.objects.filter(operationitem=operation_item):
            for launch_operation_resources in Launch_operation_resources.objects.filter(operation_resources=operation_resource, launch_operationitem=launch_operations_item):
                launch_operation_resources.resource = operation_resource.resource
                launch_operation_resources.location = operation_resource.location
                launch_operation_resources.location_fin = operation_resource.location_fin
                launch_operation_resources.batch_size = operation_resource.batch_size
                launch_operation_resources.save()

        # Изменяем материалы согласно технологической спецификации
        for operation_material in Operation_material.objects.filter(operationitem=operation_item):
            for launch_operation_material in Launch_operations_material.objects.filter(operation_material=operation_material, launch_operationitem=launch_operations_item):
                launch_operation_material.edizm = operation_material.edizm
                launch_operation_material.material = operation_material.material
                launch_operation_material.material_askon = operation_material.material_askon
                launch_operation_material.qty = operation_material.qty
                launch_operation_material.save()

    def _update_prod_specifications(self, data) -> Stack:
        from kaf_pas.planing.models.operations_view import Operations_view
        from kaf_pas.production.models.launch_operations_item import Launch_operations_item
        from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources
        from kaf_pas.production.models.operations_item import Operations_item
        from kaf_pas.production.models.launch_operation_material import Launch_operations_material
        from kaf_pas.production.models.operation_material import Operation_material
        from kaf_pas.production.models.launches import Launches
        from django.conf import settings

        parent_operation = Operations_view.objects.filter(id=data.parent_id)[0]
        if parent_operation.launch.parent != None:
            launches = list(parent_operation.launch)
        else:
            launches = list(Launches.objects.filter(parent=parent_operation.launch))

        # Удаляем операции не входящие в технологическую спецификацию
        launch_operations_items = Stack()
        exists_in_tech = list(Launch_operations_item.objects. \
                              filter(launch__in=launches). \
                              filter(operationitem__in=list(Operations_item.objects.filter(item=parent_operation.item))). \
                              filter(deleted_at__isnull=True). \
                              exclude(launch__status=settings.PROD_OPERS_STACK.CLOSED))

        for launch_operations_item in Launch_operations_item.objects. \
                filter(launch__in=launches). \
                filter(item=parent_operation.item). \
                filter(deleted_at__isnull=True). \
                exclude(id__in=[l.id for l in exists_in_tech]). \
                exclude(launch__status=settings.PROD_OPERS_STACK.CLOSED):
            Launch_operation_resources.objects.filter(launch_operationitem=launch_operations_item).soft_delete()
            Launch_operations_material.objects.filter(launch_operationitem=launch_operations_item).soft_delete()
            launch_operations_item.soft_delete()
            launch_operations_items.push(launch_operations_item)

        # Изменяем операции согласно изменения технологической спецификации
        for operation_item in Operations_item.objects.filter(item=parent_operation.item):
            for launch_operations_item in Launch_operations_item.objects. \
                    filter(operationitem=operation_item). \
                    exclude(launch__status=settings.PROD_OPERS_STACK.CLOSED):
                # launch_operations_item.description = 'Обновлено'
                launch_operations_item.ed_izm = operation_item.ed_izm
                launch_operations_item.num = operation_item.num
                launch_operations_item.old_num = operation_item.old_num
                launch_operations_item.qty = operation_item.qty
                launch_operations_item.props |= launch_operations_item.props.updated
                launch_operations_item.save()
                logger.debug(f'\nlaunch_operations_item: {launch_operations_item}\n')
                launch_operations_items.push(launch_operations_item)

                # Изменяем ресурсы согласно технологической спецификации
                self._update_prod_specifications_mat_res(launch_operations_item=launch_operations_item, operation_item=operation_item)

                # Получаем материалы вошедшие в технологическую спецификацию
                material_exists_in_tech = list(Launch_operations_material.objects.filter(operation_material__in=list(Operation_material.objects.filter(operationitem=operation_item))))

                # Удаляем материалы не вошедшие технологическую спецификацию
                Launch_operations_material.objects. \
                    exclude(id__in=[m.id for m in material_exists_in_tech]). \
                    filter(launch_operationitem=launch_operations_item). \
                    filter(deleted_at__isnull=True). \
                    soft_delete()

        return launch_operations_items

    def _update_routing(self, data, old_data, user: User, updated_launch_operations_items: Stack):
        from kaf_pas.planing.models.operations_view import Operations_view

        parent_operation = Operations_view.objects.filter(id=data.parent_id)[0]

        record = dict(data=[parent_operation.launch.id], user=user)
        res = self.routing_ext.update_routing(data=data, old_data=old_data, updated_launch_operations_items=updated_launch_operations_items)
        return res

    def _update_production_orders(self, data):
        from kaf_pas.planing.models.operation_operation import Operation_operation
        from kaf_pas.planing.models.operation_value import Operation_value
        from kaf_pas.planing.models.operation_resources import Operation_resources
        from kaf_pas.planing.models.operation_refs import Operation_refs

        for operation_resources in Operation_resources.objects.filter(operation_id=data.id):
            logger.debug(f'operation_resources: {operation_resources}')
            operation_resources.location_fin_id = data.location_fin_id
            operation_resources.resource_id = data.resource_id
            operation_resources.save()

        for operation_operation in Operation_operation.objects.filter(operation_id=data.id):
            logger.debug(f'operation_operation: {operation_operation}')
            operation_operation.production_operation_id = data.production_operation_id
            operation_operation.ed_izm_id = data.production_operation_edizm_id
            operation_operation.num = data.production_operation_num
            operation_operation.production_operation_id = data.production_operation_id
            operation_operation.qty = data.production_operation_qty
            operation_operation.props |= Operation_operation.props.updated
            operation_operation.save()

        for operation_refs in Operation_refs.objects.filter(parent_id=data.parent_id, child__opertype__code='DETAIL_SUM_PRD_TSK'):
            for operation_value in Operation_value.objects.filter(operation=operation_refs.child):
                logger.debug(f'\noperation_value: {operation_value}')
                operation_value.edizm_id = data.edizm_id
                operation_value.save()

        return data

    def update_operation(self, data, user, old_data=None):
        from django.db import transaction

        with transaction.atomic():
            if old_data == None:
                data.parent_id = data.parentRecord.get('id')
                data.id = self._create_tech_specification(data=data, user=user)
                old_data = data

            tmp_table_name = self.get_production_order_tmp_table(id=data.parent_id)

            # Меняем строку операции в технологической спецификации
            self._update_tech_specification(data=data, old_data=old_data, tmp_table_name=tmp_table_name)

            # Меняем строки операций в производственных спецификациях, которые относятся к запуску из dataБ получаем список измененных строк
            updated_launch_operations_items = self._update_prod_specifications(data=data)
            for updated_launch_operations_item in updated_launch_operations_items:
                logger.debug(f'=======================================')
                logger.debug(f'\nupdated_launch_operations_item: {updated_launch_operations_item}')

            if updated_launch_operations_items.size():
                self._update_routing(data=data, old_data=old_data, updated_launch_operations_items=updated_launch_operations_items, user=user)
                self._update_production_orders(data=data)
            raise NotImplement()

        return data
