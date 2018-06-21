from flask_restful import Resource, reqparse

create_parser = reqparse.RequestParser()
create_parser.add_argument('name', type=str, required=True)
create_parser.add_argument('image', type=str, store_missing=False)
create_parser.add_argument('flavor', type=str, store_missing=False)
create_parser.add_argument('auto_ip', type=bool, store_missing=False)
create_parser.add_argument('ips', type=list, store_missing=False)
create_parser.add_argument('ip_pool', type=str, store_missing=False)
create_parser.add_argument('boot_volume', type=str, store_missing=False)
create_parser.add_argument('terminate_volume', type=bool, store_missing=False)
create_parser.add_argument('volumes', type=list, store_missing=False)
create_parser.add_argument('meta', type=dict, store_missing=False)
create_parser.add_argument('reservation_id', type=str, store_missing=False)
create_parser.add_argument('min_count', type=int, store_missing=False)
create_parser.add_argument('max_count', type=int, store_missing=False)
create_parser.add_argument('security_groups', type=list, store_missing=False)
create_parser.add_argument('userdata', type=str, store_missing=False)
create_parser.add_argument('key_name', type=str, store_missing=False)
create_parser.add_argument('availability_zone', type=str, store_missing=False)
create_parser.add_argument('block_device_mapping', type=dict, store_missing=False)
create_parser.add_argument('block_device_mapping_v2', type=dict, store_missing=False)
create_parser.add_argument('nics', type=list, store_missing=False)
create_parser.add_argument('scheduler_hints', type=dict, store_missing=False)
create_parser.add_argument('config_drive', store_missing=False)
create_parser.add_argument('disk_config', store_missing=False)
create_parser.add_argument('admin_pass', store_missing=False)
create_parser.add_argument('wait', store_missing=False)
create_parser.add_argument('timeout', store_missing=False)
create_parser.add_argument('reuse_ips', store_missing=False)
create_parser.add_argument('network', store_missing=False)
create_parser.add_argument('boot_from_volume', store_missing=False)
create_parser.add_argument('volume_size', store_missing=False)
create_parser.add_argument('nat_destination', store_missing=False)
create_parser.add_argument('group', store_missing=False)

class ServerList(Resource):
    def __init__(self, **kwargs):
        self.openstack_connection = kwargs['openstack_connection']

    def get(self):
        return self.openstack_connection.list_servers()

    def post(self):
        create_kwargs = create_parser.parse_args()
        return self.openstack_connection.create_server(**create_kwargs)
