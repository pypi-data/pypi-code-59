""" basic collect and runtest protocol implementations """
import bdb
import os
import sys
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Generic
from typing import List
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import Union

import attr

from .reports import BaseReport
from .reports import CollectErrorRepr
from .reports import CollectReport
from .reports import TestReport
from _pytest import timing
from _pytest._code.code import ExceptionChainRepr
from _pytest._code.code import ExceptionInfo
from _pytest.compat import TYPE_CHECKING
from _pytest.config.argparsing import Parser
from _pytest.nodes import Collector
from _pytest.nodes import Item
from _pytest.nodes import Node
from _pytest.outcomes import Exit
from _pytest.outcomes import Skipped
from _pytest.outcomes import TEST_OUTCOME

if TYPE_CHECKING:
    from typing import Type
    from typing_extensions import Literal

    from _pytest.main import Session
    from _pytest.terminal import TerminalReporter

#
# pytest plugin hooks


def pytest_addoption(parser: Parser) -> None:
    group = parser.getgroup("terminal reporting", "reporting", after="general")
    group.addoption(
        "--durations",
        action="store",
        type=int,
        default=None,
        metavar="N",
        help="show N slowest setup/test durations (N=0 for all).",
    )


def pytest_terminal_summary(terminalreporter: "TerminalReporter") -> None:
    durations = terminalreporter.config.option.durations
    verbose = terminalreporter.config.getvalue("verbose")
    if durations is None:
        return
    tr = terminalreporter
    dlist = []
    for replist in tr.stats.values():
        for rep in replist:
            if hasattr(rep, "duration"):
                dlist.append(rep)
    if not dlist:
        return
    dlist.sort(key=lambda x: x.duration)
    dlist.reverse()
    if not durations:
        tr.write_sep("=", "slowest durations")
    else:
        tr.write_sep("=", "slowest %s durations" % durations)
        dlist = dlist[:durations]

    for i, rep in enumerate(dlist):
        if verbose < 2 and rep.duration < 0.005:
            tr.write_line("")
            tr.write_line(
                "(%s durations < 0.005s hidden.  Use -vv to show these durations.)"
                % (len(dlist) - i)
            )
            break
        tr.write_line("{:02.2f}s {:<8} {}".format(rep.duration, rep.when, rep.nodeid))


def pytest_sessionstart(session: "Session") -> None:
    session._setupstate = SetupState()


def pytest_sessionfinish(session: "Session") -> None:
    session._setupstate.teardown_all()


def pytest_runtest_protocol(item: Item, nextitem: Optional[Item]) -> bool:
    ihook = item.ihook
    ihook.pytest_runtest_logstart(nodeid=item.nodeid, location=item.location)
    runtestprotocol(item, nextitem=nextitem)
    ihook.pytest_runtest_logfinish(nodeid=item.nodeid, location=item.location)
    return True


def runtestprotocol(
    item: Item, log: bool = True, nextitem: Optional[Item] = None
) -> List[TestReport]:
    hasrequest = hasattr(item, "_request")
    if hasrequest and not item._request:  # type: ignore[attr-defined] # noqa: F821
        item._initrequest()  # type: ignore[attr-defined] # noqa: F821
    rep = call_and_report(item, "setup", log)
    reports = [rep]
    if rep.passed:
        if item.config.getoption("setupshow", False):
            show_test_item(item)
        if not item.config.getoption("setuponly", False):
            reports.append(call_and_report(item, "call", log))
    reports.append(call_and_report(item, "teardown", log, nextitem=nextitem))
    # after all teardown hooks have been called
    # want funcargs and request info to go away
    if hasrequest:
        item._request = False  # type: ignore[attr-defined] # noqa: F821
        item.funcargs = None  # type: ignore[attr-defined] # noqa: F821
    return reports


def show_test_item(item: Item) -> None:
    """Show test function, parameters and the fixtures of the test item."""
    tw = item.config.get_terminal_writer()
    tw.line()
    tw.write(" " * 8)
    tw.write(item.nodeid)
    used_fixtures = sorted(getattr(item, "fixturenames", []))
    if used_fixtures:
        tw.write(" (fixtures used: {})".format(", ".join(used_fixtures)))
    tw.flush()


def pytest_runtest_setup(item: Item) -> None:
    _update_current_test_var(item, "setup")
    item.session._setupstate.prepare(item)


def pytest_runtest_call(item: Item) -> None:
    _update_current_test_var(item, "call")
    try:
        del sys.last_type
        del sys.last_value
        del sys.last_traceback
    except AttributeError:
        pass
    try:
        item.runtest()
    except Exception as e:
        # Store trace info to allow postmortem debugging
        sys.last_type = type(e)
        sys.last_value = e
        assert e.__traceback__ is not None
        # Skip *this* frame
        sys.last_traceback = e.__traceback__.tb_next
        raise e


def pytest_runtest_teardown(item: Item, nextitem: Optional[Item]) -> None:
    _update_current_test_var(item, "teardown")
    item.session._setupstate.teardown_exact(item, nextitem)
    _update_current_test_var(item, None)


def _update_current_test_var(
    item: Item, when: Optional["Literal['setup', 'call', 'teardown']"]
) -> None:
    """
    Update :envvar:`PYTEST_CURRENT_TEST` to reflect the current item and stage.

    If ``when`` is None, delete ``PYTEST_CURRENT_TEST`` from the environment.
    """
    var_name = "PYTEST_CURRENT_TEST"
    if when:
        value = "{} ({})".format(item.nodeid, when)
        # don't allow null bytes on environment variables (see #2644, #2957)
        value = value.replace("\x00", "(null)")
        os.environ[var_name] = value
    else:
        os.environ.pop(var_name)


def pytest_report_teststatus(report: BaseReport) -> Optional[Tuple[str, str, str]]:
    if report.when in ("setup", "teardown"):
        if report.failed:
            #      category, shortletter, verbose-word
            return "error", "E", "ERROR"
        elif report.skipped:
            return "skipped", "s", "SKIPPED"
        else:
            return "", "", ""
    return None


#
# Implementation


def call_and_report(
    item: Item, when: "Literal['setup', 'call', 'teardown']", log: bool = True, **kwds
) -> TestReport:
    call = call_runtest_hook(item, when, **kwds)
    hook = item.ihook
    report = hook.pytest_runtest_makereport(item=item, call=call)  # type: TestReport
    if log:
        hook.pytest_runtest_logreport(report=report)
    if check_interactive_exception(call, report):
        hook.pytest_exception_interact(node=item, call=call, report=report)
    return report


def check_interactive_exception(call: "CallInfo", report: BaseReport) -> bool:
    return call.excinfo is not None and not (
        hasattr(report, "wasxfail")
        or call.excinfo.errisinstance(Skipped)
        or call.excinfo.errisinstance(bdb.BdbQuit)
    )


def call_runtest_hook(
    item: Item, when: "Literal['setup', 'call', 'teardown']", **kwds
) -> "CallInfo[None]":
    if when == "setup":
        ihook = item.ihook.pytest_runtest_setup  # type: Callable[..., None]
    elif when == "call":
        ihook = item.ihook.pytest_runtest_call
    elif when == "teardown":
        ihook = item.ihook.pytest_runtest_teardown
    else:
        assert False, "Unhandled runtest hook case: {}".format(when)
    reraise = (Exit,)  # type: Tuple[Type[BaseException], ...]
    if not item.config.getoption("usepdb", False):
        reraise += (KeyboardInterrupt,)
    return CallInfo.from_call(
        lambda: ihook(item=item, **kwds), when=when, reraise=reraise
    )


_T = TypeVar("_T")


@attr.s(repr=False)
class CallInfo(Generic[_T]):
    """ Result/Exception info a function invocation.

    :param T result: The return value of the call, if it didn't raise. Can only be accessed
        if excinfo is None.
    :param Optional[ExceptionInfo] excinfo: The captured exception of the call, if it raised.
    :param float start: The system time when the call started, in seconds since the epoch.
    :param float stop: The system time when the call ended, in seconds since the epoch.
    :param float duration: The call duration, in seconds.
    :param str when: The context of invocation: "setup", "call", "teardown", ...
    """

    _result = attr.ib(type="Optional[_T]")
    excinfo = attr.ib(type=Optional[ExceptionInfo[BaseException]])
    start = attr.ib(type=float)
    stop = attr.ib(type=float)
    duration = attr.ib(type=float)
    when = attr.ib(type="Literal['collect', 'setup', 'call', 'teardown']")

    @property
    def result(self) -> _T:
        if self.excinfo is not None:
            raise AttributeError("{!r} has no valid result".format(self))
        # The cast is safe because an exception wasn't raised, hence
        # _result has the expected function return type (which may be
        #  None, that's why a cast and not an assert).
        return cast(_T, self._result)

    @classmethod
    def from_call(
        cls,
        func: "Callable[[], _T]",
        when: "Literal['collect', 'setup', 'call', 'teardown']",
        reraise: "Optional[Union[Type[BaseException], Tuple[Type[BaseException], ...]]]" = None,
    ) -> "CallInfo[_T]":
        excinfo = None
        start = timing.time()
        precise_start = timing.perf_counter()
        try:
            result = func()  # type: Optional[_T]
        except BaseException:
            excinfo = ExceptionInfo.from_current()
            if reraise is not None and excinfo.errisinstance(reraise):
                raise
            result = None
        # use the perf counter
        precise_stop = timing.perf_counter()
        duration = precise_stop - precise_start
        stop = timing.time()
        return cls(
            start=start,
            stop=stop,
            duration=duration,
            when=when,
            result=result,
            excinfo=excinfo,
        )

    def __repr__(self) -> str:
        if self.excinfo is None:
            return "<CallInfo when={!r} result: {!r}>".format(self.when, self._result)
        return "<CallInfo when={!r} excinfo={!r}>".format(self.when, self.excinfo)


def pytest_runtest_makereport(item: Item, call: CallInfo[None]) -> TestReport:
    return TestReport.from_item_and_call(item, call)


def pytest_make_collect_report(collector: Collector) -> CollectReport:
    call = CallInfo.from_call(lambda: list(collector.collect()), "collect")
    # TODO: Better typing for longrepr.
    longrepr = None  # type: Optional[Any]
    if not call.excinfo:
        outcome = "passed"  # type: Literal["passed", "skipped", "failed"]
    else:
        skip_exceptions = [Skipped]
        unittest = sys.modules.get("unittest")
        if unittest is not None:
            # Type ignored because unittest is loaded dynamically.
            skip_exceptions.append(unittest.SkipTest)  # type: ignore
        if call.excinfo.errisinstance(tuple(skip_exceptions)):
            outcome = "skipped"
            r_ = collector._repr_failure_py(call.excinfo, "line")
            assert isinstance(r_, ExceptionChainRepr), repr(r_)
            r = r_.reprcrash
            assert r
            longrepr = (str(r.path), r.lineno, r.message)
        else:
            outcome = "failed"
            errorinfo = collector.repr_failure(call.excinfo)
            if not hasattr(errorinfo, "toterminal"):
                errorinfo = CollectErrorRepr(errorinfo)
            longrepr = errorinfo
    result = call.result if not call.excinfo else None
    rep = CollectReport(collector.nodeid, outcome, longrepr, result)
    rep.call = call  # type: ignore # see collect_one_node
    return rep


class SetupState:
    """ shared state for setting up/tearing down test items or collectors. """

    def __init__(self):
        self.stack = []  # type: List[Node]
        self._finalizers = {}  # type: Dict[Node, List[Callable[[], object]]]

    def addfinalizer(self, finalizer: Callable[[], object], colitem) -> None:
        """ attach a finalizer to the given colitem. """
        assert colitem and not isinstance(colitem, tuple)
        assert callable(finalizer)
        # assert colitem in self.stack  # some unit tests don't setup stack :/
        self._finalizers.setdefault(colitem, []).append(finalizer)

    def _pop_and_teardown(self):
        colitem = self.stack.pop()
        self._teardown_with_finalization(colitem)

    def _callfinalizers(self, colitem) -> None:
        finalizers = self._finalizers.pop(colitem, None)
        exc = None
        while finalizers:
            fin = finalizers.pop()
            try:
                fin()
            except TEST_OUTCOME as e:
                # XXX Only first exception will be seen by user,
                #     ideally all should be reported.
                if exc is None:
                    exc = e
        if exc:
            raise exc

    def _teardown_with_finalization(self, colitem) -> None:
        self._callfinalizers(colitem)
        colitem.teardown()
        for colitem in self._finalizers:
            assert colitem in self.stack

    def teardown_all(self) -> None:
        while self.stack:
            self._pop_and_teardown()
        for key in list(self._finalizers):
            self._teardown_with_finalization(key)
        assert not self._finalizers

    def teardown_exact(self, item, nextitem) -> None:
        needed_collectors = nextitem and nextitem.listchain() or []
        self._teardown_towards(needed_collectors)

    def _teardown_towards(self, needed_collectors) -> None:
        exc = None
        while self.stack:
            if self.stack == needed_collectors[: len(self.stack)]:
                break
            try:
                self._pop_and_teardown()
            except TEST_OUTCOME as e:
                # XXX Only first exception will be seen by user,
                #     ideally all should be reported.
                if exc is None:
                    exc = e
        if exc:
            raise exc

    def prepare(self, colitem) -> None:
        """Setup objects along the collector chain to the test-method."""

        # check if the last collection node has raised an error
        for col in self.stack:
            if hasattr(col, "_prepare_exc"):
                exc = col._prepare_exc  # type: ignore[attr-defined] # noqa: F821
                raise exc

        needed_collectors = colitem.listchain()
        for col in needed_collectors[len(self.stack) :]:
            self.stack.append(col)
            try:
                col.setup()
            except TEST_OUTCOME as e:
                col._prepare_exc = e  # type: ignore[attr-defined] # noqa: F821
                raise e


def collect_one_node(collector: Collector) -> CollectReport:
    ihook = collector.ihook
    ihook.pytest_collectstart(collector=collector)
    rep = ihook.pytest_make_collect_report(collector=collector)  # type: CollectReport
    call = rep.__dict__.pop("call", None)
    if call and check_interactive_exception(call, rep):
        ihook.pytest_exception_interact(node=collector, call=call, report=rep)
    return rep
