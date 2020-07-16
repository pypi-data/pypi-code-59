import asyncio
import sys

try:
    import pop.hub

    HAS_POP = True
except ImportError:
    HAS_POP = False

__virtualname__ = "idem"
__func_alias__ = {"exec_": "exec"}


def __virtual__():
    if not HAS_POP:
        return False, "pop is not installed"
    if sys.version_info < (3, 6):
        return False, "idem only works on python3.6 and later"


def __init__(opts):
    if not ["idem.hub"] in __context__:
        # Initialize the hub
        hub = pop.hub.Hub()
        hub.pop.loop.create()
        # Load idem grains/states/exec modules onto the hub
        hub.pop.sub.add(dyne_name="acct")
        hub.pop.sub.add(dyne_name="config")
        hub.pop.sub.add(dyne_name="exec")
        hub.pop.sub.add(dyne_name="grains")
        hub.pop.sub.add(dyne_name="states")
        # Read the grains/idem config options
        hub.config.integrate.load(
            ["acct", "idem", "grains"], "idem", parse_cli=False, logs=False
        )

        # TODO Should grainsv2 be collected?
        # hub.grains.init.standalone()

        __context__["idem.hub"] = hub


def exec_(
        path: str,
        acct_file: str = None,
        acct_key: str = None,
        acct_profile: str = "default",
        *args,
        **kwargs,
):
    """
    A function to call execution modules from idem

    :maintainer:    Tyler Johnson <tjohnson@saltstack.com>
    :maturity:      new
    :depends:       acct, pop, pop-config, idem
    :platform:      all

    CLI Example::

        salt '*' idem.exec test.ping
    """
    hub: pop.Hub = __context__["idem.hub"]
    coro = hub.idem.ex.run(
        path,
        args,
        kwargs,
        acct_file=acct_file,
        acct_key=acct_key,
        acct_profile=acct_profile,
    )
    task = asyncio.wait_for(coro, loop=hub.pop.Loop, timeout=-1)
    return task.result()
