import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtWidgets import QInputDialog
from plotter import displayStates
from animate import Visualization
import numpy as np

class BlochSphereApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bloch Sphere App")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.label = QLabel("Select a text file or enter a list of 1-qubit quantum states:")
        self.layout.addWidget(self.label)

        self.fileButton = QPushButton("Choose File")
        self.fileButton.clicked.connect(self.openFile)
        self.layout.addWidget(self.fileButton)

        self.stateButton = QPushButton("Enter States")
        self.stateButton.clicked.connect(self.enterStates)
        self.layout.addWidget(self.stateButton)
        
        self.visualization = QPushButton("Visualization Transition")
        self.visualization.clicked.connect(self.enterInitialAndTargetState)
        self.layout.addWidget(self.visualization)
        
    def enterInitialAndTargetState(self):
        InitialState, _ = QInputDialog.getText(self, "Visualization Transition", "Enter Initial State") 
        TargetState, _ = QInputDialog.getText(self, "Visualization Transition", "Enter Target State")
        
        State = InitialState.split(' ')
        initial_state = [float(string) for string in State]
        initial_state = np.array(initial_state)

        State = TargetState.split(' ')
        target_state = [float(string) for string in State]
        target_state = np.array(target_state)
        
        print(initial_state, target_state)
        
        Visualization(initial_state, target_state)
        
    def openFile(self):
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        fileName, _ = fileDialog.getOpenFileName(self, "Choose a text file")
        if fileName:
            with open(fileName, 'r') as file:
                states = file.readlines()
                displayStates(states)

    def enterStates(self):
        states, _ = QInputDialog.getText(self, "Enter States", "Enter a list of 1-qubit quantum states (comma-separated):")
        if states:
            array = [state.strip() for state in states.split(',')]
            displayStates(array)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BlochSphereApp()
    window.show()
    sys.exit(app.exec_())
