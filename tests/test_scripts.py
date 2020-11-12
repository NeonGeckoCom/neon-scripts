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
            if file.endswith(".nct"):
                print(file)
                s = parser.parse_script_to_dict(os.path.join(script_dir, file))
                self.assertIsInstance(s, dict)


if __name__ == '__main__':
    unittest.main()
