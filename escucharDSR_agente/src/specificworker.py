#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2024 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication
from rich.console import Console
from genericworker import *
import interfaces as ifaces

sys.path.append('/opt/robocomp/lib')
console = Console(highlight=False)

from pydsr import *


# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel


class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map, startup_check=False):
        super(SpecificWorker, self).__init__(proxy_map)
        self.Period = 2000

        # YOU MUST SET AN UNIQUE ID FOR THIS AGENT IN YOUR DEPLOYMENT. "_CHANGE_THIS_ID_" for a valid unique integer
        self.agent_id = 299
        self.g = DSRGraph(0, "pythonAgent", self.agent_id)

        try:
            signals.connect(self.g, signals.UPDATE_NODE_ATTR, self.update_node_att)
            signals.connect(self.g, signals.UPDATE_NODE, self.update_node)
            signals.connect(self.g, signals.DELETE_NODE, self.delete_node)
            signals.connect(self.g, signals.UPDATE_EDGE, self.update_edge)
            signals.connect(self.g, signals.UPDATE_EDGE_ATTR, self.update_edge_att)
            signals.connect(self.g, signals.DELETE_EDGE, self.delete_edge)
            console.print("signals connected")
        except RuntimeError as e:
            print(e)

        if startup_check:
            self.startup_check()
        else:
            self.timer.timeout.connect(self.compute)
            self.timer.start(self.Period)

        #se obtiene el nombre de los distintos nodos que están presentes en el dsr


        self.lista_nodos_ambiental = self.g.get_nodes_by_type("ambiental")
        self.lista_nodos_sonido = self.g.get_nodes_by_type("sound")
        self.nodos_ambiental=[]
        self.nodos_sonido = []


        for node in self.lista_nodos_sonido:
            self.nodos_sonido.append(node.name)


        for node in self.lista_nodos_ambiental:
            self.nodos_ambiental.append(node.name)

        print(self.nodos_ambiental)
        print(self.nodos_sonido)

    def __del__(self):
        """Destructor"""

    def setParams(self, params):
        # try:
        #	self.innermodel = InnerModel(params["InnerModelPath"])
        # except:
        #	traceback.print_exc()
        #	print("Error reading config params")
        return True


    @QtCore.Slot()
    def compute(self):
        print('SpecificWorker.compute...')
        # for i in self.lista_nodos:
        #     self.valor_temperatura= i.attrs["temperature"].value
        #     self.valor_humidity= i.attrs["humidity"].value
        #     self.valor_illumination= i.attrs["illumination"].value
        #
        #     print(i.name)

        return True

    def startup_check(self):
        QTimer.singleShot(200, QApplication.instance().quit)





    # def nombre_nodos(self):


    # =============== DSR SLOTS  ================
    # =============================================

    def update_node_att(self, id: int, attribute_names: [str]):
        # console.print(f"UPDATE NODE ATT: {id} {attribute_names}", style='green')
        pass
    def update_node(self, id: int, type: str):
        # console.print(f"UPDATE NODE: {id} {type}", style='green')
        pass
    def delete_node(self, id: int):
        # console.print(f"DELETE NODE:: {id} ", style='green')
        pass
    def update_edge(self, fr: int, to: int, type: str):

        # console.print(f"UPDATE EDGE: {fr} to {type}", type, style='green')
        pass
    def update_edge_att(self, fr: int, to: int, type: str, attribute_names: [str]):
        # console.print(f"UPDATE EDGE ATT: {fr} to {type} {attribute_names}", style='green')
        pass
    def delete_edge(self, fr: int, to: int, type: str):
        # console.print(f"DELETE EDGE: {fr} to {type} {type}", style='green')
        pass
