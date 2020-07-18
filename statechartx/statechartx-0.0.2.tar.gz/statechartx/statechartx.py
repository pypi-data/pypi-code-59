# -*- coding: utf-8 -*-

try:
    from typing import Any, Type
except ImportError:
    pass

from statechart import CompositeState, State


class WorkflowMetadata(object):
    """Holds shared, common data.

    Args:
        kwargs: The shared, common data.
    """
    def __init__(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)


class TerminalState(State):
    """A state containing no other other states or workflows.

    Args:
        name: The name of this state.
        context: The parent context (as a composite state) of this state.
        metadata: The metadata accessible to this state.
    """
    def __init__(self, name: str, context: CompositeState, metadata: WorkflowMetadata) -> None:
        super().__init__(name, context)

        self._metadata = metadata

        self.init()

    @property
    def metadata(self) -> WorkflowMetadata:
        """Returns the metadata."""
        return self._metadata

    def init(self) -> None:
        """Initialises the state.

        Subclasses must override this method to implement their own initialisation.
        """
        raise NotImplementedError


class Workflow(CompositeState):
    """A workflow is a state with transitions, the same as a composite state in statechart.

    Args:
        name: The name of this workflow.
        context: The parent context (as a composite state) of this workflow.
        metadata: The metadata accessible to this state.
        factory: The factory for creating the states and the workflows this workflow depends on.
    """
    def __init__(self,
                 name: str,
                 context: CompositeState,
                 metadata: WorkflowMetadata,
                 factory: "WorkflowFactory") -> None:
        super().__init__(name, context)

        self._metadata = metadata

        self.init(factory)

    @property
    def metadata(self) -> WorkflowMetadata:
        """Returns the metadata."""
        return self._metadata

    def init(self, factory: "WorkflowFactory") -> None:
        """Initialises the workflow.

        Subclasses must override this method to create the required states and the workflows
        including the transitions among them.

        Args:
            factory: The factory for creating the states and the workflows this workflow depends on.
                Everything this class needs for creating its instance must be available from the
                factory.
        """
        raise NotImplementedError


class WorkflowFactory(object):
    """A factory for creating terminal states and workflows.

    Args:
        metadata: The metadata the factory uses to create states and workflows.
    """
    def __init__(self, metadata: WorkflowMetadata) -> None:
        self._metadata = metadata

    def create_state(self,
                     name: str,
                     context: CompositeState,
                     type_: Type[TerminalState]) -> TerminalState:
        """Creates a terminal state.

        Args:
            name: The name of this terminal state.
            context: The parent context (as a composite state) of this terminal state.
            type_: The target type of this terminal state to create.

        Returns:
            An instance of the target terminal state.
        """
        return type_(name, context, self._metadata)

    def create_workflow(self,
                        name: str,
                        context: CompositeState,
                        type_: Type[Workflow]) -> Workflow:
        """Creates a workflow.

        Args:
            name: The name of this workflow.
            context: The parent context (as a composite state) of this workflow.
            type_: The target type of this workflow to create.

        Returns:
            An instance of the target workflow.
        """
        return type_(name, context, self._metadata, self)
