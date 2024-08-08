import os
import unittest
from infra.config_provider import ConfigProvider
from infra.jira_handler import JiraHandler


class ForceFailTest(unittest.TestCase):
    """
    this test is intentionally will fail to demonstrate the automatic creating issue in jira,
    when the test fail (Bug was found )
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(base_dir, '../../config.json')
    secret_file_path = os.path.join(base_dir, '../../secret.json')
    config = ConfigProvider().load_from_file(config_file_path)
    secret_file = ConfigProvider().load_from_file(secret_file_path)

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
