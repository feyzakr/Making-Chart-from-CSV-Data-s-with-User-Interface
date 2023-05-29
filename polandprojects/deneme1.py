
#Feyza KURUÇAY
import sys
import csv
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem,QAbstractItemView
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtWidgets import  QMainWindow, QDialog,  QTextEdit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create the application and the main window
app = QApplication(sys.argv)
window = QWidget()
#newWindow = QWidget()
window.resize(300,300)
# Create the layout for the main window
layout = QVBoxLayout()
def readRowCSV():
    mylist =[]
    countrow = 0
    countcolumn = 0
    csvfile = open("letter_frequency.csv", newline='')
    data = csv.reader(csvfile, delimiter=" ")
    for i in data:
        countrow += 1
        mylist.append(i)
    firstlinestr = ""
    for i in mylist[0]:
        firstlinestr += i + ","
    text = firstlinestr.split(",")
    for j in text:
        countcolumn +=1

    return countrow, (countcolumn-1)
def column_names(table):
    with open('letter_frequency.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        first_line = next(reader)
    table.setHorizontalHeaderLabels(first_line)

rowcount, columncount = readRowCSV()
#print(rowcount,columncount)
table = QTableWidget(rowcount,columncount)
column_names(table)
table.resize(600,700)


def openTable():
    # Create the table widget and set its dimensions

    # Populate the table with data
    #for i in range(rowcount):
    #    for j in range(columncount):

            # Create an item with the cell text and set it in the table
            #item = QTableWidgetItem("(%d, %d)" % (i, j))
            #table.setItem(i, j, item)
    csvfile = open("letter_frequency.csv", newline='')
    data = csv.reader(csvfile, delimiter=" ")
    num =0
    for k in data:

        text = k[0].split(",")
        num +=1
        if num >1:
            for i, row in enumerate(text):
                item = QTableWidgetItem(row)
                table.setItem(num-2, i, item)

        else:
            continue


    table.setEnabled(False)


    # Show the table
    table.show()
def openTableforaddings():
    # Create the table widget and set its dimensions

    # Populate the table with data
    #for i in range(rowcount):
    #    for j in range(columncount):

            # Create an item with the cell text and set it in the table
            #item = QTableWidgetItem("(%d, %d)" % (i, j))
            #table.setItem(i, j, item)
    csvfile = open("letter_frequency.csv", newline='')
    data = csv.reader(csvfile, delimiter=" ")
    num =0
    for k in data:
        text = k[0].split(",")
        num +=1
        if num >1:
            for i, row in enumerate(text):
                item = QTableWidgetItem(row)
                table.setItem(num-2, i, item)

        else:
            continue
    table.removeRow(rowCount()-1)

    table.setEnabled(False)





def save_table_data():
    # get the table and the number of rows and columns
    row_count = table.rowCount()
    col_count = table.columnCount()

    # get the column names
    headers = []
    for c in range(col_count):
        header_item = table.horizontalHeaderItem(c)
        if header_item is not None:
            headers.append(header_item.text())
        else:
            headers.append('')

    # open a file for writing
    with open('letter_frequency.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        # write the column names to the CSV file
        writer.writerow(headers)

        # write the table data to the CSV file
        for r in range(row_count):
            row_data = []
            for c in range(col_count):
                table_item = table.item(r, c)
                if table_item is not None:
                    row_data.append(table_item.text())
                else:
                    row_data.append('')
            writer.writerow(row_data)


def on_cell_clicked(item):
    row = item.row()
    column = item.column()
    value = item.text()
    newItem = QTableWidgetItem(value)
    table.setItem(row, column, newItem)
    save_table_data()

    #print(f'Cell at row {row}, column {column} clicked, value is {value}')

def edit():
    openTable()
    table.setEnabled(True)
    #table.setEditTriggers(QAbstractItemView.DoubleClicked)
    table.itemClicked.connect(on_cell_clicked)
    table.show()

def openWindorforAddingRow():
    dialog = QDialog()
    dialog.setWindowTitle("New Window")
    dialog.setFixedSize(400, 300)
    text_letter = QTextEdit(dialog)
    textfrequency = QTextEdit(dialog)
    textpercentage = QTextEdit(dialog)
    button_okey = QPushButton("Okey")
    layout = QVBoxLayout(dialog)
    layout.addWidget(text_letter)
    layout.addWidget(textfrequency)
    layout.addWidget(textpercentage)
    layout.addWidget(button_okey)
    dialog.setLayout(layout)
    button_okey.clicked.connect(lambda: save_text_and_close(dialog, text_letter, textfrequency, textpercentage))
    dialog.exec_()

def save_text_and_close(dialog, text_letter, textfrequency, textpercentage):
    text1 = text_letter.toPlainText()
    text2 = textfrequency.toPlainText()
    text3 = textpercentage.toPlainText()
    #print(text1)
    #print(text2)
    #print(text3)
    my_list = [text1, text2, text3]
    openTable()
    rowc = table.rowCount()
    table.removeRow(rowc - 1)
    table.setEnabled(True)
    rowc = table.rowCount()
    table.insertRow(rowc)
    columnnums = table.columnCount()
    i = 0
    for i in range(columnnums):
        value = my_list[i]
        item = QTableWidgetItem(value)
        table.setItem(rowc, i, item)
    save_table_data()
    table.setEnabled(False)
    dialog.close()
def openWindorforAddingColumn():
    dialog = QDialog()
    dialog.setWindowTitle("Column Name")
    dialog.setFixedSize(400, 300)
    text_column_name = QTextEdit(dialog)
    button_okey = QPushButton("Okey")
    layout = QVBoxLayout(dialog)
    layout.addWidget(text_column_name)
    layout.addWidget(button_okey)
    dialog.setLayout(layout)
    button_okey.clicked.connect(lambda: save_columntext_and_close(dialog, text_column_name))
    dialog.exec_()
def save_columntext_and_close(dialog, text_column_name):
    text1 = text_column_name.toPlainText()
    openTable()
    columnc = table.columnCount()
    table.setEnabled(True)
    column_name = text1
    numColumns = table.columnCount()
    table.insertColumn(columnc)
    table.setHorizontalHeaderItem(numColumns, QTableWidgetItem(str(column_name)))
    save_table_data()
    column_names(table)
    table.setEnabled(False)
    table.show()
    dialog.close()
def openWindorformakingLineChart():
    dialog = QDialog()
    dialog.setWindowTitle("Column Name")
    dialog.setFixedSize(300, 200)
    text_column_name1 = QTextEdit(dialog)
    text_column_name2 = QTextEdit(dialog)
    button_okey = QPushButton("Okey")
    layout = QVBoxLayout(dialog)
    layout.addWidget(text_column_name1)
    layout.addWidget(text_column_name2)
    layout.addWidget(button_okey)
    dialog.setLayout(layout)
    button_okey.clicked.connect(lambda: save_columntext_and_close_linechart(dialog, text_column_name1,text_column_name2))
    dialog.exec_()
def save_columntext_and_close_linechart(dialog, text_column_name1,text_column_name2):
    text1 = text_column_name1.toPlainText()
    text2= text_column_name2.toPlainText()
    if text1 == "letter" and text2 == "frequency":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["letter", "frequency"])
        repetation1 = csvfile["letter"].nunique()
        repetation2 = csvfile["frequency"].nunique()
    elif text1 == "letter" and text2 == "percentage":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["letter", "percentage"])
        repetation1 = csvfile["letter"].nunique()
        repetation2 = csvfile["percentage"].nunique()
    elif text1 == "frequency" and text2 == "letter":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["frequency", "letter"])
        repetation1 = csvfile["frequency"].nunique()
        repetation2 = csvfile["letter"].nunique()
    elif text1 == "frequency" and text2 == "percentage":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["frequency", "percentage"])
        repetation1 = csvfile["frequency"].nunique()
        repetation2 = csvfile["percentage"].nunique()
    elif text1 == "percentage" and text2 == "letter":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["percentage", "letter"])
        repetation1 = csvfile["percentage"].nunique()
        repetation2 = csvfile["letter"].nunique()
    elif text1 == "percentage" and text2 == "frequency":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["percentage", "frequency"])
        repetation1 = csvfile["percentage"].nunique()
        repetation2 = csvfile["frequency"].nunique()
    my_y_list = []
    for i in csvfile[text1]:
        my_y_list.append(i)
    # my_y_list.insert(0,0)
    my_x_list = []
    for i in csvfile[text2]:
        my_x_list.append(i)
    # my_x_list.insert(0,0)
    plt.rcParams["figure.figsize"] = [repetation1 / 2, repetation2 / 2]
    plt.rcParams["figure.autolayout"] = False
    fig, ax = plt.subplots()
    fig.figsize = [repetation1 / 2, repetation2 / 2]
    ax.plot(my_x_list, my_y_list)
    plt.show()

    dialog.close()
def openWindorformakingPieChart():
    dialog = QDialog()
    dialog.setWindowTitle("Column Name")
    dialog.setFixedSize(300, 100)
    text_column_name = QTextEdit(dialog)
    button_okey = QPushButton("Okey")
    layout = QVBoxLayout(dialog)
    layout.addWidget(text_column_name)
    layout.addWidget(button_okey)
    dialog.setLayout(layout)
    button_okey.clicked.connect(lambda: save_columntext_and_close_pie(dialog, text_column_name))
    dialog.exec_()
def save_columntext_and_close_pie(dialog, text_column_name):
    text1 = text_column_name.toPlainText()
    if text1 == "letter":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["letter", "letter"])
    elif text1 == "percentage":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["letter", "percentage"])
    elif text1 == "frequency":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["letter", "frequency"])
    total = csvfile[text1].sum()
    angles = csvfile[text1] / total * 360

    # Create the pie chart
    plt.pie(angles, labels=csvfile["letter"])
    plt.show()

    dialog.close()
def openWindorformakingHeatMap():
    dialog = QDialog()
    dialog.setWindowTitle("Column Name")
    dialog.setFixedSize(300, 100)
    text_column_name1 = QTextEdit(dialog)
    button_okey = QPushButton("Okey")
    layout = QVBoxLayout(dialog)
    layout.addWidget(text_column_name1)
    layout.addWidget(button_okey)
    dialog.setLayout(layout)
    button_okey.clicked.connect(lambda: save_columntext_and_close_heatmap(dialog, text_column_name1))
    dialog.exec_()
def save_columntext_and_close_heatmap(dialog, text_column_name1):
    text1 = text_column_name1.toPlainText()
    if text1 == "letter":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["letter"])
    elif text1 == "frequency":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["frequency"])
    elif text1 == "percentage":
        csvfile = pd.read_csv("letter_frequency.csv", usecols=["percentage"])
    my_y_list = []
    for i in csvfile[text1]:
        my_y_list.append(i)
        # my_y_list.insert(0,0)
    my_y_list.sort()
    data = np.array([my_y_list])
    repetation1 = csvfile[text1].nunique()
    # Create the figure and axes for the heatmap
    fig, ax = plt.subplots()
    fig.figsize = [repetation1 / 2, repetation1 / 2]

    # Create the heatmap using the imshow function
    heatmap = ax.imshow(data, cmap='hot', aspect='auto')

    ax.set_xticks(np.arange(len(my_y_list)))
    ax.set_xticklabels(my_y_list)

    # yticks = np.arange(0, 1.1, 0.25)
    # yticklabels = [str(int(p)) for p in yticks*100]
    # ax.set_yticks(yticks)
    # ax.set_yticklabels(yticklabels)

    # Add a colorbar to the heatmap
    fig.colorbar(heatmap)

    # Show the figure
    plt.show()
    dialog.close()



# Create the buttons and add them to the layout
label_welcome = QLabel("WELCOME")
label_welcome.setStyleSheet("color: purple")
label_push = QLabel("Select a button")
label_push.setStyleSheet("color: purple")
label_push.setAlignment(Qt.AlignCenter)
label_welcome.setAlignment(Qt.AlignCenter)
button1 = QPushButton("Display")
button1.setStyleSheet("color:#ff1493")
button2 = QPushButton("Edit")
button2.setStyleSheet("color:#ff1493")
button3 = QPushButton("Add Row")
button3.setStyleSheet("color:#ff1493")
button4 = QPushButton("Add column")
button4.setStyleSheet("color:#ff1493")
button5 = QPushButton("Draw line chart")
button5.setStyleSheet("color:#ff1493")
button6 = QPushButton("Draw pie chart")
button6.setStyleSheet("color:#ff1493")
button7 = QPushButton("Draw heatmap")
button7.setStyleSheet("color:#ff1493")
layout.addWidget(label_welcome)
layout.addWidget(label_push)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)
layout.addWidget(button6)
layout.addWidget(button7)

button1.clicked.connect(openTable)
button2.clicked.connect(edit)
button3.clicked.connect(openWindorforAddingRow)
button4.clicked.connect(openWindorforAddingColumn)
button5.clicked.connect(openWindorformakingLineChart)
button6.clicked.connect(openWindorformakingPieChart)
button7.clicked.connect(openWindorformakingHeatMap)
# Set the layout for the main window and show it
window.setLayout(layout)
window.show()
app.exec_()

