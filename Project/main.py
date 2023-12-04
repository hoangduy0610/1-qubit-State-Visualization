import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtWidgets import QInputDialog
from plotter import displayStates
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
            displayStates(states.splitlines())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BlochSphereApp()
    window.show()
    sys.exit(app.exec_())
