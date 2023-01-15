from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *  

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl

import numpy as np
import trimesh
from  scipy.spatial.transform import Rotation as rotate


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 700, 900) 
        self.initUI()

    
    def initUI(self):
        centerWidget = QWidget()
        self.setCentralWidget(centerWidget)
        layout = QVBoxLayout()

        self.viewer = gl.GLViewWidget()
        layout.addWidget(self.viewer, 1)

        self.viewer.setWindowTitle('STL Viewer')
        self.viewer.setCameraPosition(distance=40)

        g = gl.GLGridItem()
        g.setSize(200, 200)
        g.setSpacing(5, 5)
        self.viewer.addItem(g)

        mesh_data = self.loadModel()

        mesh = gl.GLMeshItem()
        mesh.setMeshData(vertexes=mesh_data.vertices, faces=mesh_data.faces, shader="balloon", color=(1, 0, 0, 0.2))
        mesh.setGLOptions("additive")
        '''
        balloon
        heightColor
        shaded
        edgeHilight
        normalColor
        viewNormalColor
        heightColor
        pointSprite
        '''
        # mesh.setColor(QColor(255, 0, 0, 10))
        mesh.setColor((1, 0, 0, 0.09))
        # mesh.shader.

        self.viewer.addItem(mesh)

        transform_matrix = np.array([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, -1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]],
            dtype=np.float64)

        mesh.setTransform(pg.Transform3D(transform_matrix))




        centerWidget.setLayout(layout)

    def loadModel(self):
        mesh_data = trimesh.load_mesh('./assets/FinalBaseMesh.obj')
        
        return mesh_data


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()