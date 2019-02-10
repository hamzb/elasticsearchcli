from elasticsearch import Elasticsearch
import argparse
import os
from elasticsearchcli.command_options import *

def main():
    env_cluster_address = os.environ.get('ES_CLUSTER_ADDRESS')

    # Define main parser and sub-parser for main commands
    parser = argparse.ArgumentParser()
    parser.add_argument('--cluster', dest='es_cluster_address', required=False, default=env_cluster_address, help='Specify elasticsearch cluster address using this option, or set the environment variable ES_CLUSTER_ADDRESS')
    main_subparser = parser.add_subparsers(title='sub-commands', dest='sub-commands')
    main_subparser.required = True

    # Looping over the commands and arguments dict and adding them to the parser
    # Adding the first level of commands
    for first_sub_command in cmd_options:
        first_cmd = main_subparser.add_parser(first_sub_command, help=cmd_options[first_sub_command]['help'])
        first_cmd_parser = first_cmd.add_subparsers(title=cmd_options[first_sub_command]['title'], dest=cmd_options[first_sub_command]['title'])
        first_cmd_parser.required = True
        # Adding the second level of commands
        for second_sub_command in cmd_options[first_sub_command]['subcommands']:
            second_cmd = first_cmd_parser.add_parser(second_sub_command, help=cmd_options[first_sub_command]['subcommands'][second_sub_command]['help'])
            second_cmd.set_defaults(func=cmd_options[first_sub_command]['subcommands'][second_sub_command]['function'])
            # Adding the arguments for each sub-command
            for arg in cmd_options[first_sub_command]['subcommands'][second_sub_command]['arguments']:
                second_cmd.add_argument(
                    cmd_options[first_sub_command]['subcommands'][second_sub_command]['arguments'][arg]['name'],
                    dest = cmd_options[first_sub_command]['subcommands'][second_sub_command]['arguments'][arg]['dest'],
                    required = cmd_options[first_sub_command]['subcommands'][second_sub_command]['arguments'][arg]['required'],
                    default = cmd_options[first_sub_command]['subcommands'][second_sub_command]['arguments'][arg]['default'],
                    help = cmd_options[first_sub_command]['subcommands'][second_sub_command]['arguments'][arg]['help'],
                )
                
    version_cmd = main_subparser.add_parser('version', help='Shows the currently installed version')
    version_cmd.set_defaults(func=get_version)

    args = parser.parse_args()
    if vars(args)['sub-commands'].lower() != 'version':
        try:
            assert(args.es_cluster_address)
        except AssertionError:
            print("Eleasticsearch address was not found. Make sure to pass with '--cluster' option or to set the environment variable 'ES_CLUSTER_ADDRESS'")
            exit(1)
        else:
            es_connection = Elasticsearch([args.es_cluster_address])
            args.es_connection = es_connection

    args.func(args)