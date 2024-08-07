from jira import JIRA
from infra.config_provider import ConfigProvider


class JiraHandler:
    config = ConfigProvider().load_from_file('../config.json')
    secret_file = ConfigProvider().load_from_file('../secret.json')

    def __init__(self):
        self._jira_url = self.config['jira_url']
        self._auth_jira = JIRA(
            basic_auth=(self.config['email'], self.secret_file['jira_token']),
            options={'server': self._jira_url}
        )

    def create_issue(self, project_key, summary, description, issue_type='Bug'):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': issue_type
        }
        return self._auth_jira.create_issue(fields=issue_dict)