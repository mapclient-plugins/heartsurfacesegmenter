# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'heartsurfacewidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mapclientplugins\heartsurfacesegmenterstep\view\segmentationwidget import SegmentationWidget


class Ui_HeartSurfaceWidget(object):
    def setupUi(self, HeartSurfaceWidget):
        if not HeartSurfaceWidget.objectName():
            HeartSurfaceWidget.setObjectName(u"HeartSurfaceWidget")
        HeartSurfaceWidget.resize(1021, 620)
        self.horizontalLayout = QHBoxLayout(HeartSurfaceWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(HeartSurfaceWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButtonLoad = QPushButton(self.groupBox_4)
        self.pushButtonLoad.setObjectName(u"pushButtonLoad")

        self.horizontalLayout_8.addWidget(self.pushButtonLoad)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButtonSave = QPushButton(self.groupBox_4)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout_9.addWidget(self.pushButtonSave)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.line = QFrame(self.groupBox_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButtonContinue = QPushButton(self.groupBox_4)
        self.pushButtonContinue.setObjectName(u"pushButtonContinue")

        self.horizontalLayout_7.addWidget(self.pushButtonContinue)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.verticalLayout_10.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonViewAll = QPushButton(self.groupBox_6)
        self.pushButtonViewAll.setObjectName(u"pushButtonViewAll")

        self.horizontalLayout_2.addWidget(self.pushButtonViewAll)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonHideAll = QPushButton(self.groupBox_6)
        self.pushButtonHideAll.setObjectName(u"pushButtonHideAll")

        self.horizontalLayout_6.addWidget(self.pushButtonHideAll)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.listWidget = QListWidget(self.groupBox_6)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(100, 0))

        self.verticalLayout_9.addWidget(self.listWidget)


        self.verticalLayout_10.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)

        self.spinBoxPointSize = QSpinBox(self.groupBox_5)
        self.spinBoxPointSize.setObjectName(u"spinBoxPointSize")
        self.spinBoxPointSize.setMinimum(1)

        self.horizontalLayout_10.addWidget(self.spinBoxPointSize)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_11.addWidget(self.label_2)

        self.comboBoxHeartSurface = QComboBox(self.groupBox_5)
        self.comboBoxHeartSurface.addItem("")
        self.comboBoxHeartSurface.addItem("")
        self.comboBoxHeartSurface.setObjectName(u"comboBoxHeartSurface")

        self.horizontalLayout_11.addWidget(self.comboBoxHeartSurface)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.verticalLayout_10.addWidget(self.groupBox_5)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.widgetZinc = SegmentationWidget(HeartSurfaceWidget)
        self.widgetZinc.setObjectName(u"widgetZinc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.widgetZinc)


        self.retranslateUi(HeartSurfaceWidget)

        QMetaObject.connectSlotsByName(HeartSurfaceWidget)
    # setupUi

    def retranslateUi(self, HeartSurfaceWidget):
        HeartSurfaceWidget.setWindowTitle(QCoreApplication.translate("HeartSurfaceWidget", u"Heart Surface", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("HeartSurfaceWidget", u"Heart Surface Segmenter", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("HeartSurfaceWidget", u"File", None))
        self.pushButtonLoad.setText(QCoreApplication.translate("HeartSurfaceWidget", u"Load", None))
        self.pushButtonSave.setText(QCoreApplication.translate("HeartSurfaceWidget", u"Save", None))
        self.pushButtonContinue.setText(QCoreApplication.translate("HeartSurfaceWidget", u"Continue", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("HeartSurfaceWidget", u"View", None))
        self.pushButtonViewAll.setText(QCoreApplication.translate("HeartSurfaceWidget", u"View All", None))
        self.pushButtonHideAll.setText(QCoreApplication.translate("HeartSurfaceWidget", u"Hide All", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("HeartSurfaceWidget", u"Segmentation", None))
        self.label.setText(QCoreApplication.translate("HeartSurfaceWidget", u"Point size: ", None))
        self.label_2.setText(QCoreApplication.translate("HeartSurfaceWidget", u"Heart surface: ", None))
        self.comboBoxHeartSurface.setItemText(0, QCoreApplication.translate("HeartSurfaceWidget", u"Endocardial", None))
        self.comboBoxHeartSurface.setItemText(1, QCoreApplication.translate("HeartSurfaceWidget", u"Epicardial", None))

    # retranslateUi

