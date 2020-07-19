class MockSession(object):
    def __init__(self):
        self.rollback_called = False
        self.commit_called = False
        self.delete_called = False
        self.add_called = False
        self.objects = []
        self.deleted_objects = []

    def rollback(self):
        self.rollback_called = True

    def commit(self):
        self.commit_called = True

    def add(self, obj):
        self.objects.append(obj)
        self.add_called = True

    def delete(self, obj):
        self.delete_called = True
        self.deleted_objects.append(obj)
