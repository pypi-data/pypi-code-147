#!/usr/bin/env python

"""Tests for `async_download` package."""


import unittest

from click.testing import CliRunner

from async_download import cli


class TestAsync_download(unittest.TestCase):
    """Tests for `async_download` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code != 0
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
