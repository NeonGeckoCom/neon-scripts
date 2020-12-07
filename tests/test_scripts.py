# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
#
# Copyright 2008-2020 Neongecko.com Inc. | All Rights Reserved
#
# Notice of License - Duplicating this Notice of License near the start of any file containing
# a derivative of this software is a condition of license for this software.
# Friendly Licensing:
# No charge, open source royalty free use of the Neon AI software source and object is offered for
# educational users, noncommercial enthusiasts, Public Benefit Corporations (and LLCs) and
# Social Purpose Corporations (and LLCs). Developers can contact developers@neon.ai
# For commercial licensing, distribution of derivative works or redistribution please contact licenses@neon.ai
# Distributed on an "AS IS” basis without warranties or conditions of any kind, either express or implied.
# Trademarks of Neongecko: Neon AI(TM), Neon Assist (TM), Neon Communicator(TM), Klat(TM)
# Authors: Guy Daniels, Daniel McKnight, Regina Bloomstine, Elon Gasper, Richard Leeds
#
# Specialized conversational reconveyance options from Conversation Processing Intelligence Corp.
# US Patents 2008-2020: US7424516, US20140161250, US20140177813, US8638908, US8068604, US8553852, US10530923, US10530924
# China Patent: CN102017585  -  Europe Patent: EU2156652  -  Patents Pending

import logging
import unittest
import os

from logging import log
from script_parser import ScriptParser


class TestCompileScripts(unittest.TestCase):
    def test_scripts_compile(self):
        parser = ScriptParser()
        script_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        for file in os.listdir(script_dir):
            log(logging.DEBUG, file)
            if str(file).endswith(".nct"):
                s = parser.parse_script_to_dict(os.path.join(script_dir, file))
                self.assertIsInstance(s, dict)

                self.assertIsInstance(s["formatted_script"], list)
                self.assertIsInstance(s["language"], dict)
                self.assertIsInstance(s["variables"], dict)
                self.assertIsInstance(s["loops"], dict)
                self.assertIsInstance(s["tags"], dict)
                self.assertIsInstance(s["timeout"], int)

                self.assertIn("timeout_action", s)
                if s["timeout_action"]:
                    self.assertIsInstance(s["timeout_action"], str)

                self.assertIsInstance(s["synonyms"], list)
                self.assertIsInstance(s["claps"], dict)
                self.assertIsInstance(s["meta"], dict)

    def test_load_compiled_scripts(self):
        parser = ScriptParser()
        valid_opts = list(parser._pre_parser_options.keys())
        valid_opts.append(None)
        script_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        for file in os.listdir(script_dir):
            log(logging.DEBUG, file)
            if str(file).endswith(".ncs"):
                s = parser.load_script_file(os.path.join(script_dir, file))
                self.assertIsInstance(s[0], list)

                for line in s[0]:
                    self.assertIsInstance(line, dict)

                    self.assertIn("text", line)
                    self.assertIsInstance(line["text"], str)

                    self.assertIn("command", line)
                    self.assertIn(line["command"], valid_opts)

                    self.assertIn("indent", line)
                    self.assertIsInstance(line["indent"], int)

                    self.assertIn("parent_case_indents", line)
                    self.assertIsInstance(line["parent_case_indents"], list)

                    self.assertIsInstance(line.get("data", {}), dict)


if __name__ == '__main__':
    unittest.main()
