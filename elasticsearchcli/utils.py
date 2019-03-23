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

def get_cluster_settings(args):
    print(json.dumps(args.es_connection.cluster.get_settings(include_defaults=args.include_defaults, flat_settings=args.flat_settings), indent=2))

def set_shard_allocation(args):
    try:
        assert(args.update_mode in ['persistent', 'transient'])
        assert(args.shard_allocation_mode in ['all', 'primaries', 'new_primaries', 'none'])
    except AssertionError:
        print("Error - Incorrect settings\n--update-mode should be (persistent|transient)\n--shard-allocation-mode should be (all|primaries|new_primaries|none)")
        exit(1)
    data = {args.update_mode: {"cluster.routing.allocation.enable": args.shard_allocation_mode}}
    json_data = json.dumps(data)
    print(json_data)
    print(json.dumps(args.es_connection.cluster.put_settings(flat_settings=True, body=json_data), indent=2))

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

def list_repos(args):
    print(json.dumps(args.es_connection.snapshot.get_repository(), indent=2))

def list_snapshots(args):
    if args.snapshot:
        args.snapshot = args.snapshot.replace(' ', '')
    print(json.dumps(args.es_connection.snapshot.get(repository=args.repository, snapshot=args.snapshot, ignore_unavailable=args.ignore_unavailable), indent=2))

def create_repo(args):
    with open(args.config_file_path) as config_file:  
        repo_config = json.load(config_file)
    print(json.dumps(args.es_connection.snapshot.create_repository(repository=args.repository, body=repo_config), indent=2))

def create_snapshot(args):
    if args.indices:
        args.indices = args.indices.replace(' ', '')
    snapshot_body = {"indices": args.indices, "ignore_unavailable": args.ignore_unavailable, "include_global_state": args.include_global_state}
    snapshot_body_json = json.dumps(snapshot_body)
    print(json.dumps(args.es_connection.snapshot.create(
        repository=args.repository, 
        snapshot=args.snapshot,
        body=snapshot_body_json,
        wait_for_completion=args.wait_for_completion), indent=2))

def delete_snapshot(args):
    print(json.dumps(args.es_connection.snapshot.delete(repository=args.repository, snapshot=args.snapshot), indent=2))

def restore_snapshot(args):
    if args.indices:
        args.indices = args.indices.replace(' ', '')
    snapshot_body = {"indices": args.indices, "ignore_unavailable": args.ignore_unavailable, "include_global_state": args.include_global_state}
    snapshot_body_json = json.dumps(snapshot_body)
    print(json.dumps(args.es_connection.snapshot.restore(
        repository=args.repository, 
        snapshot=args.snapshot,
        body=snapshot_body_json,
        wait_for_completion=args.wait_for_completion), indent=2))

def snapshot_status(args):
    print(json.dumps(args.es_connection.snapshot.status(repository=args.repository, snapshot=args.snapshot), indent=2))

def verify_repo(args):
    print(json.dumps(args.es_connection.snapshot.verify_repository(repository=args.repository), indent=2))

def delete_repo(args):
    args.repository = args.repository.replace(' ', '')
    print(json.dumps(args.es_connection.snapshot.delete_repository(repository=args.repository), indent=2))