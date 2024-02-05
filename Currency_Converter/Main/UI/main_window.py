# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        if not mw_Main.objectName():
            mw_Main.setObjectName(u"mw_Main")
        mw_Main.resize(311, 261)
        font = QFont()
        font.setPointSize(12)
        mw_Main.setFont(font)
        self.gridLayout = QGridLayout(mw_Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(mw_Main)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cb_InputCurrency = QComboBox(self.groupBox)
        self.cb_InputCurrency.addItem("")
        self.cb_InputCurrency.addItem("")
        self.cb_InputCurrency.addItem("")
        self.cb_InputCurrency.setObjectName(u"cb_InputCurrency")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cb_InputCurrency)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.le_InputValue = QLineEdit(self.groupBox)
        self.le_InputValue.setObjectName(u"le_InputValue")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_InputValue.sizePolicy().hasHeightForWidth())
        self.le_InputValue.setSizePolicy(sizePolicy)
        self.le_InputValue.setFocusPolicy(Qt.StrongFocus)
        self.le_InputValue.setFrame(True)
        self.le_InputValue.setClearButtonEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.le_InputValue)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.le_OutputValue = QLineEdit(self.groupBox_2)
        self.le_OutputValue.setObjectName(u"le_OutputValue")
        self.le_OutputValue.setReadOnly(True)

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.le_OutputValue)

        self.cb_OutputCurrency = QComboBox(self.groupBox_2)
        self.cb_OutputCurrency.addItem("")
        self.cb_OutputCurrency.addItem("")
        self.cb_OutputCurrency.addItem("")
        self.cb_OutputCurrency.setObjectName(u"cb_OutputCurrency")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.cb_OutputCurrency)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.pb_Convert = QPushButton(self.groupBox_3)
        self.pb_Convert.setObjectName(u"pb_Convert")
        self.pb_Convert.setAutoDefault(True)

        self.gridLayout_2.addWidget(self.pb_Convert, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.l_Message = QLabel(mw_Main)
        self.l_Message.setObjectName(u"l_Message")
        self.l_Message.setEnabled(True)
        self.l_Message.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.l_Message, 2, 0, 1, 1)

        QWidget.setTabOrder(self.le_InputValue, self.cb_InputCurrency)
        QWidget.setTabOrder(self.cb_InputCurrency, self.cb_OutputCurrency)
        QWidget.setTabOrder(self.cb_OutputCurrency, self.pb_Convert)
        QWidget.setTabOrder(self.pb_Convert, self.le_OutputValue)

        self.retranslateUi(mw_Main)

        self.cb_OutputCurrency.setCurrentIndex(1)
        self.pb_Convert.setDefault(False)


        QMetaObject.connectSlotsByName(mw_Main)
    # setupUi

    def retranslateUi(self, mw_Main):
        mw_Main.setWindowTitle(QCoreApplication.translate("mw_Main", u"Currency Convertor", None))
        self.groupBox.setTitle(QCoreApplication.translate("mw_Main", u"Input", None))
        self.label.setText(QCoreApplication.translate("mw_Main", u"Currency", None))
        self.cb_InputCurrency.setItemText(0, QCoreApplication.translate("mw_Main", u"CZK", None))
        self.cb_InputCurrency.setItemText(1, QCoreApplication.translate("mw_Main", u"EUR", None))
        self.cb_InputCurrency.setItemText(2, QCoreApplication.translate("mw_Main", u"USD", None))

        self.label_2.setText(QCoreApplication.translate("mw_Main", u"Amount", None))
        self.le_InputValue.setInputMask("")
        self.le_InputValue.setText("")
        self.le_InputValue.setPlaceholderText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("mw_Main", u"Output", None))
        self.label_3.setText(QCoreApplication.translate("mw_Main", u"Currency", None))
        self.label_4.setText(QCoreApplication.translate("mw_Main", u"Amount", None))
        self.cb_OutputCurrency.setItemText(0, QCoreApplication.translate("mw_Main", u"CZK", None))
        self.cb_OutputCurrency.setItemText(1, QCoreApplication.translate("mw_Main", u"EUR", None))
        self.cb_OutputCurrency.setItemText(2, QCoreApplication.translate("mw_Main", u"USD", None))

        self.cb_OutputCurrency.setCurrentText(QCoreApplication.translate("mw_Main", u"EUR", None))
        self.pb_Convert.setText(QCoreApplication.translate("mw_Main", u"Convert", None))
        self.l_Message.setText(QCoreApplication.translate("mw_Main", u"Message", None))
    # retranslateUi

