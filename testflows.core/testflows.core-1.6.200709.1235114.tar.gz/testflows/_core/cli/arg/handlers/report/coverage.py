# Copyright 2019 Katteli Inc.
# TestFlows Test Framework (http://testflows.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys
import json
import time
import base64
import threading
import importlib.util

from datetime import datetime

import testflows.settings as settings
import testflows._core.cli.arg.type as argtype

from testflows._core import __version__
from testflows._core.flags import Flags, SKIP
from testflows._core.testtype import TestType
from testflows._core.cli.arg.common import epilog
from testflows._core.cli.arg.common import HelpFormatter
from testflows._core.cli.arg.handlers.handler import Handler as HandlerBase
from testflows._core.cli.arg.handlers.report.copyright import copyright
from testflows._core.transform.log.pipeline import ResultsLogPipeline
from testflows._core.transform.log.short import format_test, format_result
from testflows._core.utils.timefuncs import localfromtimestamp, strftimedelta
from testflows._core.name import sep
from testflows._core.transform.log.report.totals import Counts
from testflows._core.objects import Requirement

logo = '<img class="logo" src="data:image/png;base64,%(data)s" alt="logo"/>'
testflows = '<span class="testflows-logo"></span> [<span class="logo-test">Test</span><span class="logo-flows">Flows</span>]'
testflows_em = testflows.replace("[", "").replace("]", "")

FailResults = ["Fail", "Error", "Null"]
XoutResults = ["XOK", "XFail", "XError", "XNull"]

template = f"""
<section class="clearfix">%(logo)s%(confidential)s%(copyright)s</section>

---
# Requirements Coverage Report
%(body)s

---
Generated by {testflows} Open-Source Test Framework

[<span class="logo-test">Test</span><span class="logo-flows">Flows</span>]: https://testflows.com
[ClickHouse]: https://clickhouse.yandex


<script>
%(script)s
</script>

"""

script = """
window.onload = function(){
    // Toggle requirement description on click
    document.querySelectorAll('.requirement').forEach(
        function(item){
            item.addEventListener('click', function(){
                item.nextElementSibling.classList.toggle('show');
                item.children[0].classList.toggle('active');
            });
        });

    // Toggle test procedure on click
    document.querySelectorAll('.test').forEach(
        function(item){
            item.addEventListener('click', function(){
                item.nextElementSibling.classList.toggle('show');
                item.classList.toggle('active');
            });
        });
}
"""

class Formatter:
    utf_icons = {
        "satisfied": "\u2714",
        "unsatisfied": "\u2718",
        "untested": "\u270E"
    }

    icon_colors = {
        "satisfied": "color-ok",
        "unsatisfied": "color-fail",
        "untested": "color-error"
    }

    def format_logo(self, data):
        if not data["company"].get("logo"):
            return ""
        data = base64.b64encode(data["company"]["logo"]).decode("utf-8")
        return '\n<p>' + logo % {"data": data} + "</p>\n"

    def format_confidential(self, data):
        if not data["company"].get("confidential"):
            return ""
        return f'\n<p class="confidential">Document status - Confidential</p>\n'

    def format_copyright(self, data):
        if not data["company"].get("name"):
            return ""
        return (f'\n<p class="copyright">\n'
            f'{copyright(data["company"]["name"])}\n'
            "</p>\n")

    def format_metadata(self, data):
        metadata = data["metadata"]
        s = (
            "\n\n"
            f"||**Date**||{localfromtimestamp(metadata['date']):%b %d, %Y %-H:%M}||\n"
            f'||**Framework**||'
            f'{testflows} {metadata["version"]}||\n'
        )
        return s + "\n"

    def format_summary(self, data):
        counts = data["counts"]

        def template(value, title, color):
            return (
                f'<div class="c100 p{value} {color} smaller-title">'
                    f'<span>{value}%</span>'
                    f'<span class="title">{title}</span>'
                    '<div class="slice">'
                        '<div class="bar"></div>'
                        '<div class="fill"></div>'
                    '</div>'
                '</div>\n')

        s = "\n## Summary\n"
        if counts.units <= 0:
            s += "No tests"
        else:
            s += '<div class="chart">'
            if counts.satisfied > 0:
                s += template(f"{counts.satisfied / float(counts.units) * 100:.0f}", "Satisfied", "green")
            if counts.unsatisfied > 0:
                s += template(f"{counts.unsatisfied / float(counts.units) * 100:.0f}", "Unsatisfied", "red")
            if counts.untested > 0:
                s += template(f"{counts.untested / float(counts.units) * 100:.0f}", "Untested", "orange")
            s += '</div>\n'
        return s

    def format_statistics(self, data):
        counts = data["counts"]
        result_map = {
            "OK": "Satisfied",
            "Fail": "Unsatisfied",
            "Error": "Untested"
        }
        s = "\n\n## Statistics\n"
        s += "||" + "||".join(
            ["<span></span>", "Units"]
            + [f'<span class="result result-{k.lower()}">{v}</span>' for k, v in result_map.items()]
        ) + "||\n"
        s += "||" + "||".join([f"<center>{i}</center>" for i in ["**Requirements**",
                str(counts.units), str(counts.satisfied),
                str(counts.unsatisfied), str(counts.untested)]]) + "||\n"
        return s + "\n"

    def format_table(self, data):
        reqs = data["requirements"]
        s = "\n\n## Coverage\n"
        for r in reqs.values():
            s += f'\n<section class="requirement"><span class="requirement-inline"><i class="utf-icon {self.icon_colors[r["status"]]}">{self.utf_icons[r["status"]]}</i>{r["requirement"].name}</span></section>'
            description = r["requirement"].description.replace("\\n","\n")
            if description:
                s += f'\n<div markdown="1" class="requirement-description hidden">\n{description}\n</div>'
            for test in r["tests"]:
                result = test["result"]
                cls = result["result_type"].lower()
                s += f'\n<div class="test"><span class="result result-inline result-{cls}">{result["result_type"]}</span><span class="time time-inline">{strftimedelta(result["message_rtime"])}</span>{test["test"]["test_name"]}</div>'
                s += f'\n<div class="test-procedure hidden">\n```testflows\n{test["messages"]}\n```\n</div>'
            if not r["tests"]:
                s += f'\n<div class="no-tests">\n<span class="result-inline">\u270E</span>\nNo tests\n</div>'
            s += "\n"
        return s + "\n"

    def format(self, data):
        body = ""
        body += self.format_metadata(data)
        body += self.format_summary(data)
        body += self.format_statistics(data)
        body += self.format_table(data)
        return template.strip() % {
            "logo": self.format_logo(data),
            "confidential": self.format_confidential(data),
            "copyright": self.format_copyright(data),
            "body": body,
            "script": script}

class Counts(object):
    def __init__(self, name, units, satisfied, unsatisfied, untested):
        self.name = name
        self.units = units
        self.satisfied = satisfied
        self.unsatisfied = unsatisfied
        self.untested = untested

    def __bool__(self):
        return self.units > 0

class Handler(HandlerBase):
    @classmethod
    def add_command(cls, commands):
        parser = commands.add_parser("coverage", help="requirements coverage report", epilog=epilog(),
            description="Generate requirements coverage report.",
            formatter_class=HelpFormatter)

        parser.add_argument("requirements", metavar="source", type=str,
                help="requirements source file")
        parser.add_argument("input", metavar="input", type=argtype.logfile("r", bufsize=1, encoding="utf-8"),
                nargs="?", help="input log, default: stdin", default="-")
        parser.add_argument("output", metavar="output", type=argtype.file("w", bufsize=1, encoding="utf-8"),
                nargs="?", help='output file, default: stdout', default="-")
        parser.add_argument("--show", metavar="status", type=str, nargs="+", help="verification status. Choices: 'satisfied', 'unsatisfied', 'untested'",
            choices=["satisfied", "unsatisfied", "untested"],
            default=["satisfied", "unsatisfied", "untested"])
        parser.add_argument("--input-link", metavar="attribute",
            help="attribute that is used as a link to the input log, default: job.url",
            type=str, default="job.url")
        parser.add_argument("--format", metavar="type", type=str,
            help="output format, default: md (Markdown)", choices=["md"], default="md")
        parser.add_argument("--copyright", metavar="name", help="add copyright notice", type=str)
        parser.add_argument("--confidential", help="mark as confidential", action="store_true")
        parser.add_argument("--logo", metavar="path", type=argtype.file("rb"),
                help='use logo image (.png)')

        parser.set_defaults(func=cls())

    def get_attribute(self, result, name, default=None):
        tests = list(result["tests"].values())

        if not tests:
            return default

        test = tests[0]["test"]
        for attr in test["attributes"]:
            if attr["attribute_name"] == name:
                return attr["attribute_value"]

        return default

    def table(self, results):
        table = {
            "header": ["Requirement", "Tests"],
            "rows": [],
        }

        return table

    def metadata(self, results):
        return {
            "date": time.time(),
            "version": __version__,
        }

    def requirements(self, path):
        spec = importlib.util.spec_from_file_location("requirements", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _requirements = {}

        for name, value in vars(module).items():
            if not isinstance(value, Requirement):
                continue
            _requirements[value.name] = {"requirement": value, "tests": []}

        return _requirements

    def add_test_messages(self, test, idx, tests, tests_by_parent, tests_by_id):
        started = test["test"]["message_time"]
        ended = test["result"]["message_time"]

        messages = [format_test(test["test"], "", tests_by_parent, tests_by_id)]

        if getattr(TestType, test["test"]["test_type"]) > TestType.Test:
            for t in tests[idx + 1:]:
                flags = Flags(t["test"]["test_flags"])
                if flags & SKIP and settings.show_skipped is False:
                    continue
                if t["test"]["message_time"] > ended:
                    break
                if getattr(TestType, t["test"]["test_type"]) >= TestType.Test \
                        and t["test"]["test_id"].startswith(test["test"]["test_id"]):
                    messages.append(format_test(t["test"], "", tests_by_parent, tests_by_id))
                    messages.append(format_result(t["result"]))
        else:
            for t in tests[idx + 1:]:
                flags = Flags(t["test"]["test_flags"])
                if flags & SKIP and settings.show_skipped is False:
                    continue
                if t["test"]["message_time"] > ended:
                    break
                if t["test"]["test_id"].startswith(test["test"]["test_id"]):
                    messages.append(format_test(t["test"], "", tests_by_parent, tests_by_id))
                    messages.append(format_result(t["result"]))

        messages.append(format_result(test["result"]))

        test["messages"] = "".join(messages)
        return test

    def add_tests(self, requirements, results):
        tests = list(results["tests"].values())
        for i, test in enumerate(tests):
            flags = Flags(test["test"]["test_flags"])
            if flags & SKIP and settings.show_skipped is False:
                continue
            result = test["result"]
            if getattr(TestType, result["test_type"]) < TestType.Test:
                continue
            for requirement in test["test"]["requirements"]:
                if requirement["requirement_name"] in requirements:
                    requirements[requirement["requirement_name"]]["tests"].append(self.add_test_messages(test, i, tests, results["tests_by_parent"], results["tests_by_id"]))
        return requirements

    def counts(self, requirements):
        counts = Counts("requirements", *([0] * 4))

        for req in requirements.values():
            counts.units += 1
            tests = req["tests"]
            if not tests:
                counts.untested += 1
                req["status"] = "untested"
            else:
                satisfied = True
                for test in tests:
                    result = test["result"]
                    if result["result_type"] != "OK":
                        satisfied = False
                if satisfied:
                    counts.satisfied += 1
                    req["status"] = "satisfied"
                else:
                    counts.unsatisfied += 1
                    req["status"] = "unsatisfied"
        return counts

    def company(self, args):
        d = {}
        if args.copyright:
            d["name"] = args.copyright
        if args.confidential:
            d["confidential"] = True
        if args.logo:
            d["logo"] = args.logo.read()
        return d

    def data(self, source, results, args):
        d = dict()
        requirements = self.requirements(source)
        d["requirements"] = self.add_tests(requirements, results)
        d["metadata"] = self.metadata(results)
        d["counts"] = self.counts(d["requirements"])
        d["company"] = self.company(args)
        counts = d["counts"]
        return d

    def generate(self, formatter, results, args):
        output = args.output
        output.write(
            formatter.format(self.data(args.requirements, results, args))
        )
        output.write("\n")

    def handle(self, args):
        results = {}
        formatter = Formatter()
        ResultsLogPipeline(args.input, results).run()
        self.generate(formatter, results, args)
