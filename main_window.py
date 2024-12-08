import os
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from Iterator import SimpleIterator

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.image_label = QLabel("Image will be here")
        self.annotation_text = QLabel(self)
        self.load_button = QPushButton("Load Dataset", self)
        self.load_button.clicked.connect(self.load_dataset)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.annotation_text)
        layout.addWidget(self.load_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.image_iterator = None

        self.resize(800, 600)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200, 900)

    def load_image(self, image_path: str) -> QPixmap:
        """
        Downloading image
        """
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                print("Error: Can't download image")
                return None
            return pixmap
        else:
            print("Error: Can't find file")
            return None

    def show_image(self, image_path: str, annotation: str) -> None:
        """
        Showing image and annotation
        """
        pixmap = self.load_image(image_path)
        if pixmap:
            scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
            self.annotation_text.setText(annotation)

    def load_dataset(self) -> None:
        """
        Loading Dataset from CSV file
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if file_name:
            self.image_iterator = SimpleIterator(file_name)
            self.load_button.hide()
            self.show_next_image()

    def show_next_image(self) -> None:
        """
        Showing next image
        """
        if self.image_iterator:
            try:
                image_path, annotation = next(self.image_iterator)
                self.show_image(image_path, annotation)
            except StopIteration:
                print("No more images to show")
                self.load_button.show()
            except Exception as e:
                print(f"Error: {e}")    

    def keyPressEvent(self, event) -> None:
        """
        Processing push button event
        """
        if event.key() == Qt.Key_N:
            self.show_next_image()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = MainWindow()
    viewer.show()
    app.exit(app.exec_())
