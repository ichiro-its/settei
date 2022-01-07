from settei_interfaces.srv import GetData

import rclpy
from rclpy.node import Node
from settei import SqliteHandler


class GetDataService(Node):

    def __init__(self):
        super().__init__('get_data_service')
        self.srv = self.create_service(GetData, 'get_data', self.get_data_callback)

    def get_data_callback(self, request, response):
        sqlite_handler = SqliteHandler(':memory:')

        response.json_config = sqlite_handler.load(request.package_name)
        self.get_logger().info('Incoming request for %d config get the data' % (request.package_name))

        return response