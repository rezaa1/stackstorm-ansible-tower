from lib import action
import tower_cli
from tower_cli import get_resource
from tower_cli import conf

class CreateInventory(action.AnsibleTowerAction):
    def run(self, inventory_name, organization):
        with conf.settings.runtime_values(host=self.config['hostname'], username=self.config['username'], password=self.config['password']):
            response = tower_cli.get_resource('organization')
            org = response.get(name=organization)
            res = tower_cli.get_resource('inventory')
            return res.create(name=inventory_name, organization=org['id'])
