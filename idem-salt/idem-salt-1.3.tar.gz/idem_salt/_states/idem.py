import asyncio
import os
import sys
from typing import List

try:
    import pop.hub

    HAS_POP = True
except ImportError:
    HAS_POP = False

__virtualname__ = "idem"


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


def _get_refs(hub, sources: list[str]):
    """
    Determine where the sls sources are
    """
    sls_sources = []
    SLSs = []
    for sls in sources:
        if os.path.isfile(sls):
            if sls.endswith(".sls"):
                ref = sls[:-4]
            else:
                ref = sls
            SLSs.append(ref)
            sls_dir = os.path.dirname(sls)
            implied = f"file://{sls_dir}"
            if implied not in sls_sources:
                sls_sources.append(implied)
        else:
            SLSs.append(sls)
    if hub.OPT.idem.tree:
        tree = f"file://{hub.OPT.idem.tree}"
        if tree not in sls_sources:
            sls_sources.insert(0, tree)
    return sls_sources, SLSs


def state(
        name: str,
        sls: List[str],
        test: bool = False,
        acct_file: str = None,
        acct_key: str = None,
        acct_profile: str = None,
):
    """
    A function to call state modules from idem

    :maintainer:    Tyler Johnson <tjohnson@saltstack.com>
    :maturity:      new
    :depends:       acct, pop, pop-config, idem
    :platform:      all
    """
    hub: pop.Hub = __context__["idem.hub"]

    if isinstance(sls, str):
        sls = [sls]

    sls_sources, SLSs = _get_refs(hub, sls)
    coro = hub.idem.state.apply(
        name=name,
        sls_sources=sls_sources,
        render=hub.OPT.idem.render,
        runtime=hub.OPT.idem.runtime,
        subs=["states"],
        cache_dir=hub.OPT.idem.cache_dir,
        sls=SLSs,
        test=test,
        acct_file=acct_file or hub.OPT.acct.acct_file,
        acct_key=acct_key or hub.OPT.acct.acct_key,
        acct_profile=acct_profile or hub.OPT.acct.acct_profile,
    )
    asyncio.wait_for(coro, loop=hub.pop.Loop, timeout=-1)

    errors = hub.idem.RUNS[name]["errors"]
    running = hub.idem.RUNS[name]["running"]

    # This is the bare minimum of what salt looks for in a custom state module
    result = {
        "name": name,
        "result": bool(errors),
        "comment": errors,
        "changes": {},
    }
    # Tack on all the state runs
    result.update(running)
    return result
