#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template
import os


class HtmlTemplates:
    def __init__(self, baseDir):
        self.TEMPLATES_DIR = baseDir

    def _read_template(self, template_path):
        with open(os.path.join(self.TEMPLATES_DIR, template_path)) as template:
            result = template.read()
            return result

    def render(self, template_path, data):
        return Template(
            self._read_template(template_path)
        ).render(data)
