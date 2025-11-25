# Import necessary libraries
from PyQt6 import QtWidgets, uic, QtGui, QtCore
from PyQt6.QtWidgets import QDialog, QMessageBox
from datetime import date
import sys

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the .ui file here
        # Example:
        uic.loadUi('LibManagementSys.ui', self)

        # --- Setup UI defaults here ---
        # Example:
        self.IssuedBy.setEnabled(False)
        self.IssuedOn.setEnabled(False)

        # --- Connect widgets to functions ---
        # Example: checkbox, buttons, dropdown changes
        self.Issued.stateChanged.connect(self.handle_click)
        self.comboBox.currentIndexChanged.connect(self.index_changed)
        self.pushButton.clicked.connect(self.authorChange)
        self.OkayButton.clicked.connect(self.validateForm)
        # --- Show the GUI ---
        self.show()

    # Function to handle checkbox toggle for Issued/Not Issued
    def handle_click(self, state):
        """
        Enable or disable the 'Issued By' and 'Issued On' fields
        depending on whether the checkbox is checked.
        """
        # self.IssuedBy.setEnabled(True)
        if self.Issued.isChecked():
            self.IssuedBy.setEnabled(True)
            self.IssuedOn.setEnabled(True)
        else:
            self.IssuedBy.setEnabled(False)
            self.IssuedOn.setEnabled(False)

    # Function to update subcategories based on selected category
    def index_changed(self, index):
        """
        Load the correct subcategories into the SubcategoryBox
        when a category is selected.
        """
        # Hint: clear existing items and add new ones based on category
        # print(index)
        if index == 0:
            self.subcomboBox.setEnabled(False)
        elif index == 1:
            self.subcomboBox.setEnabled(True)
            self.subcomboBox.clear()
            self.subcomboBox.addItems(['C++','Java'])
        elif index == 2:
            self.subcomboBox.setEnabled(True)
            self.subcomboBox.clear()
            self.subcomboBox.addItems(['ERD','SQL','OLAP','Data Mining'])
        elif index == 3:
            self.subcomboBox.setEnabled(True)
            self.subcomboBox.clear()
            self.subcomboBox.addItems(['Machine Learning','Robotics','Computer Vision'])
    # Function to add authors to the list
    def authorChange(self):
        """
        Add the author name from the input field to the authors list box.
        """
        self.authorsList.addItem(self.AuthorLine.text())


    # Function to validate form entries before submission
    def validateForm(self):
        """
        Perform form validation based on these rules:
        1. ISBN should not be more than 12 characters long.
        2. Purchased date should not be in the future.
        3. Journals should have no authors; other books need at least one author.
        4. If the book is issued, ensure 'Issued To' is filled and date is valid.
        """
        # Hint: Access values using self.ISBNBox.text(), self.purchasedOnBox.date(), etc.
        # Use conditions to check validity and set 'warning' messages.
        # Display message box for feedback.

        isbnBool = True
        dateBool = True
        authorBool = True
        issuedBool = True

        # ISBN validation
        if len(self.ISBNBox.text()) > 12:
            isbnBool = False
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Invalid ISBN!")
            dlg.exec()

        # Date validation
        if self.purchasedOnBox.date().toPyDate() >= date.today():
            dateBool = False
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Invalid Date!")
            dlg.exec()

        # Journal author validation
        if self.JournalButton.isChecked():
            if self.authorsList.count() > 0:
                authorBool = False
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Journals cannot have authors!")
                dlg.exec()
        elif self.RefBookButton.isChecked() or self.TextBookButton.isChecked():
            if self.authorsList.count() == 0:
                authorBool = False
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Books must have at least one author!")
                dlg.exec()
        else:
            authorBool = False
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Choose a valid book type!")
            dlg.exec()

        # issued validation
        if self.Issued.isChecked():
            if self.IssuedBy.text() == "":
                issuedBool = False
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Issued To must be filled!")
                dlg.exec()
            if (self.IssuedOn.date().toPyDate() >= date.today()) or (self.IssuedOn.date() <= self.purchasedOnBox.date().toPyDate()):
                issuedBool = False
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Invalid Issued On date!")
                dlg.exec()
        
        if isbnBool and dateBool and authorBool and issuedBool:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Book added successfully!")
            dlg.exec()
        


# Boilerplate code to run the app
app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec()
