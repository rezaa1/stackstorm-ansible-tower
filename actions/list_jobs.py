from lib import action
import tower_cli
from tower_cli import get_resource
from tower_cli import conf

class ListJobs(action.AnsibleTowerAction):
    def run(self):
        with conf.settings.runtime_values(host=self.config['hostname'], username=self.config['username'], password=self.config['password']):
            res = tower_cli.get_resource('job')
            results = res.list(all_pages=True)
            return results
