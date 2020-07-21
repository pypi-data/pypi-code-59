class CpuData(object):
    user = str()
    kernel = str()

    def serialize(self):
        return {"user": self.user,
                "kernel": self.kernel}
