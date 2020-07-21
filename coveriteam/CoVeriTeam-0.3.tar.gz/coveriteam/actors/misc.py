# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

from benchexec.result import get_result_classification
from coveriteam.language.artifact import (
    CProgram,
    Condition,
    Witness,
    Specification,
    TestGoal,
    TestSpecification,
    TestSuite,
    Verdict,
    AtomicActorDefinition,
)
from coveriteam.language.actor import Actor, Instrumentor, Reducer, Transformer
from coveriteam.language.atomicactor import AtomicActor
import os
import logging
from coveriteam.util import create_archive


class WitnessInstrumentor(Instrumentor, AtomicActor):
    _input_artifacts = {"program": CProgram, "witness": Witness}
    _output_artifacts = {"program": CProgram}
    _result_files_patterns = ["**/*.c"]

    def _act(self, program, witness):
        # Witness is passes as specification in this case. This is from CPAchecker, can't do much
        self._run_tool(program.path, witness.path)
        return super()._act()

    def _extract_result(self):
        # extract result
        for file in self.log_dir().glob("**/*.c"):
            instrumentedProgram = CProgram(file)

        return {"program": instrumentedProgram}


class WitnessToTest(AtomicActor):
    _input_artifacts = {"program": CProgram, "spec": Specification, "witness": Witness}
    _output_artifacts = {"test_suite": TestSuite}
    _result_files_patterns = ["**/*.xml"]

    def _act(self, program, spec, witness):
        options = ["-witness", self._get_relative_path_to_tool(witness.path)]
        self._run_tool(program.path, spec.path, options)
        return super()._act()

    def _extract_result(self):
        # We assume that the test generator will succeed and create a directory
        # containing metadata.xml. This directory is the test suite.
        for file in self.log_dir().glob("**/metadata.xml"):
            testSuite = TestSuite(os.path.dirname(file))

        return {"test_suite": testSuite}


class TestCriterionInstrumentor(Instrumentor, AtomicActor):
    _input_artifacts = {"program": CProgram, "test_spec": TestSpecification}
    _output_artifacts = {"program": CProgram}
    _result_files_patterns = ["**/*.c"]

    def _act(self, program, test_spec):
        # hard coded output path
        options = ["--output", "instrumented.c"]
        self._run_tool(program.path, test_spec.path, options)
        return super()._act()

    def _extract_result(self):
        # extract result
        for file in self.log_dir().glob("**/*.c"):
            instrumentedProgram = CProgram(file)

        return {"program": instrumentedProgram}


class TestGoalPruner(Reducer, AtomicActor):
    _input_artifacts = {
        "program": CProgram,
        "test_spec": TestSpecification,
        "covered_goals": TestGoal,
    }
    _output_artifacts = {"program": CProgram}
    _result_files_patterns = ["**/*.c"]

    def _act(self, program, test_spec, covered_goals):
        # hard coded output path
        options = ["--output", "reduced.c"]
        if covered_goals.path:
            options += [
                "--covered-labels",
                self._get_relative_path_to_tool(covered_goals.path),
            ]

        self._run_tool(program.path, test_spec.path, options)
        return super()._act()

    def _extract_result(self):
        # extract result
        for file in self.log_dir().glob("**/reduced.c"):
            prunedProgram = CProgram(file)

        return {"program": prunedProgram}


class TestGoalAnnotator(Reducer, AtomicActor):
    _input_artifacts = {
        "program": CProgram,
        "test_spec": TestSpecification,
        "covered_goals": TestGoal,
    }
    _output_artifacts = {"program": CProgram}
    _result_files_patterns = ["**/*.c"]

    def _act(self, program, test_spec, covered_goals):
        # hard coded output path
        options = ["--output", "reduced.c"]
        if covered_goals.path:
            options += [
                "--covered-labels",
                self._get_relative_path_to_tool(covered_goals.path),
            ]

        self._run_tool(program.path, test_spec.path, options)
        return super()._act()

    def _extract_result(self):
        # extract result
        for file in self.log_dir().glob("**/reduced.c"):
            annotatedProgram = CProgram(file)

        return {"program": annotatedProgram}


class TestGoalExtractor(Transformer, AtomicActor):
    _input_artifacts = {
        "program": CProgram,
        "test_spec": TestSpecification,
        "test_suite": TestSuite,
    }
    _output_artifacts = {"extracted_goals": TestGoal}
    _result_files_patterns = ["**/*.txt"]

    def _act(self, program, test_spec, test_suite):
        # hard coded output path
        options_output = ["-o", "covered_goals.txt"]
        # Passing the directory of the test suite
        options_remaining_goals = ["--test-suite", test_suite.path]
        options = options_remaining_goals + options_output
        self._run_tool(program.path, test_spec.path, options)
        return super()._act()

    def _extract_result(self):
        # extract result
        for file in self.log_dir().glob("**/covered_goals.txt"):
            extracted_goals = TestGoal(file)

        return {"extracted_goals": extracted_goals}


class CMCReducer(Transformer, AtomicActor):
    _input_artifacts = {"program": CProgram, "condition": Condition}
    _output_artifacts = {"program": CProgram}
    _result_files_patterns = ["**/*.c"]

    def _act(self, program, condition):
        # hard coded output path
        options_assm_file = [
            "-setprop",
            "residualprogram.assumptionFile="
            + self._get_relative_path_to_tool(condition.path),
        ]
        options_assm_automaton = [
            "-setprop",
            "AssumptionAutomaton.cpa.automaton.inputFile="
            + self._get_relative_path_to_tool(condition.path),
        ]
        options = options_assm_automaton + options_assm_file
        self._run_tool(program.path, "", options)
        return super()._act()

    def _extract_result(self):
        # extract result
        for file in self.log_dir().glob("**/*.c"):
            reducedProgram = CProgram(file)

        return {"program": reducedProgram}


class TestValidator(Transformer, AtomicActor):
    _input_artifacts = {
        "program": CProgram,
        "test_suite": TestSuite,
        "test_spec": TestSpecification,
    }
    _output_artifacts = {"verdict": Verdict}
    _result_files_patterns = []

    def _act(self, program, test_suite, test_spec):
        options_spec = ["--goal", self._get_relative_path_to_tool(test_spec.path)]
        testzip = os.path.join(os.path.dirname(test_suite.path), "test_suite.zip")
        create_archive(test_suite.path, testzip)
        testzip = self._get_relative_path_to_tool(testzip)
        options_test_suite = ["--test-suite", testzip]
        options = options_test_suite + options_spec
        self._run_tool(program.path, "", options)
        return super()._act()

    def _extract_result(self):
        try:
            with open(self.log_file(), "rt", errors="ignore") as outputFile:
                output = outputFile.readlines()
                # first 6 lines are for logging, rest is output of subprocess, see runexecutor.py for details
                output = output[6:]
        except IOError as e:
            logging.warning("Cannot read log file: %s", e.strerror)
            output = []

        verdict = Verdict(
            get_result_classification(self._tool.determine_result(0, 0, output, False))
        )
        return {"verdict": verdict}


class AlgorithmSelector(AtomicActor):
    _input_artifacts = {"program": CProgram, "spec": Specification}
    _output_artifacts = {"actordef": AtomicActorDefinition}
    _result_files_patterns = []

    def _act(self, program, spec):
        self._run_tool(program.path, spec.path)
        return super()._act()

    def _extract_result(self):
        # TODO this could be put in a pattern
        try:
            with open(self.log_file(), "rt", errors="ignore") as outputFile:
                output = outputFile.readlines()
                # first 6 lines are for logging, rest is output of subprocess, see runexecutor.py for details
                output = output[6:]
        except IOError as e:
            logging.warning("Cannot read log file: %s", e.strerror)
            output = []

        # It assumes that the first line will contain the actor name.
        actordef = AtomicActorDefinition(output[0].rstrip())

        return {"actordef": actordef}


class DynamicActor(Actor):
    # TODO find a place to put this actor.
    # It is neither an atomic not a composite actor.

    def __init__(self, actorkind):
        self.actor_to_execute_class = actorkind
        self._input_artifacts = self.actor_to_execute_class._input_artifacts.copy()
        # Additionally add the actor definition.
        self._input_artifacts.update(actordef=AtomicActorDefinition)
        self._output_artifacts = self.actor_to_execute_class._output_artifacts.copy()

    def name(self):
        return self.actor_to_execute_class.get_actor_kind()

    def _act(self, actordef, **kwargs):
        """
        This should first create an actor based on the actor definition, and then call its _act.
        This should suffice.
        This makes me think it is a composite actor.
        """
        actor_to_execute = self.actor_to_execute_class(actordef.path)
        return actor_to_execute.act(**kwargs)
