import os
import unittest
from infra.config_provider import ConfigProvider
from infra.jira_handler import JiraHandler


class ForceFailTest(unittest.TestCase):
    """
    this test is intentionally will fail to demonstrate the automatic creating issue in jira,
    when the test fail (Bug was found )
    """
    config = ConfigProvider().load_from_file('../../config.json', __file__)
    secret = ConfigProvider().load_from_file('../../secret.json', __file__)

    def setUp(self):
        self.error = None

    def tearDown(self):
        if self.error:
            JiraHandler().create_issue(self.config['project_key'], self._testMethodName, self.error)

    def test_jira_create_issue(self):
        try:
            self.assertEqual(1, 2)
        except AssertionError as e:
            self.error = f"an error occurred :{e}"
