#!/usr/bin/env python

from st2common.runners.base_action import Action
import tower_cli
from tower_cli.conf import settings

class AnsibleTowerAction(Action):

    def __init__(self, config):
        super(AnsibleTowerAction, self).__init__(config)

    def _get_client(self):
        hostname = self.config['hostname']
        username = self.config['username']
        password = self.config['password']

        client = tower_cli.conf.settings.runtime_values(hostname, username, password)
        return client
