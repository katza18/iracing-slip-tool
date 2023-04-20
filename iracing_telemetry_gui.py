import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QFrame, QVBoxLayout, QHBoxLayout, QMainWindow
from PyQt5.QtGui import QIcon

class TelemetryWindow(QMainWindow):
    def __init__(self):
        # Window
        super().__init__()
        self.setWindowTitle('Sim Telemetry Tool')
        self.setGeometry(100, 100, 400, 300)

        # Graph
        graph1 = pg.PlotWidget()
        graph2 = pg.PlotWidget()
        graph3 = pg.PlotWidget()
        graph4 = pg.PlotWidget()
        graph5 = pg.PlotWidget()

        # Labels
        slip_label = QLabel("Slip angle:")
        slip_value = QLabel("0.00º")
        k_label = QLabel("Oversteer/Understeer:")
        k_value = QLabel("0.00")
        wheel_slip_label = QLabel("Wheel Slip:")
        wheel_slip_value = QLabel("0.00")
        brake_label = QLabel("Brake Percent:")
        brake_value = QLabel("0%")
        throttle_label = QLabel("Throttle Percent:")
        throttle_value = QLabel("0%")

        # Grid
        grid = QGridLayout()
        grid.addWidget(graph1, 0, 0, 1, 3)
        grid.addWidget(graph2, 1, 0, 1, 3)
        grid.addWidget(graph3, 2, 0, 1, 3)
        grid.addWidget(graph4, 3, 0, 1, 3)
        grid.addWidget(graph5, 4, 0, 1, 3)
        grid.addWidget(slip_label, 5, 0)
        grid.addWidget(slip_value, 5, 1)
        grid.addWidget(k_label, 6, 0)
        grid.addWidget(k_value, 6, 1)
        grid.addWidget(wheel_slip_label, 7, 0)
        grid.addWidget(wheel_slip_value, 7, 1)
        grid.addWidget(brake_label, 8, 0)
        grid.addWidget(brake_value, 8, 1)
        grid.addWidget(throttle_label, 9, 0)
        grid.addWidget(throttle_value, 9, 1)

        frame = QFrame()
        frame.setLayout(grid)

        self.setCentralWidget(frame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelemetryWindow()
    window.show()
    sys.exit(app.exec_())
