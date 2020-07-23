import abc

EnvironmentRegistry = []


class Environment(abc.ABC):
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__setattr__("name", cls.__name__)
        return obj

    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        if cls.__name__ not in [env.__name__ for env in EnvironmentRegistry]:
            EnvironmentRegistry.append(cls)

    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def step(self, u_in, u_out, t):
        pass
