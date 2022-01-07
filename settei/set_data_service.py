from settei_interfaces.srv import SetData

import rclpy
from rclpy.node import Node
from settei import SqliteHandler


class SetDataService(Node):

    def __init__(self):
        super().__init__('update_data_service')
        self.srv = self.create_service(SetData, 'set_data', self.set_data_callback)

    def set_data_callback(self, request, response):
        sqlite_handler = SqliteHandler(':memory:')

        sqlite_handler.save(request.package_name, request.json_config)

        self.get_logger().info('Incoming request for %d config to set the data' % (request.package_name))

        return response