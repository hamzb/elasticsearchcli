# escli
A command line utility to interact with Elasticsearch
## Requirements
* Python3
* pip3 (Required for installation)
## Supported Environment
* Elasticsearch 6 or higher
* This utility was mostly tested on Linux, but should run on any environment with Python 3
## Installation
* Clone repository: ```git clone https://github.com/hamzb/elasticsearchcli.git```
* Browse to the cloned repository directory: ```cd elasticsearchcli```
* Install the utility with pip3: ```pip3 install .```  

The following packages will also be downloaded as dependancies:
  * elasticsearch
  * argparse

## Usage
```$ escli --help
usage: escli [-h] [--cluster ES_CLUSTER_ADDRESS]
             [--timeout CONNECTION_TIMEOUT]
             {cluster,node,index,snapshot,version} ...

optional arguments:
  -h, --help            show this help message and exit
  --cluster ES_CLUSTER_ADDRESS
                        Specify elasticsearch cluster address using this
                        option, or set the environment variable
                        ES_CLUSTER_ADDRESS
  --timeout CONNECTION_TIMEOUT
                        Connection Timeout

sub-commands:
  {cluster,node,index,snapshot,version}
    cluster             command for cluster level operations
    node                command for node level operations
    index               command for index level operations
    snapshot            command for snapshot level operations
    version             Shows the currently installed version
```
### Version
```
escli version
0.1-alpha
```
### Setting Elasticsearch Connection Endpoint
To define the connection endpoint to your elasticsearch cluster, either use ```--cluster``` option or export the environment variable ```ES_CLUSTER_ADDRESS```. The value should be in the format ```IP|DNS_NAME:PORT```. Example: ```escli --cluster 192.168.1.40:9200```, or ```export ES_CLUSTER_ADDRESS='es_cluster.mydomain.local:9200'```

### Cluster Operations
```
health              Retrieves cluster health
state               Retrieves cluster state
settings            Retrieves cluster settings
set-shard-allocation
                    Sets the shard allocation paramaters. Useful in case
                    of a cluster maintenance to avoid unnecessary shard
                    re-allocations when restarting nodes
reset-shard-allocation
                        Resets the existing "persistent" or "transient" shard
                        allocation paramaters
```
### Node Operations
```
get-master          Shows the master node information
list                Lists cluster nodes
info                Retrieves nodes information
stats               Retrieves nodes stats
usage               Retrieves nodes usage
```
### Index Operations
```
list              Lists the indices
list-shards       Lists the shards and their allocation on nodes
```
### Snapshot Operations
```
list-repos          Lists the snapshots repositories
create-repo         Create a snapshot repository
verify-repo         Verify repository availability on all nodes
delete-repo         Delete repository configuration
list                Lists the snapshots
create              create a snapshot
delete              Delete a snapshot
status              Retrieves the status of a snapshot
restore             Restores a snapshot
```
### Additional Help Information
You can list the help information for the operations/actions with ```--help``` option. Example
```
escli snapshot create --help
usage: escli snapshot create [-h] --repository REPOSITORY --snapshot SNAPSHOT
                             [--indices INDICES]
                             [--ignore-unavailable IGNORE_UNAVAILABLE]
                             [--ignore-global-state INCLUDE_GLOBAL_STATE]
                             [--wait-for-completion WAIT_FOR_COMPLETION]

optional arguments:
  -h, --help            show this help message and exit
  --repository REPOSITORY
                        Snapshots repository
  --snapshot SNAPSHOT   Snapshot name
  --indices INDICES     The list of indices to include in the snapshot.
                        Default is all indices.
  --ignore-unavailable IGNORE_UNAVAILABLE
                        Whether to ignore unavailable indices or throw an
                        exception. Default is False
  --ignore-global-state INCLUDE_GLOBAL_STATE
                        Whether to include the global state in the snapshot.
                        Default is True
  --wait-for-completion WAIT_FOR_COMPLETION
                        Whether to wait for the stapshot completion. Default
                        is False
```
