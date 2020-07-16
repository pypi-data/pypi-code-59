from roboself import actions, Context


@actions.register(intent='dummy_intent')
def dummy_action(ctx: Context, dummy_object):
    """Dummy action with dummy object"""

    ctx.chat.utter("dummy_message", dummy=dummy_object)
