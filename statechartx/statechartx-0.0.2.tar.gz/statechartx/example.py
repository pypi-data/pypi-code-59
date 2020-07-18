# -*- coding: utf-8 -*-

from statechart import Event, FinalState, InitialState, Statechart, Transition
from statechartx import TerminalState, Workflow, WorkflowFactory, WorkflowMetadata


class StateA(TerminalState):
    """Every TerminalState always has access to:
        - the workflow metadata via self.metadata
    """
    def init(self) -> None:
        self._a = self.metadata.a

    def do(self, event: Event) -> None:
        print("state '{}' got event '{}'".format(self.name, event))


class StateB(TerminalState):
    """Every TerminalState always has access to:
        - the workflow metadata via self.metadata
    """
    def init(self) -> None:
        self._b = self.metadata.b

    def do(self, event: Event) -> None:
        print("state '{}' got event '{}'".format(self.name, event))


class MainWorkflow(Workflow):
    """Every Workflow always has access to:
        - the workflow metadata via self.metadata
        - the workflow factory via parameter factory in method init().
    """
    def init(self, factory: WorkflowFactory) -> None:
        state_a = factory.create_state("state-a", self, StateA)
        state_b = factory.create_state("state-b", self, StateB)

        init = InitialState(self)
        final = FinalState(self)

        Transition(init, state_a)
        Transition(state_a, state_b, event=Event("to-state-b"))
        Transition(state_b, final, event=Event("final"))


def main() -> None:
    """Code here shows how everything is wired together.

    The following lines are the expected output:

        state 'state-a' got event 'None'
        state 'state-b' got event 'Event(name="to-state-b", data={})'
    """
    # Create the state machine -- the root context of every workflow.
    state_machine = Statechart("state-machine")

    # Create the workflow metadata with all the data accessible to all states and workflows.
    metadata = WorkflowMetadata(a=10, b="foo", c="bar")

    # Create the workflow factory backed by the workflow metadata.
    factory = WorkflowFactory(metadata)

    # Create the main workflow using the workflow factory.
    main_workflow = factory.create_workflow("main-workflow", state_machine, MainWorkflow)

    # Set up the main transitions.
    init = InitialState(state_machine)
    final = FinalState(state_machine)
    Transition(init, main_workflow)
    Transition(main_workflow, final, event=Event("final"))

    # Run the state machine.
    state_machine.start()
    state_machine.dispatch(Event("to-state-b"))


if __name__ == "__main__":
    main()
