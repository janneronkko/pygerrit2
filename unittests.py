#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The MIT License
#
# Copyright 2012 Sony Mobile Communications. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

""" Unit tests for pygerrit. """

import unittest

from setup import REQUIRES as setup_requires


class TestConsistentDependencies(unittest.TestCase):

    """ Verify that dependency package versions are consistent. """

    def test_dependencies(self):
        requirements_txt = {}
        setup_py = {}

        for package in open("requirements.txt").read().strip().splitlines():
            name, version = package.split('==')
            requirements_txt[name] = version

        for package in setup_requires:
            name, version = package.split('==')
            setup_py[name] = version

        self.assertEquals(requirements_txt, setup_py,
                          "Inconsistency between dependency package versions "
                          "listed in requirements.txt and setup.py")


if __name__ == '__main__':
    unittest.main()
