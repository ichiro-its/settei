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


from sqlite3 import Connection, Cursor, Row, connect


class SqliteHandler():
    def __init__(self, database: str):
        self.connection: Connection = connect(database)
        self.connection.row_factory = Row
        self.cursor: Cursor = self.connection.cursor()

    def load(self, table: str) -> str:
        self.cursor.execute(f'SELECT json FROM {table} ORDER BY id DESC LIMIT 1')

        return self.cursor.fetchone()['json']

    def save(self, table: str, package: str, robot: str, branch: str, filename: str, json:str) -> None:
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table} (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                package TEXT NOT NULL,
                                robot TEXT NOT NULL,
                                branch TEXT NOT NULL,
                                filename TEXT NOT NULL,
                                json TEXT NOT NULL,
                                datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        self.cursor.execute(f'''INSERT INTO {table} (package, robot, branch, filename, json)
                                VALUES('{package}', '{robot}', '{branch}', '{filename}', '{json}')''')

        self.connection.commit()
