#for GUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo                                  
from PyQt5.QtWidgets import QFileDialog,QLabel
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QDialog, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification



import random

import numpy as np
from recognition_module import single_classification, find_combo_by_top

class Ui_MainWindow(object):
    """
    This class to to generate a GUI (graphical user interface)
    """
    def __init__(self):
        """
        initil them three in order to add clothes later.
        """
        self.top = []
        self.bottom = []
        self.shoes = []
        self.ad_top = None
        self.ad_bot = None
        self.ad_sho = None
        self.final_outfit = None
        
    def ALL_PREDICT(self):
        """
        User click ADD botton to call this function, after getting a path of a photo, this function do prediction by the models and show the result in the GUI.
        """
        _translate = QtCore.QCoreApplication.translate
        directory1 = QFileDialog.getOpenFileName(None, "Select file", "C:/")

        if not directory1[0]:
            return
        result = single_classification(directory1[0])

        # Check if the result is None
        if result is None:
            QMessageBox.critical(self.centralwidget, "Information", "Unable to classify.")
            return
        sub, info, res_place_holder = single_classification(directory1[0])
        
        # if the result is top, then add an item to the "top" list on GUI.
        if sub == "top":
            item = QtWidgets.QListWidgetItem(info)
            self.TOP_LIST.addItem(item)
            self.top.append(res_place_holder)
        # if the result is bottom, then add an item to the "bottom" list on GUI.
        elif sub == "bottom":
            item = QtWidgets.QListWidgetItem(info)
            self.BOTTOM_LIST.addItem(item)
            self.bottom.append(res_place_holder)
        # if the result is shoes, then add an item to the "shoes" list on GUI.
        elif sub == "foot":
            item = QtWidgets.QListWidgetItem(info)
            self.SHOE_LIST.addItem(item)
            self.shoes.append(res_place_holder)
        else:
        # Handle the case when no suitable category is identified
            QMessageBox.critical(self.centralwidget, "Information", "No suitable category found.")
    def TOP_LIST_EDIT(self):
            """
            User click EDIT botton to call this function to edit a prediction result.
            """
            selected_items = self.TOP_LIST.selectedItems()
             # Check if any item is selected
            if not selected_items:
                # Display a message box
                QMessageBox.critical(self.centralwidget, "Information", "No item selected. Please select a TOP item to edit.")
                return
            selected_items = self.TOP_LIST.selectedItems()
            text, okPressed = QtWidgets.QInputDialog.getText(self.AddTopButton, "EDIT","Please Edit This Top:", QtWidgets.QLineEdit.Normal, selected_items[0].text())
            for i in selected_items:
                self.TOP_LIST.takeItem(self.TOP_LIST.row(i))
            if okPressed and text != '':
                item = QtWidgets.QListWidgetItem(text)
                self.TOP_LIST.addItem(item)   
    def TOP_LIST_DEL(self):
            """
            User click DELETE botton to call this function to delete a photo with prediction result.
            """
            selected_items = self.TOP_LIST.selectedItems()
            # Check if any item is selected
            if not selected_items:
                # Display a message box
                QMessageBox.critical(self.centralwidget, "Information", "No item selected. Please select a TOP item to delete.")
                return
            
            selected_items = self.TOP_LIST.selectedItems()
            for i in selected_items:
                self.TOP_LIST.takeItem(self.TOP_LIST.row(i))
            text = selected_items[0].text()
            
            path = text.split(", ")[-1]
            for i in self.top:
                if(i[-1] == path):
                    self.top.remove(i)
            
    ####          
    def BOTTOM_LIST_EDIT(self):
            """
            User click EDIT botton to call this function to edit a prediction result.
            """
            selected_items = self.BOTTOM_LIST.selectedItems()
             # Check if any item is selected
            if not selected_items:
                # Display a message box
                QMessageBox.critical(self.centralwidget, "Information", "No item selected. Please select a BOTTOM item to edit.")
                return
            
            selected_items = self.BOTTOM_LIST.selectedItems()
            text, okPressed = QtWidgets.QInputDialog.getText(self.AddBottomButton, "EDIT","Please Edit This Bottom:", QtWidgets.QLineEdit.Normal, selected_items[0].text())
            for i in selected_items:
                self.BOTTOM_LIST.takeItem(self.BOTTOM_LIST.row(i))
            if okPressed and text != '':
                item = QtWidgets.QListWidgetItem(text)
                self.BOTTOM_LIST.addItem(item)   
    def BOTTOM_LIST_DEL(self):
            """
            User click DELETE botton to call this function to delete a photo with prediction result.
            """
            selected_items = self.BOTTOM_LIST.selectedItems()
             # Check if any item is selected
            if not selected_items:
                # Display a message box
                QMessageBox.critical(self.centralwidget, "Information", "No item selected. Please select a BOTTOM item to delete.")
                return
            
            selected_items = self.BOTTOM_LIST.selectedItems()
            for i in selected_items:
                self.BOTTOM_LIST.takeItem(self.BOTTOM_LIST.row(i))
            text = selected_items[0].text()
            
            path = text.split(", ")[-1]
            for i in self.bottom:
                if(i[-1] == path):
                    self.bottom.remove(i)
            
           
    def SHOE_LIST_EDIT(self):
            """
            User click EDIT botton to call this function to edit a prediction result.
            """
            selected_items = self.SHOE_LIST.selectedItems()
             # Check if any item is selected
            if not selected_items:
                # Display a message box
                QMessageBox.critical(self.centralwidget, "Information", "No item selected. Please select a SHOE item to edit.")
                return
            
            selected_items = self.SHOE_LIST.selectedItems()
            text, okPressed = QtWidgets.QInputDialog.getText(self.AddShoeButton, "EDIT","Please Edit This Shoes:", QtWidgets.QLineEdit.Normal, selected_items[0].text())
            for i in selected_items:
                self.SHOE_LIST.takeItem(self.SHOE_LIST.row(i))
            if okPressed and text != '':
                item = QtWidgets.QListWidgetItem(text)
                self.SHOE_LIST.addItem(item)   
    def SHOE_LIST_DEL(self):
            """
            User click DELETE botton to call this function to delete a photo with prediction result.
            """
            selected_items = self.SHOE_LIST.selectedItems()
             # Check if any item is selected
            if not selected_items:
                # Display a message box
                QMessageBox.critical(self.centralwidget, "Information", "No item selected. Please select a SHOE item to delete.")
                return
            
            selected_items = self.SHOE_LIST.selectedItems()
            for i in selected_items:
                self.SHOE_LIST.takeItem(self.SHOE_LIST.row(i))
            text = selected_items[0].text()
            
            path = text.split(", ")[-1]
            for i in self.shoes:
                if(i[-1] == path):
                    self.shoes.remove(i)
    #################
    def Generate(self):
          
    # Use find_combo_by_top to select top, bottom, and shoes
            top_color_group = np.random.randint(12 + 3)  # Assuming there are 12 colors + 3 multi-color options
            combo_type = np.random.choice([0, 30, 60, 90])  # Assuming 0 corresponds to same combo, 30 to close combo, etc.

    # Call find_combo_by_top to get the recommended combination
            bottom_color_group, shoes_color_group = find_combo_by_top(top_color_group, combo_type)

    # Filter items based on the selected combination
            top_candidates = [i for i in self.top if i[2] == top_color_group and i[3] == toseason]
            bottom_candidates = [i for i in self.bottom if i[2] == bottom_color_group and i[3] == toseason]
            shoes_candidates = [i for i in self.shoes if i[2] == shoes_color_group and i[3] == toseason]

    # Select random items if there are candidates, otherwise, choose randomly from the entire list
            ad_top = random.choice(top_candidates) if top_candidates else random.choice(self.top)
            ad_bot = random.choice(bottom_candidates) if bottom_candidates else random.choice(self.bottom)
            ad_sho = random.choice(shoes_candidates) if shoes_candidates else random.choice(self.shoes)

    # Update the GUI with the selected outfit
            self.listWidget_1.setPixmap(QtGui.QPixmap(ad_top[-1]).scaled(281, 300))
            self.listWidget_2.setPixmap(QtGui.QPixmap(ad_bot[-1]).scaled(281, 300))
            self.listWidget_3.setPixmap(QtGui.QPixmap(ad_sho[-1]).scaled(281, 300))
            
            self.ad_top = ad_top
            self.ad_bot = ad_bot
            self.ad_sho = ad_sho
    

    def CombineOutfits(self):
        top_candidates = self.top
        bottom_candidates = self.bottom
        shoes_candidates = self.shoes
        
        if not self.is_item_selected(top_candidates) or not self.is_item_selected(bottom_candidates) or not self.is_item_selected(shoes_candidates):
            # Display a QMessageBox for incomplete selection
            QMessageBox.warning(self.centralwidget, 'Incomplete Selection', 'Please select at least one item for each category.')
            return
        
        memoization_table = {}

        # Define contemporary colors
        contemporary_colors = ["white", "black", "gray", "beige", "navy", "pastel", "offwhite","gainsboro", "navyblue",]

        def is_contemporary_color(color):
            return color.lower() in contemporary_colors

        def dp_combine_outfits(top_index, bottom_index, shoes_index):
            # Check if already at the last index for bottoms or shoes
            if top_index == len(top_candidates) - 1 or bottom_index == len(bottom_candidates) - 1 or shoes_index == len(shoes_candidates) - 1:
                current_top = top_candidates[top_index]
                current_bottom = bottom_candidates[bottom_index]
                current_shoes = shoes_candidates[shoes_index]

                # Check if colors match and are contemporary
                if is_contemporary_color(current_top[2]) and is_contemporary_color(current_bottom[2]) and is_contemporary_color(current_shoes[2]):
                    return [current_top, current_bottom, current_shoes]
                else:
                    return []

            memo_key = (top_index, bottom_index, shoes_index)
            if memo_key in memoization_table:
                return memoization_table[memo_key]

            current_top = top_candidates[top_index]
            current_bottom = bottom_candidates[bottom_index]
            current_shoes = shoes_candidates[shoes_index]

            # Check if colors match and are contemporary
            if is_contemporary_color(current_top[2]) and is_contemporary_color(current_bottom[2]) and is_contemporary_color(current_shoes[2]):
                # Recursively check all combinations for the next bottom and shoes
                result1 = dp_combine_outfits(top_index + 1, bottom_index + 1, shoes_index + 1)
                result2 = dp_combine_outfits(top_index + 1, bottom_index + 1, shoes_index)
                result3 = dp_combine_outfits(top_index + 1, bottom_index, shoes_index + 1)
                result4 = dp_combine_outfits(top_index, bottom_index + 1, shoes_index + 1)
                result5 = dp_combine_outfits(top_index, bottom_index + 1, shoes_index)
                result6 = dp_combine_outfits(top_index, bottom_index, shoes_index + 1)

                # Choose the combination with the maximum length
                result = max([result1, result2, result3, result4, result5, result6], key=len)
            else:
                # If colors don't match or are not contemporary, check all combinations for the next bottom and shoes
                result1 = dp_combine_outfits(top_index + 1, bottom_index + 1, shoes_index)
                result2 = dp_combine_outfits(top_index + 1, bottom_index, shoes_index + 1)
                result3 = dp_combine_outfits(top_index, bottom_index + 1, shoes_index + 1)

                # Choose the combination with the maximum length
                result = max(result1, result2, result3, key=len)

            memoization_table[memo_key] = result
            return result

        final_outfit = dp_combine_outfits(0, 0, 0)

        if final_outfit:
            self.final_outfit = final_outfit

        # Assuming final_outfit is a list of file paths for top, bottom, and shoes
            top_image_path, bottom_image_path, shoes_image_path = final_outfit[0][5], final_outfit[1][5], final_outfit[2][5]

        # Update the pixmaps of the QLabel widgets with the images of the selected outfit
            self.listWidget_4.setPixmap(QtGui.QPixmap(top_image_path).scaled(281, 300))
            self.listWidget_5.setPixmap(QtGui.QPixmap(bottom_image_path).scaled(281, 300))
            self.listWidget_6.setPixmap(QtGui.QPixmap(shoes_image_path).scaled(281, 300))
        else:
    # Display a QMessageBox for no matching contemporary outfit
           
            QMessageBox.critical(self.centralwidget, 'Warning', 'No matching contemporary outfit found.')


    def NLP(self):
    
        if not self.ad_top and not self.ad_bot and not self.ad_sho or not self.final_outfit:
            QMessageBox.critical(self.centralwidget, "Information", "Please generate an outfit before using NLP.")
            return
        checkpoint = "amir7d0/distilbert-base-uncased-finetuned-amazon-reviews"
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        model = TFAutoModelForSequenceClassification.from_pretrained(checkpoint)

        # Get text from the textbox
        text = self.textbox.text()

        # Check if the textbox is empty
        if not text:
            QMessageBox.critical(self.centralwidget, "Information", "Please enter some text to analyze.")
            return

        # Tokenize and predict the class
        encoded_input = tokenizer(text, return_tensors='tf')
        output = model(encoded_input)
        logits = output.logits.numpy()
        predicted_class = int(logits.argmax(axis=1).item())

        # Show result based on the predicted class
        if predicted_class <= 3:
            QMessageBox.information(self.centralwidget, "Information", "Please remove any undesired pieces to recommend a satisfactory outfit")
        else:
            QMessageBox.information(self.centralwidget, "Information", "Congratulations on finding your outfit")


    # The above is what functions the GUI should have
    
#####################################################################################

    # The below are the appearance settings of the GUI
    
    def setupUi(self, MainWindow):
        """
        Add items into GUI.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200,1550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TOP_LIST = QtWidgets.QListWidget(self.centralwidget)
        self.TOP_LIST.setGeometry(QtCore.QRect(10, 30, 281, 181))
        self.TOP_LIST.setObjectName("TOP_LIST")
        self.AddTopButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddTopButton.setGeometry(QtCore.QRect(10, 210, 141, 41))
        self.AddTopButton.setAutoFillBackground(False)
        self.AddTopButton.setCheckable(False)
        self.AddTopButton.setObjectName("AddTopButton")
        self.DeleteTopButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteTopButton.setGeometry(QtCore.QRect(150, 210, 141, 41))
        self.DeleteTopButton.setCheckable(False)
        self.DeleteTopButton.setChecked(False)
        self.DeleteTopButton.setObjectName("DeleteTopButton")
        self.AddBottomButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddBottomButton.setGeometry(QtCore.QRect(300, 210, 141, 41))
        self.AddBottomButton.setObjectName("AddBottomButton")
        self.BOTTOM_LIST = QtWidgets.QListWidget(self.centralwidget)
        self.BOTTOM_LIST.setGeometry(QtCore.QRect(300, 30, 281, 181))
        self.BOTTOM_LIST.setObjectName("BOTTOM_LIST")
        self.DeleteBottomButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteBottomButton.setGeometry(QtCore.QRect(440, 210, 141, 41))
        self.DeleteBottomButton.setObjectName("DeleteBottomButton")
        self.AddShoeButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddShoeButton.setGeometry(QtCore.QRect(590, 210, 141, 41))
        self.AddShoeButton.setObjectName("AddShoeButton")
        self.SHOE_LIST = QtWidgets.QListWidget(self.centralwidget)
        self.SHOE_LIST.setGeometry(QtCore.QRect(590, 30, 281, 181))
        self.SHOE_LIST.setObjectName("SHOE_LIST")
        self.DeleteShoeButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteShoeButton.setGeometry(QtCore.QRect(730, 210, 141, 41))
        self.DeleteShoeButton.setObjectName("DeleteShoeButton")
        self.GenerateButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateButton.setGeometry(QtCore.QRect(300, 270, 281, 81))
        self.GenerateButton.setObjectName("GenerateButton")
        self.CombineOutfitButton = QtWidgets.QPushButton(self.centralwidget)
        self.CombineOutfitButton.setGeometry(QtCore.QRect(590, 270, 281, 81))
        self.CombineOutfitButton.setObjectName("CombineOutfitButton")
        
        self.HistoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.HistoryButton.setGeometry(QtCore.QRect(10, 270, 281, 81))
        self.HistoryButton.setObjectName("HistoryButton")
        self.TopLabel = QtWidgets.QLabel(self.centralwidget)
        self.TopLabel.setGeometry(QtCore.QRect(140, 10, 60, 16))
        self.TopLabel.setTextFormat(QtCore.Qt.RichText)
        self.TopLabel.setObjectName("TopLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 10, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 60, 16))
        self.label_2.setObjectName("label_2")
        self.listWidget_1 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_1.setGeometry(QtCore.QRect(10, 370, 281, 300))
        self.listWidget_1.setObjectName("listWidget_1")
        self.listWidget_1.setPixmap(QtGui.QPixmap(r"pictures\top_question.png").scaled(281,300))
        self.listWidget_2 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(300, 370, 281, 300))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setPixmap(QtGui.QPixmap(r"pictures\top_question.png").scaled(281,300))
        
        self.listWidget_3 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(590, 370, 281, 300))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_3.setPixmap(QtGui.QPixmap(r"pictures\top_question.png").scaled(281,300))
        
        self.listWidget_4 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(10, 680, 281, 300))
        self.listWidget_4.setObjectName("listWidget_1")
        self.listWidget_4.setPixmap(QtGui.QPixmap(r"pictures\top_question.png").scaled(281,300))
        self.listWidget_5 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(300, 680, 281, 300))
        self.listWidget_5.setObjectName("listWidget_2")
        self.listWidget_5.setPixmap(QtGui.QPixmap(r"pictures\top_question.png").scaled(281,300))

        self.listWidget_6 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_6.setGeometry(QtCore.QRect(590, 680, 281, 300))
        self.listWidget_6.setObjectName("listWidget_3")
        self.listWidget_6.setPixmap(QtGui.QPixmap(r"pictures\top_question.png").scaled(281,300))
        
        self.textbox = QLineEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(885, 270, 300, 200))
        font = QFont()
        font.setPointSize(18)
        self.textbox.setFont(font)

        # Create a button in the window
        self.button = QPushButton('Show Verdict', self.centralwidget)
        self.button.setGeometry(QtCore.QRect(885, 471, 141, 51))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #####################################################################################
        
        # Establish a connection between buttons and functions
        self.AddTopButton.clicked.connect(self.TOP_LIST_EDIT)
        self.DeleteTopButton.clicked.connect(self.TOP_LIST_DEL)
        
        self.AddBottomButton.clicked.connect(self.BOTTOM_LIST_EDIT)
        self.DeleteBottomButton.clicked.connect(self.BOTTOM_LIST_DEL)
        self.button.clicked.connect(self.NLP)
        self.AddShoeButton.clicked.connect(self.SHOE_LIST_EDIT)
        self.DeleteShoeButton.clicked.connect(self.SHOE_LIST_DEL)
        self.HistoryButton.clicked.connect(self.ALL_PREDICT)            
        self.GenerateButton.clicked.connect(self.Generate)   
        self.CombineOutfitButton.clicked.connect(self.CombineOutfits)
           
        
        #####################################################################################

    def retranslateUi(self, MainWindow):
        """
        This function translate the item on GUI from what computer can understand to what we can understand. (Gives items names)
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI-WORS"))
        self.AddTopButton.setText(_translate("MainWindow", "EDIT"))
        self.DeleteTopButton.setText(_translate("MainWindow", "DELETE"))
        self.AddBottomButton.setText(_translate("MainWindow", "EDIT "))
        self.DeleteBottomButton.setText(_translate("MainWindow", "DELETE"))
        self.AddShoeButton.setText(_translate("MainWindow", "EDIT "))
        self.DeleteShoeButton.setText(_translate("MainWindow", "DELETE"))
        self.GenerateButton.setText(_translate("MainWindow", "Generate Outfit (Greedy Algorithm)"))
        self.CombineOutfitButton.setText(_translate("MainWindow", "Generate Outfit (Dynamic Programming)"))
        self.HistoryButton.setText(_translate("MainWindow", "ADD A PHOTO"))
        self.TopLabel.setText(_translate("MainWindow", "Top"))
        self.label.setText(_translate("MainWindow", "Bottom"))
        self.label_2.setText(_translate("MainWindow", "Shoes"))
        
def run_ui():
    

    # This part is to run the GUI we defined above and for some basic settings about the GUI, such as color, style, etc.

    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('fusion'))
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet("color: white;"
                             "selection-background-color: peru;"
                             "selection-color: white;"
                             "background-color: saddlebrown;")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from ui_module import*
run_ui()  