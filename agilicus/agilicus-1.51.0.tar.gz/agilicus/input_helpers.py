from . import context


def update_if_not_none(obj: dict, new_values: dict):
    for k, v in new_values.items():
        if v is not None:
            obj[k] = v


def pop_item_if_none(obj: dict):
    if not obj:
        return

    keys_to_pop = []
    for k, v in obj.items():
        if v is None:
            keys_to_pop.append(k)
    for k in keys_to_pop:
        obj.pop(k)


def build_updated_model(klass, model, new_values):
    model_dict = model.to_dict()
    update_if_not_none(model_dict, new_values)
    return klass(**model_dict)


def get_org_from_input_or_ctx(ctx, org_id=None, **kwargs):
    if org_id is None:
        token = context.get_token(ctx)
        org_id = context.get_org_id(ctx, token)

    # Treat an empty-string org id like None so that we can query all if necessary
    if org_id == "":
        org_id = None

    return org_id
