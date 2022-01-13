# Copyright (c) 2021 ICHIRO ITS
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


from settei_interfaces.srv import SetData

from rclpy.node import Node
from settei import SqliteHandler


class SetDataService(Node):

    def __init__(self):
        super().__init__('update_data_service')
        self.srv = self.create_service(SetData, 'set_data', self.set_data_callback)

    def set_data_callback(self, request, response):
        sqlite_handler = SqliteHandler(':memory:')

        sqlite_handler.save(request.package_name, request.json_config)
        response.status = 'success'

        self.get_logger().info('Incoming request for %s to set data' % (request.package_name))

        return response
