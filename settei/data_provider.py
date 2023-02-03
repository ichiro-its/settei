# Copyright (c) 2023 Ichiro ITS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from .sqlite_handler import SqliteHandler
import rclpy
from rclpy.node import Node
from settei_interfaces.srv import GetData
from settei_interfaces.srv import SetData

class DataProvider (Node):
    def __init__(self, node_name: str):
        super().__init__(node_name)

        self.handler = SqliteHandler("settei")

        self.set_data_srv = self.create_service(SetData, 'set_data', self.set_data_callback)
        self.get_data_srv = self.create_service(GetData, 'get_data', self.get_data_callback)

    def get_data_callback(self, request, response):
        response.json_config = self.handler.load("config", request.package_name, request.robot_name, request.branch, request.file_name)
        
        return response

    def set_data_callback(self, request, response):
        self.handler.save("config", request.package_name, request.robot_name, request.branch, request.file_name, request.json_config)
        
        return response

def main(args=None):
    try:
        rclpy.init(args=args)
        data_provider = DataProvider("settei")

        rclpy.spin(data_provider)

        data_provider.destroy_node()
        rclpy.shutdown()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
