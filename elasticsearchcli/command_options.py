from elasticsearchcli.utils import *

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
                        'help': 'Limit the results to the specified nodes'
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
                        'help': 'Limit the results to the specified nodes'
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
                'help': 'Retrieves node usage',
                'function': get_node_usage,
                'arguments': {
                    'node-id': {
                        'name': '--node-id',
                        'dest': 'node_id',
                        'required': False,
                        'default': None,
                        'help': 'Limit the results to the specified nodes'
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
        'help': 'command for snapshot level operations',
        'title': 'snapshot operations subcommands',
        'subcommands': {
            'list-repos': {
                'help': 'Lists the snapshots repositories',
                'function': list_repos,
                'arguments':{}
            },
            'create-repo': {
                'help': 'Create a snapshot repository',
                'function': create_repo,
                'arguments':{
                    'repository': {
                        'name': '--repository',
                        'dest': 'repository',
                        'required': True,
                        'default': None,
                        'help': 'Repository name'
                    },
                    'repo-config-file': {
                        'name': '--repository-config-file',
                        'dest': 'config_file_path',
                        'required': True,
                        'default': None,
                        'help': 'Repository settings in json format'
                    }
                }
            },
            'verify-repo': {
                'help': 'Verify repository availability on all nodes',
                'function': verify_repo,
                'arguments':{
                    'repository': {
                        'name': '--repository',
                        'dest': 'repository',
                        'required': True,
                        'default': None,
                        'help': 'Repository name'
                    }
                }
            },
            'delete-repo': {
                'help': 'Delete repository configuration',
                'function': delete_repo,
                'arguments':{
                    'repository': {
                        'name': '--repository',
                        'dest': 'repository',
                        'required': True,
                        'default': None,
                        'help': 'Repository name'
                    }
                }
            },
            'list': {
                'help': 'Lists the snapshots',
                'function': list_snapshots,
                'arguments':{
                    'repository': {
                        'name': '--repository',
                        'dest': 'repository',
                        'required': True,
                        'default': None,
                        'help': 'Snapshots repository'
                    },
                    'snapshot': {
                        'name': '--snapshot',
                        'dest': 'snapshot',
                        'required': False,
                        'default': '_all',
                        'help': 'A comma-separated list of snapshot names'
                    },
                    'ignore_unavailable': {
                        'name': '--ignore-unavailable',
                        'dest': 'ignore_unavailable',
                        'required': False,
                        'default': False,
                        'help': 'Whether to ignore unavailable snapshots or throw an exception for them. Default is False.'
                    }
                }
            },
            'create': {
                'help': 'create a snapshot',
                'function': create_snapshot,
                'arguments':{
                    'repository': {
                        'name': '--repository',
                        'dest': 'repository',
                        'required': True,
                        'default': None,
                        'help': 'Snapshots repository'
                    },
                    'snapshot': {
                        'name': '--snapshot',
                        'dest': 'snapshot',
                        'required': True,
                        'default': None,
                        'help': 'Snapshot name'
                    },
                    'indices': {
                        'name': '--indices',
                        'dest': 'indices',
                        'required': False,
                        'default': '_all',
                        'help': 'The list of indices to include in the snapshot. Default is all indices.'
                    },
                    'ignore_unavailable': {
                        'name': '--ignore-unavailable',
                        'dest': 'ignore_unavailable',
                        'required': False,
                        'default': False,
                        'help': 'Whether to ignore unavailable indices or throw an exception. Default is False'
                    },
                    'include_global_state': {
                        'name': '--ignore-global-state',
                        'dest': 'include_global_state',
                        'required': False,
                        'default': True,
                        'help': 'Whether to include the global state in the snapshot. Default is True'
                    },
                    'wait_for_completion': {
                        'name': '--wait-for-completion',
                        'dest': 'wait_for_completion',
                        'required': False,
                        'default': False,
                        'help': 'Whether to wait for the stapshot completion. Default is False'
                    },
                }
            },
            'delete': {
                'help': 'Delete a snapshot',
                'function': delete_snapshot,
                'arguments':{
                    'repository': {
                        'name': '--repository',
                        'dest': 'repository',
                        'required': True,
                        'default': None,
                        'help': 'Snapshots repository'
                    },
                    'snapshot': {
                        'name': '--snapshot',
                        'dest': 'snapshot',
                        'required': True,
                        'default': None,
                        'help': 'A comma-separated list of snapshot names'
                    }
                }
            },
            'status': {
                'help': 'Retrieves the status of a snapshot',
                'function': snapshot_status,
                'arguments':{
                    'repository': {
                        'name': '--repository',
                        'dest': 'repository',
                        'required': True,
                        'default': None,
                        'help': 'Snapshots repository'
                    },
                    'snapshot': {
                        'name': '--snapshot',
                        'dest': 'snapshot',
                        'required': True,
                        'default': None,
                        'help': 'A comma-separated list of snapshot names'
                    }
                }
            },
            'restore': {
                'help': 'Restores a snapshot',
                'function': restore_snapshot,
                'arguments':{
                    'repository': {
                        'name': '--repository',
                        'dest': 'repository',
                        'required': True,
                        'default': None,
                        'help': 'Snapshots repository'
                    },
                    'snapshot': {
                        'name': '--snapshot',
                        'dest': 'snapshot',
                        'required': True,
                        'default': None,
                        'help': 'A comma-separated list of snapshot names'
                    },
                    'indices': {
                        'name': '--indices',
                        'dest': 'indices',
                        'required': False,
                        'default': '_all',
                        'help': 'The list of indices to restore. Default is all indices.'
                    },
                    'ignore_unavailable': {
                        'name': '--ignore-unavailable',
                        'dest': 'ignore_unavailable',
                        'required': False,
                        'default': True,
                        'help': 'Whether to ignore unavailable indices or throw an exception. Default is True'
                    },
                    'include_global_state': {
                        'name': '--ignore-global-state',
                        'dest': 'include_global_state',
                        'required': False,
                        'default': False,
                        'help': 'Whether to include the global state in the snapshot. Default is False'
                    },
                    'wait_for_completion': {
                        'name': '--wait-for-completion',
                        'dest': 'wait_for_completion',
                        'required': False,
                        'default': False,
                        'help': 'Whether to wait for the restore completion. Default is False'
                    }
                }
            },
        }
    },
}
