from lib import action
import tower_cli
from tower_cli import get_resource
from tower_cli import conf

class ListJobs(action.AnsibleTowerAction):
    def run(self, job_template):
        with conf.settings.runtime_values(host=self.config['hostname'], username=self.config['username'], password=self.config['password']):
            res = tower_cli.get_resource('job')
            return res.launch(job_template=job_template, monitor=True)
