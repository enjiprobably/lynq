"""
This file is part of Lynq (elemenom/lynq).

Lynq is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lynq is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Lynq. If not, see <https://www.gnu.org/licenses/>.
"""

from lynq.server import LynqServer
from lynq._backendutils.dependencies.basin.object import BasinObject
from lynq._backendutils.dependencies.basin.getval import getval

class BasinLynqServer(LynqServer):
    def __init__(self, name: str) -> None:
        from lynq.launcher import launch

        basin: BasinObject = BasinObject(name)

        super().__init__(
            port=getval("port", basin, 8000),
            directory=getval("directory", basin, "./")
        )