"""
support for presenting detailed information in failing assertions.
"""
import sys
from typing import Any
from typing import Generator
from typing import List
from typing import Optional

from _pytest.assertion import rewrite
from _pytest.assertion import truncate
from _pytest.assertion import util
from _pytest.assertion.rewrite import assertstate_key
from _pytest.compat import TYPE_CHECKING
from _pytest.config import Config
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item

if TYPE_CHECKING:
    from _pytest.main import Session


def pytest_addoption(parser: Parser) -> None:
    group = parser.getgroup("debugconfig")
    group.addoption(
        "--assert",
        action="store",
        dest="assertmode",
        choices=("rewrite", "plain"),
        default="rewrite",
        metavar="MODE",
        help=(
            "Control assertion debugging tools.\n"
            "'plain' performs no assertion debugging.\n"
            "'rewrite' (the default) rewrites assert statements in test modules"
            " on import to provide assert expression information."
        ),
    )
    parser.addini(
        "enable_assertion_pass_hook",
        type="bool",
        default=False,
        help="Enables the pytest_assertion_pass hook."
        "Make sure to delete any previously generated pyc cache files.",
    )


def register_assert_rewrite(*names: str) -> None:
    """Register one or more module names to be rewritten on import.

    This function will make sure that this module or all modules inside
    the package will get their assert statements rewritten.
    Thus you should make sure to call this before the module is
    actually imported, usually in your __init__.py if you are a plugin
    using a package.

    :raise TypeError: if the given module names are not strings.
    """
    for name in names:
        if not isinstance(name, str):
            msg = "expected module names as *args, got {0} instead"
            raise TypeError(msg.format(repr(names)))
    for hook in sys.meta_path:
        if isinstance(hook, rewrite.AssertionRewritingHook):
            importhook = hook
            break
    else:
        # TODO(typing): Add a protocol for mark_rewrite() and use it
        # for importhook and for PytestPluginManager.rewrite_hook.
        importhook = DummyRewriteHook()  # type: ignore
    importhook.mark_rewrite(*names)


class DummyRewriteHook:
    """A no-op import hook for when rewriting is disabled."""

    def mark_rewrite(self, *names: str) -> None:
        pass


class AssertionState:
    """State for the assertion plugin."""

    def __init__(self, config: Config, mode) -> None:
        self.mode = mode
        self.trace = config.trace.root.get("assertion")
        self.hook = None  # type: Optional[rewrite.AssertionRewritingHook]


def install_importhook(config: Config) -> rewrite.AssertionRewritingHook:
    """Try to install the rewrite hook, raise SystemError if it fails."""
    config._store[assertstate_key] = AssertionState(config, "rewrite")
    config._store[assertstate_key].hook = hook = rewrite.AssertionRewritingHook(config)
    sys.meta_path.insert(0, hook)
    config._store[assertstate_key].trace("installed rewrite import hook")

    def undo() -> None:
        hook = config._store[assertstate_key].hook
        if hook is not None and hook in sys.meta_path:
            sys.meta_path.remove(hook)

    config.add_cleanup(undo)
    return hook


def pytest_collection(session: "Session") -> None:
    # this hook is only called when test modules are collected
    # so for example not in the master process of pytest-xdist
    # (which does not collect test modules)
    assertstate = session.config._store.get(assertstate_key, None)
    if assertstate:
        if assertstate.hook is not None:
            assertstate.hook.set_session(session)


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_protocol(item: Item) -> Generator[None, None, None]:
    """Setup the pytest_assertrepr_compare and pytest_assertion_pass hooks

    The rewrite module will use util._reprcompare if
    it exists to use custom reporting via the
    pytest_assertrepr_compare hook.  This sets up this custom
    comparison for the test.
    """

    ihook = item.ihook

    def callbinrepr(op, left: object, right: object) -> Optional[str]:
        """Call the pytest_assertrepr_compare hook and prepare the result

        This uses the first result from the hook and then ensures the
        following:
        * Overly verbose explanations are truncated unless configured otherwise
          (eg. if running in verbose mode).
        * Embedded newlines are escaped to help util.format_explanation()
          later.
        * If the rewrite mode is used embedded %-characters are replaced
          to protect later % formatting.

        The result can be formatted by util.format_explanation() for
        pretty printing.
        """
        hook_result = ihook.pytest_assertrepr_compare(
            config=item.config, op=op, left=left, right=right
        )
        for new_expl in hook_result:
            if new_expl:
                new_expl = truncate.truncate_if_required(new_expl, item)
                new_expl = [line.replace("\n", "\\n") for line in new_expl]
                res = "\n~".join(new_expl)
                if item.config.getvalue("assertmode") == "rewrite":
                    res = res.replace("%", "%%")
                return res
        return None

    saved_assert_hooks = util._reprcompare, util._assertion_pass
    util._reprcompare = callbinrepr

    if ihook.pytest_assertion_pass.get_hookimpls():

        def call_assertion_pass_hook(lineno: int, orig: str, expl: str) -> None:
            ihook.pytest_assertion_pass(item=item, lineno=lineno, orig=orig, expl=expl)

        util._assertion_pass = call_assertion_pass_hook

    yield

    util._reprcompare, util._assertion_pass = saved_assert_hooks


def pytest_sessionfinish(session: "Session") -> None:
    assertstate = session.config._store.get(assertstate_key, None)
    if assertstate:
        if assertstate.hook is not None:
            assertstate.hook.set_session(None)


def pytest_assertrepr_compare(
    config: Config, op: str, left: Any, right: Any
) -> Optional[List[str]]:
    return util.assertrepr_compare(config=config, op=op, left=left, right=right)
