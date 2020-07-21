from pluggy import HookspecMarker

hookspec = HookspecMarker("pytest")


@hookspec(historic=True)
def pytest_configure(config: "Config") -> None:
    
