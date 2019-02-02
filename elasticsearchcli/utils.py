import json

escli_version = "0.1-alpha"

def get_version(args):
    print(escli_version)

def get_cluster_health(args):
    if args.cluster_index:
        args.cluster_index = args.cluster_index.replace(' ', '')
    print(json.dumps(args.es_connection.cluster.health(
        level=args.cluster_health_level, 
        index=args.cluster_index, 
        wait_for_status=args.wait_for_status), 
        indent=2)
    )

def get_cluster_state(args):
    print(json.dumps(args.es_connection.cluster.state(), indent=2))

def get_node_info(args):
    if args.node_id:
        args.node_id = args.node_id.replace(' ', '')
    print(json.dumps(args.es_connection.nodes.info(node_id=args.node_id, metric=args.metrics), indent=2))

def get_node_stats(args):
    if args.node_id:
        args.node_id = args.node_id.replace(' ', '')
    print(json.dumps(args.es_connection.nodes.stats(node_id=args.node_id, metric=args.metrics, level=args.level), indent=2))

def get_node_usage(args):
    if args.node_id:
        args.node_id = args.node_id.replace(' ', '')
    print(json.dumps(args.es_connection.nodes.usage(node_id=args.node_id), indent=2))
    
def get_master_node(args):
    print(json.dumps(args.es_connection.cat.master(format='json'), indent=2))

def list_nodes(args):
    print(json.dumps(args.es_connection.cat.nodes(format='json'), indent=2))

def list_index(args):
    if args.index_id:
        args.index_id = args.index_id.replace(' ', '')
    print(json.dumps(args.es_connection.cat.indices(index=args.index_id, health=args.index_health, format='json'), indent=2))

def list_shards(args):
    if args.index_id:
        args.index_id = args.index_id.replace(' ', '')
    print(json.dumps(args.es_connection.cat.shards(index=args.index_id, format='json'), indent=2))

def list_snapshots(args):
    print(json.dumps(args.es_connection.snapshot.get(), indent=2))

def list_repos(args):
    print(json.dumps(args.es_connection.snapshot.get_repository(), indent=2))