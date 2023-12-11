import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QInputDialog
from plotter import display_states
from PyQt5.QtGui import QFont

class BlochSphereApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1-Qubit States Visualization")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.label = QLabel("Select a feature from the list below")
        self.layout.addWidget(self.label)

        self.fileButton = QPushButton("Choose File")
        self.fileButton.clicked.connect(self.open_file)
        self.layout.addWidget(self.fileButton)

        self.stateButton = QPushButton("Enter States")
        self.stateButton.clicked.connect(self.enter_states)
        self.layout.addWidget(self.stateButton)
        
        self.visualization = QPushButton("Visualization Transition")
        self.visualization.clicked.connect(self.visualization_transition)
        self.layout.addWidget(self.visualization)
        

    # ==================================================================================================
    # ACTIONS    
    def visualization_transition(self):
        InitialState, _ = QInputDialog.getText(self, "Visualization Transition", "Enter Initial State") 
        TargetState, _ = QInputDialog.getText(self, "Visualization Transition", "Enter Target State")
        
        command = f"python qubit_animation.py \"{InitialState}\" \"{TargetState}\""
        subprocess.run(command, shell=True)
        
    def open_file(self):
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        fileName, _ = fileDialog.getOpenFileName(self, "Choose a text file")
        if fileName:
            with open(fileName, 'r') as file:
                states = file.readlines()
                display_states(states)

    def enter_states(self):
        states, _ = QInputDialog.getMultiLineText(self, "Enter States", "Enter a list of 1-qubit quantum states:")
        if states:
            array = [state.strip() for state in states.split('\n')]
            display_states(array)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("*{font-size: 20pt;}")
    window = BlochSphereApp()
    window.show()
    sys.exit(app.exec_())
