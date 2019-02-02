from utils import *

# Defining dictionary to contain the commands, sub-commands and arguments
cmd_options = {
    'cluster': {
        'help': 'command for cluster level operations',
        'title': 'cluster operations subcommands',
        'subcommands': {
            'health': {
                'help': 'Retrieves cluster health',
                'function': get_cluster_health,
                'arguments': {
                    'level': {
                        'name': '--level',
                        'dest': 'cluster_health_level',
                        'required': False,
                        'default': 'cluster',
                        'help': 'Cluster health details level. Could be "cluster", "indices" or "shards"'
                    },
                    'index': {
                        'name': '--index',
                        'dest': 'cluster_index',
                        'required': False,
                        'default': None,
                        'help': 'Limit health information to the specified index'
                    },
                    'wait-for-status': {
                        'name': '--wait-for-status',
                        'dest': 'wait_for_status',
                        'required': False,
                        'default': None,
                        'help': 'Wait for the cluster to reach a specific status. Could be "green", "yellow" or "red"'
                    }
                }
            },
            'state': {
                'help': 'Retrieves cluster state',
                'function': get_cluster_state,
                'arguments':{}
            }
        }
    },
    'node': {
        'help': 'command for node level operations',
        'title': 'node operations subcommands',
        'subcommands': {
            'get-master': {
                'help': 'Shows the master node information',
                'function': get_master_node,
                'arguments': {}
            },
            'list': {
                'help': 'Lists cluster nodes',
                'function': list_nodes,
                'arguments': {}
            },
            'info': {
                'help': 'Retrieves node information',
                'function': get_node_info,
                'arguments': {
                    'node-id': {
                        'name': '--node-id',
                        'dest': 'node_id',
                        'required': False,
                        'default': None,
                        'help': 'Limit the results to the specified node'
                    },
                    'metrics': {
                        'name': '--metrics',
                        'dest': 'metrics',
                        'required': False,
                        'default': None,
                        'help': 'Limit the results to the specified metrics'
                    }
                }
            },
            'stats': {
                'help': 'Retrieves node stats',
                'function': get_node_stats,
                'arguments': {
                    'node-id': {
                        'name': '--node-id',
                        'dest': 'node_id',
                        'required': False,
                        'default': None,
                        'help': 'Limit the results to the specified node'
                    },
                    'metrics': {
                        'name': '--metrics',
                        'dest': 'metrics',
                        'required': False,
                        'default': None,
                        'help': 'Limit the results to the specified metrics'
                    },
                    'level': {
                        'name': '--level',
                        'dest': 'level',
                        'required': False,
                        'default': None,
                        'help': "Return indices stats aggregated at index, node or shard level, valid choices are: 'indices', 'node', 'shards'"
                    },
                }
            },
            'usage': {
                'help': 'Retrieves node uage',
                'function': get_node_usage,
                'arguments': {
                    'node-id': {
                        'name': '--node-id',
                        'dest': 'node_id',
                        'required': False,
                        'default': None,
                        'help': 'Limit the results to the specified node'
                    },
                }
            }
        }
    },
    'index': {
        'help': 'command for index level operations',
        'title': 'index operations subcommands',
        'subcommands': {
            'list': {
                'help': 'Lists the indices',
                'function': list_index,
                'arguments': {
                   'index-id': {
                        'name': '--index-id',
                        'dest': 'index_id',
                        'required': False,
                        'default': None,
                        'help': 'A comma-separated list of index names to limit the returned information'
                    },
                    'index-health': {
                        'name': '--health',
                        'dest': 'index_health',
                        'required': False,
                        'default': None,
                        'help': "Filter only indices matching the specified health status, valid choices are 'green', 'yellow', 'red'"
                    }
                }
            },
            'list-shards': {
                'help': 'Lists the shards',
                'function': list_shards,
                'arguments': {
                    'index-id': {
                        'name': '--index-id',
                        'dest': 'index_id',
                        'required': False,
                        'default': None,
                        'help': 'A comma-separated list of index names to limit the returned information'
                    }
                }
            }
        }
    },
    'snapshot': {
        'help': 'command for index level operations',
        'title': 'index operations subcommands',
        'subcommands': {
            'list': {
                'help': 'Lists the snapshots',
                'function': list_snapshots,
                'arguments':{}
            },
            'list-repos': {
                'help': 'Lists the snapshots repositories',
                'function': list_repos,
                'arguments':{}
            }
        }
    }
}
