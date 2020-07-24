

def mod_record_cursor_id_between(mod, from_id, to_id,
                                 base_exression_list=None):
    """
    这个功能一般用户导出excel，可能要导入上w的数据，
    不使用这个的话，query_result.iterator() 第一个数据会卡住
    Args:
        from_id (int): >= from_id
        to_id (int): < to_id
        base_expression_list (list): expression_list
    """
    local_max_id = to_id
    if base_exression_list is None:
        base_exression_list = []
    while 1:
        new_query_result = mod.select().where(
            [getattr(mod, 'id') < local_max_id,
             getattr(mod, 'id') >= from_id,
             *base_exression_list]
        ).order_by(getattr(mod, 'id').desc()).paginate(0, 10)

        if new_query_result.count() == 0:
            break

        for ele in new_query_result.iterator():
            yield ele
            local_max_id = min(local_max_id, ele.id)
