""" hook specifications for pytest plugins, invoked from main.py and builtin plugins.  """
from typing import Any
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

import py.path
from pluggy import HookspecMarker

from .deprecated import COLLECT_DIRECTORY_HOOK
from .deprecated import WARNING_CAPTURED_HOOK
from _pytest.compat import TYPE_CHECKING

if TYPE_CHECKING:
    import pdb
    import warnings
    from typing_extensions import Literal

    from _pytest._code.code import ExceptionRepr
    from _pytest.code import ExceptionInfo
    from _pytest.config import Config
    from _pytest.config import ExitCode
    from _pytest.config import PytestPluginManager
    from _pytest.config import _PluggyPlugin
    from _pytest.config.argparsing import Parser
    from _pytest.fixtures import FixtureDef
    from _pytest.fixtures import SubRequest
    from _pytest.main import Session
    from _pytest.nodes import Collector
    from _pytest.nodes import Item
    from _pytest.nodes import Node
    from _pytest.outcomes import Exit
    from _pytest.python import Function
    from _pytest.python import Metafunc
    from _pytest.python import Module
    from _pytest.python import PyCollector
    from _pytest.reports import CollectReport
    from _pytest.reports import TestReport
    from _pytest.runner import CallInfo
    from _pytest.terminal import TerminalReporter


hookspec = HookspecMarker("pytest")

# -------------------------------------------------------------------------
# Initialization hooks called for every plugin
# -------------------------------------------------------------------------


@hookspec(historic=True)
def pytest_addhooks(pluginmanager: "PytestPluginManager") -> None:
    """called at plugin registration time to allow adding new hooks via a call to
    ``pluginmanager.add_hookspecs(module_or_class, prefix)``.


    :param _pytest.config.PytestPluginManager pluginmanager: pytest plugin manager

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """


@hookspec(historic=True)
def pytest_plugin_registered(
    plugin: "_PluggyPlugin", manager: "PytestPluginManager"
) -> None:
    """ a new pytest plugin got registered.

    :param plugin: the plugin module or instance
    :param _pytest.config.PytestPluginManager manager: pytest plugin manager

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """


@hookspec(historic=True)
def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    """register argparse-style options and ini-style config values,
    called once at the beginning of a test run.

    .. note::

        This function should be implemented only in plugins or ``conftest.py``
        files situated at the tests root directory due to how pytest
        :ref:`discovers plugins during startup <pluginorder>`.

    :arg _pytest.config.argparsing.Parser parser: To add command line options, call
        :py:func:`parser.addoption(...) <_pytest.config.argparsing.Parser.addoption>`.
        To add ini-file values call :py:func:`parser.addini(...)
        <_pytest.config.argparsing.Parser.addini>`.

    :arg _pytest.config.PytestPluginManager pluginmanager: pytest plugin manager,
        which can be used to install :py:func:`hookspec`'s or :py:func:`hookimpl`'s
        and allow one plugin to call another plugin's hooks to change how
        command line options are added.

    Options can later be accessed through the
    :py:class:`config <_pytest.config.Config>` object, respectively:

    - :py:func:`config.getoption(name) <_pytest.config.Config.getoption>` to
      retrieve the value of a command line option.

    - :py:func:`config.getini(name) <_pytest.config.Config.getini>` to retrieve
      a value read from an ini-style file.

    The config object is passed around on many internal objects via the ``.config``
    attribute or can be retrieved as the ``pytestconfig`` fixture.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """


@hookspec(historic=True)
def pytest_configure(config: "Config") -> None:
    """
    Allows plugins and conftest files to perform initial configuration.

    This hook is called for every plugin and initial conftest file
    after command line options have been parsed.

    After that, the hook is called for other conftest files as they are
    imported.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.

    :arg _pytest.config.Config config: pytest config object
    """


# -------------------------------------------------------------------------
# Bootstrapping hooks called for plugins registered early enough:
# internal and 3rd party plugins.
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def pytest_cmdline_parse(
    pluginmanager: "PytestPluginManager", args: List[str]
) -> Optional["Config"]:
    """return initialized config object, parsing the specified args.

    Stops at first non-None result, see :ref:`firstresult`

    .. note::
        This hook will only be called for plugin classes passed to the ``plugins`` arg when using `pytest.main`_ to
        perform an in-process test run.

    :param _pytest.config.PytestPluginManager pluginmanager: pytest plugin manager
    :param list[str] args: list of arguments passed on the command line
    """


def pytest_cmdline_preparse(config: "Config", args: List[str]) -> None:
    """(**Deprecated**) modify command line arguments before option parsing.

    This hook is considered deprecated and will be removed in a future pytest version. Consider
    using :func:`pytest_load_initial_conftests` instead.

    .. note::
        This hook will not be called for ``conftest.py`` files, only for setuptools plugins.

    :param _pytest.config.Config config: pytest config object
    :param list[str] args: list of arguments passed on the command line
    """


@hookspec(firstresult=True)
def pytest_cmdline_main(config: "Config") -> Optional[Union["ExitCode", int]]:
    """ called for performing the main command line action. The default
    implementation will invoke the configure hooks and runtest_mainloop.

    .. note::
        This hook will not be called for ``conftest.py`` files, only for setuptools plugins.

    Stops at first non-None result, see :ref:`firstresult`

    :param _pytest.config.Config config: pytest config object
    """


def pytest_load_initial_conftests(
    early_config: "Config", parser: "Parser", args: List[str]
) -> None:
    """ implements the loading of initial conftest files ahead
    of command line option parsing.

    .. note::
        This hook will not be called for ``conftest.py`` files, only for setuptools plugins.

    :param _pytest.config.Config early_config: pytest config object
    :param list[str] args: list of arguments passed on the command line
    :param _pytest.config.argparsing.Parser parser: to add command line options
    """


# -------------------------------------------------------------------------
# collection hooks
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def pytest_collection(session: "Session") -> Optional[object]:
    """Perform the collection protocol for the given session.

    Stops at first non-None result, see :ref:`firstresult`.
    The return value is not used, but only stops further processing.

    The hook is meant to set `session.items` to a sequence of items at least,
    but normally should follow this procedure:

      1. Call the pytest_collectstart hook.
      2. Call the pytest_collectreport hook.
      3. Call the pytest_collection_modifyitems hook.
      4. Call the pytest_collection_finish hook.
      5. Set session.testscollected to the amount of collect items.
      6. Set `session.items` to a list of items.

    You can implement this hook to only perform some action before collection,
    for example the terminal plugin uses it to start displaying the collection
    counter (and returns `None`).

    :param _pytest.main.Session session: the pytest session object
    """


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """ called after collection has been performed, may filter or re-order
    the items in-place.

    :param _pytest.main.Session session: the pytest session object
    :param _pytest.config.Config config: pytest config object
    :param List[_pytest.nodes.Item] items: list of item objects
    """


def pytest_collection_finish(session: "Session") -> None:
    """Called after collection has been performed and modified.

    :param _pytest.main.Session session: the pytest session object
    """


@hookspec(firstresult=True)
def pytest_ignore_collect(path: py.path.local, config: "Config") -> Optional[bool]:
    """Return True to prevent considering this path for collection.

    This hook is consulted for all files and directories prior to calling
    more specific hooks.

    Stops at first non-None result, see :ref:`firstresult`.

    :param path: a :py:class:`py.path.local` - the path to analyze
    :param _pytest.config.Config config: pytest config object
    """


@hookspec(firstresult=True, warn_on_impl=COLLECT_DIRECTORY_HOOK)
def pytest_collect_directory(path: py.path.local, parent) -> Optional[object]:
    """Called before traversing a directory for collection files.

    Stops at first non-None result, see :ref:`firstresult`.

    :param path: a :py:class:`py.path.local` - the path to analyze
    """


def pytest_collect_file(path: py.path.local, parent) -> "Optional[Collector]":
    """Return collection Node or None for the given path.

    Any new node needs to have the specified ``parent`` as a parent.

    :param path: a :py:class:`py.path.local` - the path to collect
    """


# logging hooks for collection


def pytest_collectstart(collector: "Collector") -> None:
    """ collector starts collecting. """


def pytest_itemcollected(item: "Item") -> None:
    """We just collected a test item."""


def pytest_collectreport(report: "CollectReport") -> None:
    """ collector finished collecting. """


def pytest_deselected(items: Sequence["Item"]) -> None:
    """Called for deselected test items, e.g. by keyword."""


@hookspec(firstresult=True)
def pytest_make_collect_report(collector: "Collector") -> "Optional[CollectReport]":
    """ perform ``collector.collect()`` and return a CollectReport.

    Stops at first non-None result, see :ref:`firstresult` """


# -------------------------------------------------------------------------
# Python test function related hooks
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def pytest_pycollect_makemodule(path: py.path.local, parent) -> Optional["Module"]:
    """Return a Module collector or None for the given path.

    This hook will be called for each matching test module path.
    The pytest_collect_file hook needs to be used if you want to
    create test modules for files that do not match as a test module.

    Stops at first non-None result, see :ref:`firstresult`.

    :param path: a :py:class:`py.path.local` - the path of module to collect
    """


@hookspec(firstresult=True)
def pytest_pycollect_makeitem(
    collector: "PyCollector", name: str, obj: object
) -> Union[None, "Item", "Collector", List[Union["Item", "Collector"]]]:
    """Return a custom item/collector for a Python object in a module, or None.

    Stops at first non-None result, see :ref:`firstresult`.
    """


@hookspec(firstresult=True)
def pytest_pyfunc_call(pyfuncitem: "Function") -> Optional[object]:
    """ call underlying test function.

    Stops at first non-None result, see :ref:`firstresult` """


def pytest_generate_tests(metafunc: "Metafunc") -> None:
    """ generate (multiple) parametrized calls to a test function."""


@hookspec(firstresult=True)
def pytest_make_parametrize_id(
    config: "Config", val: object, argname: str
) -> Optional[str]:
    """Return a user-friendly string representation of the given ``val`` that will be used
    by @pytest.mark.parametrize calls. Return None if the hook doesn't know about ``val``.
    The parameter name is available as ``argname``, if required.

    Stops at first non-None result, see :ref:`firstresult`

    :param _pytest.config.Config config: pytest config object
    :param val: the parametrized value
    :param str argname: the automatic parameter name produced by pytest
    """


# -------------------------------------------------------------------------
# runtest related hooks
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def pytest_runtestloop(session: "Session") -> Optional[object]:
    """Performs the main runtest loop (after collection finished).

    The default hook implementation performs the runtest protocol for all items
    collected in the session (``session.items``), unless the collection failed
    or the ``collectonly`` pytest option is set.

    If at any point :py:func:`pytest.exit` is called, the loop is
    terminated immediately.

    If at any point ``session.shouldfail`` or ``session.shouldstop`` are set, the
    loop is terminated after the runtest protocol for the current item is finished.

    :param _pytest.main.Session session: The pytest session object.

    Stops at first non-None result, see :ref:`firstresult`.
    The return value is not used, but only stops further processing.
    """


@hookspec(firstresult=True)
def pytest_runtest_protocol(
    item: "Item", nextitem: "Optional[Item]"
) -> Optional[object]:
    """Performs the runtest protocol for a single test item.

    The default runtest protocol is this (see individual hooks for full details):

    - ``pytest_runtest_logstart(nodeid, location)``

    - Setup phase:
        - ``call = pytest_runtest_setup(item)`` (wrapped in ``CallInfo(when="setup")``)
        - ``report = pytest_runtest_makereport(item, call)``
        - ``pytest_runtest_logreport(report)``
        - ``pytest_exception_interact(call, report)`` if an interactive exception occurred

    - Call phase, if the the setup passed and the ``setuponly`` pytest option is not set:
        - ``call = pytest_runtest_call(item)`` (wrapped in ``CallInfo(when="call")``)
        - ``report = pytest_runtest_makereport(item, call)``
        - ``pytest_runtest_logreport(report)``
        - ``pytest_exception_interact(call, report)`` if an interactive exception occurred

    - Teardown phase:
        - ``call = pytest_runtest_teardown(item, nextitem)`` (wrapped in ``CallInfo(when="teardown")``)
        - ``report = pytest_runtest_makereport(item, call)``
        - ``pytest_runtest_logreport(report)``
        - ``pytest_exception_interact(call, report)`` if an interactive exception occurred

    - ``pytest_runtest_logfinish(nodeid, location)``

    :arg item: Test item for which the runtest protocol is performed.

    :arg nextitem: The scheduled-to-be-next test item (or None if this is the end my friend).

    Stops at first non-None result, see :ref:`firstresult`.
    The return value is not used, but only stops further processing.
    """


def pytest_runtest_logstart(
    nodeid: str, location: Tuple[str, Optional[int], str]
) -> None:
    """Called at the start of running the runtest protocol for a single item.

    See :func:`pytest_runtest_protocol` for a description of the runtest protocol.

    :param str nodeid: Full node ID of the item.
    :param location: A triple of ``(filename, lineno, testname)``.
    """


def pytest_runtest_logfinish(
    nodeid: str, location: Tuple[str, Optional[int], str]
) -> None:
    """Called at the end of running the runtest protocol for a single item.

    See :func:`pytest_runtest_protocol` for a description of the runtest protocol.

    :param str nodeid: Full node ID of the item.
    :param location: A triple of ``(filename, lineno, testname)``.
    """


def pytest_runtest_setup(item: "Item") -> None:
    """Called to perform the setup phase for a test item.

    The default implementation runs ``setup()`` on ``item`` and all of its
    parents (which haven't been setup yet). This includes obtaining the
    values of fixtures required by the item (which haven't been obtained
    yet).
    """


def pytest_runtest_call(item: "Item") -> None:
    """Called to run the test for test item (the call phase).

    The default implementation calls ``item.runtest()``.
    """


def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
    """Called to perform the teardown phase for a test item.

    The default implementation runs the finalizers and calls ``teardown()``
    on ``item`` and all of its parents (which need to be torn down). This
    includes running the teardown phase of fixtures required by the item (if
    they go out of scope).

    :arg nextitem: The scheduled-to-be-next test item (None if no further
                   test item is scheduled).  This argument can be used to
                   perform exact teardowns, i.e. calling just enough finalizers
                   so that nextitem only needs to call setup-functions.
    """


@hookspec(firstresult=True)
def pytest_runtest_makereport(
    item: "Item", call: "CallInfo[None]"
) -> Optional["TestReport"]:
    """Called to create a :py:class:`_pytest.reports.TestReport` for each of
    the setup, call and teardown runtest phases of a test item.

    See :func:`pytest_runtest_protocol` for a description of the runtest protocol.

    :param CallInfo[None] call: The ``CallInfo`` for the phase.

    Stops at first non-None result, see :ref:`firstresult`.
    """


def pytest_runtest_logreport(report: "TestReport") -> None:
    """Process the :py:class:`_pytest.reports.TestReport` produced for each
    of the setup, call and teardown runtest phases of an item.

    See :func:`pytest_runtest_protocol` for a description of the runtest protocol.
    """


@hookspec(firstresult=True)
def pytest_report_to_serializable(
    config: "Config", report: Union["CollectReport", "TestReport"],
) -> Optional[Dict[str, Any]]:
    """
    Serializes the given report object into a data structure suitable for sending
    over the wire, e.g. converted to JSON.
    """


@hookspec(firstresult=True)
def pytest_report_from_serializable(
    config: "Config", data: Dict[str, Any],
) -> Optional[Union["CollectReport", "TestReport"]]:
    """
    Restores a report object previously serialized with pytest_report_to_serializable().
    """


# -------------------------------------------------------------------------
# Fixture related hooks
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def pytest_fixture_setup(
    fixturedef: "FixtureDef", request: "SubRequest"
) -> Optional[object]:
    """Performs fixture setup execution.

    :return: The return value of the call to the fixture function.

    Stops at first non-None result, see :ref:`firstresult`.

    .. note::
        If the fixture function returns None, other implementations of
        this hook function will continue to be called, according to the
        behavior of the :ref:`firstresult` option.
    """


def pytest_fixture_post_finalizer(
    fixturedef: "FixtureDef", request: "SubRequest"
) -> None:
    """Called after fixture teardown, but before the cache is cleared, so
    the fixture result ``fixturedef.cached_result`` is still available (not
    ``None``)."""


# -------------------------------------------------------------------------
# test session related hooks
# -------------------------------------------------------------------------


def pytest_sessionstart(session: "Session") -> None:
    """Called after the ``Session`` object has been created and before performing collection
    and entering the run test loop.

    :param _pytest.main.Session session: the pytest session object
    """


def pytest_sessionfinish(
    session: "Session", exitstatus: Union[int, "ExitCode"],
) -> None:
    """Called after whole test run finished, right before returning the exit status to the system.

    :param _pytest.main.Session session: the pytest session object
    :param int exitstatus: the status which pytest will return to the system
    """


def pytest_unconfigure(config: "Config") -> None:
    """Called before test process is exited.

    :param _pytest.config.Config config: pytest config object
    """


# -------------------------------------------------------------------------
# hooks for customizing the assert methods
# -------------------------------------------------------------------------


def pytest_assertrepr_compare(
    config: "Config", op: str, left: object, right: object
) -> Optional[List[str]]:
    """Return explanation for comparisons in failing assert expressions.

    Return None for no custom explanation, otherwise return a list
    of strings.  The strings will be joined by newlines but any newlines
    *in* a string will be escaped.  Note that all but the first line will
    be indented slightly, the intention is for the first line to be a summary.

    :param _pytest.config.Config config: pytest config object
    """


def pytest_assertion_pass(item: "Item", lineno: int, orig: str, expl: str) -> None:
    """
    **(Experimental)**

    .. versionadded:: 5.0

    Hook called whenever an assertion *passes*.

    Use this hook to do some processing after a passing assertion.
    The original assertion information is available in the `orig` string
    and the pytest introspected assertion information is available in the
    `expl` string.

    This hook must be explicitly enabled by the ``enable_assertion_pass_hook``
    ini-file option:

    .. code-block:: ini

        [pytest]
        enable_assertion_pass_hook=true

    You need to **clean the .pyc** files in your project directory and interpreter libraries
    when enabling this option, as assertions will require to be re-written.

    :param _pytest.nodes.Item item: pytest item object of current test
    :param int lineno: line number of the assert statement
    :param string orig: string with original assertion
    :param string expl: string with assert explanation

    .. note::

        This hook is **experimental**, so its parameters or even the hook itself might
        be changed/removed without warning in any future pytest release.

        If you find this hook useful, please share your feedback opening an issue.
    """


# -------------------------------------------------------------------------
# hooks for influencing reporting (invoked from _pytest_terminal)
# -------------------------------------------------------------------------


def pytest_report_header(
    config: "Config", startdir: py.path.local
) -> Union[str, List[str]]:
    """ return a string or list of strings to be displayed as header info for terminal reporting.

    :param _pytest.config.Config config: pytest config object
    :param startdir: py.path object with the starting dir

    .. note::

        Lines returned by a plugin are displayed before those of plugins which
        ran before it.
        If you want to have your line(s) displayed first, use
        :ref:`trylast=True <plugin-hookorder>`.

    .. note::

        This function should be implemented only in plugins or ``conftest.py``
        files situated at the tests root directory due to how pytest
        :ref:`discovers plugins during startup <pluginorder>`.
    """


def pytest_report_collectionfinish(
    config: "Config", startdir: py.path.local, items: Sequence["Item"],
) -> Union[str, List[str]]:
    """
    .. versionadded:: 3.2

    Return a string or list of strings to be displayed after collection has finished successfully.

    These strings will be displayed after the standard "collected X items" message.

    :param _pytest.config.Config config: pytest config object
    :param startdir: py.path object with the starting dir
    :param items: list of pytest items that are going to be executed; this list should not be modified.

    .. note::

        Lines returned by a plugin are displayed before those of plugins which
        ran before it.
        If you want to have your line(s) displayed first, use
        :ref:`trylast=True <plugin-hookorder>`.
    """


@hookspec(firstresult=True)
def pytest_report_teststatus(
    report: Union["CollectReport", "TestReport"], config: "Config"
) -> Tuple[
    str, str, Union[str, Mapping[str, bool]],
]:
    """Return result-category, shortletter and verbose word for status
    reporting.

    The result-category is a category in which to count the result, for
    example "passed", "skipped", "error" or the empty string.

    The shortletter is shown as testing progresses, for example ".", "s",
    "E" or the empty string.

    The verbose word is shown as testing progresses in verbose mode, for
    example "PASSED", "SKIPPED", "ERROR" or the empty string.

    pytest may style these implicitly according to the report outcome.
    To provide explicit styling, return a tuple for the verbose word,
    for example ``"rerun", "R", ("RERUN", {"yellow": True})``.

    :param report: The report object whose status is to be returned.
    :param _pytest.config.Config config: The pytest config object.

    Stops at first non-None result, see :ref:`firstresult`.
    """


def pytest_terminal_summary(
    terminalreporter: "TerminalReporter", exitstatus: "ExitCode", config: "Config",
) -> None:
    """Add a section to terminal summary reporting.

    :param _pytest.terminal.TerminalReporter terminalreporter: the internal terminal reporter object
    :param int exitstatus: the exit status that will be reported back to the OS
    :param _pytest.config.Config config: pytest config object

    .. versionadded:: 4.2
        The ``config`` parameter.
    """


@hookspec(historic=True, warn_on_impl=WARNING_CAPTURED_HOOK)
def pytest_warning_captured(
    warning_message: "warnings.WarningMessage",
    when: "Literal['config', 'collect', 'runtest']",
    item: Optional["Item"],
    location: Optional[Tuple[str, int, str]],
) -> None:
    """(**Deprecated**) Process a warning captured by the internal pytest warnings plugin.

    .. deprecated:: 6.0

    This hook is considered deprecated and will be removed in a future pytest version.
    Use :func:`pytest_warning_recorded` instead.

    :param warnings.WarningMessage warning_message:
        The captured warning. This is the same object produced by :py:func:`warnings.catch_warnings`, and contains
        the same attributes as the parameters of :py:func:`warnings.showwarning`.

    :param str when:
        Indicates when the warning was captured. Possible values:

        * ``"config"``: during pytest configuration/initialization stage.
        * ``"collect"``: during test collection.
        * ``"runtest"``: during test execution.

    :param pytest.Item|None item:
        The item being executed if ``when`` is ``"runtest"``, otherwise ``None``.

    :param tuple location:
        When available, holds information about the execution context of the captured
        warning (filename, linenumber, function). ``function`` evaluates to <module>
        when the execution context is at the module level.
    """


@hookspec(historic=True)
def pytest_warning_recorded(
    warning_message: "warnings.WarningMessage",
    when: "Literal['config', 'collect', 'runtest']",
    nodeid: str,
    location: Optional[Tuple[str, int, str]],
) -> None:
    """
    Process a warning captured by the internal pytest warnings plugin.

    :param warnings.WarningMessage warning_message:
        The captured warning. This is the same object produced by :py:func:`warnings.catch_warnings`, and contains
        the same attributes as the parameters of :py:func:`warnings.showwarning`.

    :param str when:
        Indicates when the warning was captured. Possible values:

        * ``"config"``: during pytest configuration/initialization stage.
        * ``"collect"``: during test collection.
        * ``"runtest"``: during test execution.

    :param str nodeid: full id of the item

    :param tuple|None location:
        When available, holds information about the execution context of the captured
        warning (filename, linenumber, function). ``function`` evaluates to <module>
        when the execution context is at the module level.

    .. versionadded:: 6.0
    """


# -------------------------------------------------------------------------
# error handling and internal debugging hooks
# -------------------------------------------------------------------------


def pytest_internalerror(
    excrepr: "ExceptionRepr", excinfo: "ExceptionInfo[BaseException]",
) -> Optional[bool]:
    """Called for internal errors.

    Return True to suppress the fallback handling of printing an
    INTERNALERROR message directly to sys.stderr.
    """


def pytest_keyboard_interrupt(
    excinfo: "ExceptionInfo[Union[KeyboardInterrupt, Exit]]",
) -> None:
    """ called for keyboard interrupt. """


def pytest_exception_interact(
    node: "Node",
    call: "CallInfo[object]",
    report: Union["CollectReport", "TestReport"],
) -> None:
    """Called when an exception was raised which can potentially be
    interactively handled.

    May be called during collection (see :py:func:`pytest_make_collect_report`),
    in which case ``report`` is a :py:class:`_pytest.reports.CollectReport`.

    May be called during runtest of an item (see :py:func:`pytest_runtest_protocol`),
    in which case ``report`` is a :py:class:`_pytest.reports.TestReport`.

    This hook is not called if the exception that was raised is an internal
    exception like ``skip.Exception``.
    """


def pytest_enter_pdb(config: "Config", pdb: "pdb.Pdb") -> None:
    """ called upon pdb.set_trace(), can be used by plugins to take special
    action just before the python debugger enters in interactive mode.

    :param _pytest.config.Config config: pytest config object
    :param pdb.Pdb pdb: Pdb instance
    """


def pytest_leave_pdb(config: "Config", pdb: "pdb.Pdb") -> None:
    """ called when leaving pdb (e.g. with continue after pdb.set_trace()).

    Can be used by plugins to take special action just after the python
    debugger leaves interactive mode.

    :param _pytest.config.Config config: pytest config object
    :param pdb.Pdb pdb: Pdb instance
    """
