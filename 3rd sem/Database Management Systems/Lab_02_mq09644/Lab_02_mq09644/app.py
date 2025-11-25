from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QTableWidget, QMessageBox
import sys

# Sample book data
books = [
    ["0201144719 9780201144710", "An introduction to database systems", "Database", "Reference Book", "True"],
    ["0805301453 9780805301458", "Fundamentals of database systems", "Database", "Reference Book", "False"],
    ["1571690867 9781571690869", "Object oriented programming in Java", "OOP", "Text Book", "False"],
    ["1842652478 9781842652473", "Object oriented programming using C++", "OOP", "Text Book", "False"],
    ["0070522618 9780070522619", "Artificial intelligence", "AI", "Journal", "False"],
    ["0865760047 9780865760042", "The Handbook of artificial intelligence", "AI", "Journal", "False"],
]

# Categories for dropdown
category = ["Database", "OOP", "AI"]


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the main window:
        - Load the UI file.
        - Populate the table with book data.
        - Fill the category dropdown (comboBox).
        - Connect buttons to their respective functions.
        """
        super(UI, self).__init__()
        uic.loadUi('Lab02.ui', self)
        self.comboBox.addItems(category)
        for book in books:
            rowPos = self.booksTableWidget.rowCount()
            self.booksTableWidget.insertRow(rowPos)
            for point, data in enumerate(book):
                self.booksTableWidget.setItem(rowPos, point, QTableWidgetItem(data))
        self.comboBox.setCurrentIndex (-1)
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.view)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_4.clicked.connect(self.closed)

        self.booksTableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

    def search(self):
        """
        Search and filter the table based on:
        - Selected category (comboBox)
        - Title text (lineEdit)
        - Book type (radio buttons)
        - Issued status (checkBox)
        """
        # bookTitle = self.lineEdit.text()
        # issued = self.checkBox.isChecked()
        # catfilter = self.comboBox.currentText()

        # # retrieves booktype from radio button
        # if self.radioButton_4.isChecked():
        #     booktype = self.radioButton_4.text()
        # elif self.radioButton_5.isChecked():
        #     booktype = self.radioButton_5.text()
        # elif self.radioButton_6.isChecked():
        #     booktype = self.radioButton_6.text()
        # else:
        #     booktype = None
        
        # # retrieves Title from title wali jaga
        # for row in range(self.bookTableWidget.rowCount()):
        #     book = self.bookTabeWidget
        #     for i in range(5):
        #         if bookTitle != self.bookTableWidget

        """
        Function to search and filter the booksTableWidget
        based on user input from comboBox , lineEdit , radioButtons , and checkBox. 
        """

    # Get user input
        selected_combo = self.comboBox.currentText ()
        selected_title = self.lineEdit.text()
        sel_radio_4 = self.radioButton_4.isChecked()
        sel_radio_5 = self.radioButton_5.isChecked()
        sel_radio_6 = self.radioButton_6.isChecked()
        issued = self.checkBox.isChecked()

        for row in range(self.booksTableWidget.rowCount()):
            # Get values from the current row
            combo_compare = self.booksTableWidget.item(row, 2)
            title_compare = self.booksTableWidget.item(row, 1)
            radio_compare = self.booksTableWidget.item(row, 3)
            issued_compare = self.booksTableWidget.item(row, 4)

            # Check if the user input and row data matches
            combo_match = selected_combo in combo_compare.text()
            title_match = selected_title in title_compare.text()
            issued_match = False
            if (issued_compare.text() == 'False' and not issued) or (issued_compare.text() == "True" and issued):
                issued_match = True

            # Implement the radio_match conditions below
            radio_match = False
            if (sel_radio_4 and radio_compare.text() == "Reference Book") or (sel_radio_5 and radio_compare.text() == "Text Book") or (sel_radio_6 and radio_compare.text() == "Journal"):
                radio_match = True

            match = combo_match and title_match and radio_match and issued_match
            self.booksTableWidget.setRowHidden(row, not match)



    def view(self):
        """
        Show details of the currently selected book:
        - Get selected row values (ISBN, title, category, type, issued status).
        - Open a new window to display book details.
        - Clear current selection after viewing.
        - Show a warning if no row is selected.
        """
        # Get the currently selected row
        curr_row = self.booksTableWidget.currentRow ()

        if curr_row >= 0:
        # Extract values from the selected row
            isbn = self.booksTableWidget.item(curr_row, 0).text()
            title = self.booksTableWidget.item(curr_row, 1).text()
            cat = self.booksTableWidget.item(curr_row, 2).text()
            rad = self.booksTableWidget.item(curr_row, 3).text()
            issue = self.booksTableWidget.item(curr_row, 4).text()

            # Create and show the detailed view window
            self.view = ViewBook(isbn, title, cat, rad, issue)
            self.view.show ()
            # Reset current selection
            self.booksTableWidget.setCurrentItem(None)
        else:
            # Show a warning if no row is selected
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error!")
            dlg.setText("Ghalat Entry Clanker!")
            dlg.exec()

        pass
    def delete(self):
        """
        Delete the currently selected row:
        - Confirm deletion with the user.
        - If confirmed, remove the row from the table.
        - Show a warning if no row is selected.
        """
        curr_row = self.booksTableWidget.currentRow()
        self.booksTableWidget.removeRow(curr_row)
        if curr_row <0:
            QMessageBox.warning(None, "Warning", "No Row Selected")
        else:
            QMessageBox.warning(None, "Success!", "Deleted Successfully!")

    def closed(self):
        """
        Close the application window.
        """
        self.close()


class ViewBook(QtWidgets.QMainWindow):
    def __init__(self, isbn, title, cat, rad, issue):
        """
        Initialize the detailed view window:
        - Load the 'view.ui' file.
        - Disable input fields (read-only mode).
        - Display book details (ISBN, title, category, type, issued status).
        """
        super(ViewBook, self).__init__()
        uic.loadUi('view.ui', self)

        self.lineEdit.setText(isbn)
        self.lineEdit_2.setText(title)
        self.lineEdit_3.setText(cat)
        if rad == "Journal":
            self.radioButton_6.setChecked(True)
        elif rad == "Text Book":
            self.radiobutton_5.setChecked(True)
        elif rad == "Reference Book":
            self.radioButton_4.setChecked(True)
        if issue == "True":
            self.checkBox.setChecked(True)
        





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())
