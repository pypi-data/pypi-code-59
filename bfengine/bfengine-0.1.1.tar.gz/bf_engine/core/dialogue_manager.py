from .module import Module


class DialogueManager(Module):
    """
    对话管理
    """
    def __init__(self, app_id):
        super().__init__(app_id, 'dm')
