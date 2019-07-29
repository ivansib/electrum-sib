"""Sibcoin look and feel."""

import os
from electrum_dash.util import pkg_dir


sibcoin_stylesheet = """

/**********************/
/* SIBCOIN Evolution CSS */
/*
0. OSX Reset
1. Navigation Bar
2. Editable Fields, Labels
3. Containers
4. File Menu, Toolbar
5. Buttons, Spinners, Dropdown
6. Table Headers
7. Scroll Bar
8. Tree View
9. Dialog Boxes
*/
/**********************/


/**********************/
/* 0. OSX Reset */

QWidget { /* Set default style for QWidget, override in following statements */
    border: 0;
    selection-color: #fff;
    selection-background-color: #818181;
}

QGroupBox {
    margin-top: 1em;
    color:#333;
}

QGroupBox::title {
    subcontrol-origin: margin;
}

/**********************/
/* 1. Navigation Bar */

#main_window_nav_bar {
    border:0;
}

#main_window_nav_bar > QStackedWidget {
    border-top: 2px solid #FF0000;
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));
}

#main_window_nav_bar > QTabBar{
    color: #fff;
    border:0;
}

#main_window_nav_bar > QTabBar {
    background: url(electrum_sibcoin/gui/icons/navlogo.png) no-repeat left top;
}

QTabWidget#main_window_nav_bar::tab-bar {
    alignment: left;
}

QTabWidget#main_window_nav_bar::pane {
    position: absolute;
}

#main_window_nav_bar > QTabBar::tab {
    background-color:#333397;
    color:#fff;
    min-height: 44px;
    padding-left:1em;
    padding-right:1em;
}

#main_window_nav_bar > QTabBar::tab:first {
    border-left: 0 solid #fff;
    margin-left: 60px;
}

#main_window_nav_bar > QTabBar::tab:last {
    border-right: 0 solid #fff;
}

#main_window_nav_bar > QTabBar::tab:selected, #main_window_nav_bar > QTabBar::tab:hover {
    background-color:#25256f;
    color:#fff;
}


/**********************/
/* 2. Editable Fields and Labels */

QCheckBox { /* Checkbox Labels */
    color:#333333;
    background-color:transparent;
}

QCheckBox:hover {
    background-color:transparent;
}

QCheckBox {
    spacing: 5px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
}

QCheckBox::indicator:unchecked {
    image:url('electrum_sibcoin/gui/icons/checkbox/unchecked.png');
}

QCheckBox::indicator:unchecked:disabled {
    image:url('electrum_sibcoin/gui/icons/checkbox/unchecked_disabled.png');
}

QCheckBox::indicator:unchecked:pressed {
    image:url('electrum_sibcoin/gui/icons/checkbox/checked.png');
}

QCheckBox::indicator:checked {
    image:url('electrum_sibcoin/gui/icons/checkbox/checked.png');
}

QCheckBox::indicator:checked:disabled {
    image:url('electrum_sibcoin/gui/icons/checkbox/checked_disabled.png');
}

QCheckBox::indicator:checked:pressed {
    image:url('electrum_sibcoin/gui/icons/checkbox/unchecked.png');
}

QCheckBox::indicator:indeterminate {
    image:url('electrum_sibcoin/gui/icons/checkbox/indeterminate.png');
}

QCheckBox::indicator:indeterminate:disabled {
    image:url('electrum_sibcoin/gui/icons/checkbox/indeterminate_disabled.png');
}

QCheckBox::indicator:indeterminate:pressed {
    image:url('electrum_sibcoin/gui/icons/checkbox/checked.png');
}

QRadioButton {
    padding: 2px;
    spacing: 5px;
    color: #333;
}

QRadioButton::indicator {
    width: 16px;
    height: 16px;
}

QRadioButton::indicator::unchecked {
    image:url('electrum_sibcoin/gui/icons/radio/unchecked.png');
}

QRadioButton::indicator:unchecked:disabled {
    image:url('electrum_sibcoin/gui/icons/radio/unchecked_disabled.png');
}

QRadioButton::indicator:unchecked:pressed {
    image:url('electrum_sibcoin/gui/icons/radio/checked.png');
}

QRadioButton::indicator::checked {
    image:url('electrum_sibcoin/gui/icons/radio/checked.png');
}

QRadioButton::indicator:checked:disabled {
    image:url('electrum_sibcoin/gui/icons/radio/checked_disabled.png');
}

QRadioButton::indicator:checked:pressed {
    image:url('electrum_sibcoin/gui/icons/radio/checked.png');
}

ScanQRTextEdit, ShowQRTextEdit, ButtonsTextEdit {
    color:#333;
    background-color:#FFFFFF;
    border: 1px solid #2e2ed6;
}

QValidatedLineEdit, QLineEdit, PayToEdit { /* Text Entry Fields */
    border: 1px solid #2e2ed6;
    outline:0;
    padding: 5px 3px;
    background-color:#fcfcfc;
    color:#818181;
}

PayToEdit {
    padding: 6px;
}

ButtonsLineEdit {
    color:#818181;
    background: #fff;
}

QLabel {
    color: #333;
}


/**********************/
/* 3. Containers */


/* Wallet Container */
#main_window_container {
    background: #333397;
    color: #fff;
}


/* History Container */
#history_container {
    margin-top: 0;
}


/* Send Container */
#send_container {
    margin-top: 0;
}

#send_container > QLabel {
    margin-left:10px;
    min-width:150px;
}


/* Receive Container */
#receive_container {
    margin-top: 0;
}

#receive_container > QLabel {
    margin-left:10px;
    min-width:150px;
}


/* Addressses Container */
#addresses_container {
    margin-top: 0;
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));
}


/* Contacts Container */
#contacts_container, #utxo_container {
    margin-top: 0;
}


/* Console Container */
#console_container {
    margin-top: 0;
    color:#818181;
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));
}


/* Balance Label */
#main_window_balance {
    color:#ffffff;
    font-weight:bold;
    margin-left:10px;
}


/**********************/
/* 4. File Menu, Toolbar */

#main_window_container QMenuBar {
    color: #fff;
}

QMenuBar {
    background-color:#fff;
}

QMenuBar::item {
    background-color:#fff;
    color:#333;
}

QMenuBar::item:selected {
    background-color:#f8f6f6;
}

QMenu {
    background-color:#f8f6f6;
    border:1px solid #2B2727;
}

QMenu::item {
    color:#333;
}

QMenu::item:selected {
    background-color:#f2f0f0;
    color:#333;
}

QToolBar {
    background-color:#3398CC;
    border:0px solid #000;
    padding:0;
    margin:0;
}

QToolBar > QToolButton {
    background-color:#3398CC;
    border:0px solid #333;
    min-height:2.5em;
    padding: 0em 1em;
    font-weight:bold;
    color:#fff;
}

QToolBar > QToolButton:checked {
    background-color:#fff;
    color:#333;
    font-weight:bold;
}

QMessageBox {
    background-color:#F8F6F6;
}


QLabel { /* Base Text Size & Color */
    color:#333333;
}


/**********************/
/* 5. Buttons, Spinners, Dropdown */

QPushButton { /* Global Button Style */
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: .01 #5e5efd, stop: .1 #4444e7, stop: .95 #4444e7, stop: 1 #4747d5);
    border:0;
    border-radius:3px;
    color:#ffffff;
    /* font-size:12px; */
    font-weight:bold;
    padding: 7px 25px;
}

QPushButton:hover {
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: .01 #5e5efd, stop: .1 #5e5efd, stop: .95 #5e5efd, stop: 1 #4747d5);
}

QPushButton:focus {
    border:none;
    outline:none;
}

QPushButton:pressed {
    border:1px solid #f8f8f8;
}

QPushButton:disabled
{
    color: #e6e6ff;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #c0c0ff, stop: 1 #c0c0ff);
}

QStatusBar {
    color: #fff;
}

QStatusBar QPushButton:pressed {
    border:1px solid #2e2ed6;
}

QStatusBar::item {
    border: none;
}

QComboBox { /* Dropdown Menus */
    border:1px solid #2e2ed6;
    padding: 5px;
    background:#fcfcfc;
    color:#818181;
    combobox-popup: 0;
}

QComboBox::disabled {
    background:#eeeeee;
}

QComboBox::drop-down {
    width:25px;
    border:0px;
}

QComboBox::down-arrow {
    border-image: url('electrum_sibcoin/gui/icons/sibcoin_downArrow.png') 0 0 0 0 stretch stretch;
}

QComboBox QListView {
    border: 1px solid #2e2ed6;
    color: #818181;
    padding: 3px;
    background-color: #fff;
    selection-color: #fff;
    selection-background-color: #818181;
}

QAbstractSpinBox {
    border:1px solid #2e2ed6;
    padding: 5px 3px;
    background:#fcfcfc;
    color:#818181;
}

QAbstractSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width:21px;
    background:#fcfcfc;
    border-left:0px;
    border-right:1px solid #2e2ed6;
    border-top:1px solid #2e2ed6;
    border-bottom:0px;
    padding-right:1px;
    padding-left:5px;
    padding-top:2px;
}


QAbstractSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width:21px;
    background:#fcfcfc;
    border-top:0px;
    border-left:0px;
    border-right:1px solid #2e2ed6;
    border-bottom:1px solid #2e2ed6;
    padding-right:1px;
    padding-left:5px;
    padding-bottom:2px;
}

QAbstractSpinBox::up-arrow {
    image: url(electrum_sibcoin/gui/icons/sibcoin_upArrow_small.png);
    width: 10px;
    height: 10px;
}

QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {
    image: url(electrum_sibcoin/gui/icons/sibcoin_upArrow_small_disabled.png);
}

QAbstractSpinBox::down-arrow {
    image: url(electrum_sibcoin/gui/icons/sibcoin_downArrow_small.png);
    width: 10px;
    height: 10px;
}

QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {
    image: url(electrum_sibcoin/gui/icons/sibcoin_downArrow_small_disabled.png);
}

QSlider::groove:horizontal {
    border: 1px solid #2e2ed6;
    background: white;
    height: 10px;
}

QSlider::sub-page:horizontal {
    background-color: #818181;
    border: 1px solid #2e2ed6;
    height: 10px;
}

QSlider::add-page:horizontal {
    background: #fff;
    border: 1px solid #2e2ed6;
    height: 10px;
}

QSlider::handle:horizontal {
    background-color: #2e2ed6;
    border: 1px solid #2e2ed6;
    width: 13px;
    margin-top: -2px;
    margin-bottom: -2px;
    border-radius: 2px;
}

/**********************/
/* 6. Table Headers */

QHeaderView { /* Table Header */
    background-color:transparent;
    border:0px;

}

QHeaderView::section { /* Table Header Sections */
    qproperty-alignment:center;
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.25, stop: 0 #5a5ae7, stop: 1 #5a5ae7);
    color:#fff;
    font-weight:bold;
    font-size:11px;
    outline:0;
    border:0;
    border-right:1px solid #5d69f0;
    padding-left:2px;
    padding-right:10px;
    padding-top:1px;
    padding-bottom:1px;
}

#contacts_container QHeaderView::section {
}

#contacts_container QHeaderView::section:first {
    padding-left:50px;
    padding-right:40px;
}

QHeaderView::section:last {
    border-right: 0px solid #d7d7d7;
}


/**********************/
/* 7. Scroll Bar */

QAbstractScrollArea::corner {
    background: none;
    border: none;
}

QScrollBar { /* Scroll Bar */
}

QScrollBar:vertical { /* Vertical Scroll Bar Attributes */
    border:0;
    background:#ffffff;
    width:18px;
    margin: 18px 0px 18px 0px;
}

QScrollBar:horizontal { /* Horizontal Scroll Bar Attributes */
    border:0;
    background:#ffffff;
    height:18px;
    margin: 0px 18px 0px 18px;
}


QScrollBar::handle:vertical { /* Scroll Bar Slider - vertical */
    background:#e0e0e0;
    min-height:10px;
}

QScrollBar::handle:horizontal { /* Scroll Bar Slider - horizontal */
    background:#e0e0e0;
    min-width:10px;
}

QScrollBar::add-page, QScrollBar::sub-page { /* Scroll Bar Background */
    background:#F8F6F6;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical, QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { /* Define Arrow Button Dimensions */
    background-color:#F8F6F6;
    border: 1px solid #f2f0f0;
    width:16px;
    height:16px;
}

QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed {
    background-color:#e0e0e0;
}

QScrollBar::sub-line:vertical { /* Vertical - top button position */
    subcontrol-position:top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical { /* Vertical - bottom button position */
    subcontrol-position:bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal { /* Vertical - left button position */
    subcontrol-position:left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal { /* Vertical - right button position */
    subcontrol-position:right;
    subcontrol-origin: margin;
}

QScrollBar:up-arrow, QScrollBar:down-arrow, QScrollBar:left-arrow, QScrollBar:right-arrow { /* Arrows Icon */
    width:10px;
    height:10px;
}

QScrollBar:up-arrow {
    background-image: url('electrum_sibcoin/gui/icons/sibcoin_upArrow_small.png');
}

QScrollBar:down-arrow {
    background-image: url('electrum_sibcoin/gui/icons/sibcoin_downArrow_small.png');
}

QScrollBar:left-arrow {
    background-image: url('electrum_sibcoin/gui/icons/sibcoin_leftArrow_small.png');
}

QScrollBar:right-arrow {
    background-image: url('electrum_sibcoin/gui/icons/sibcoin_rightArrow_small.png');
}


/**********************/
/* 8. Tree Widget */

QTreeView, QTreeWidget, QListWidget, QTableView, QTextEdit  {
    border: 0px;
    color:#818181;
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));
}

QTreeView QLineEdit, QTreeWidget QLineEdit {
    min-height: 0;
    padding: 0;
}

QListWidget, QTableView, QTextEdit, QDialog QTreeWidget, QDialog QTreeView {
    border: 1px solid #2e2ed6;
}

#send_container QTreeWidget, #receive_container QTreeWidget,
#send_container QTreeView, #receive_container QTreeView {
    border: 1px solid #2e2ed6;
    background-color: #fff;
}

QTableView {
    background-color: #fff;
}

QTreeView::branch {
    color: #818181;
    background-color: transparent;
}

QTreeView::branch:selected {
    background-color:#808080;
}

QTreeView::item:selected, QTreeView::item:selected:active {
    color: #fff;
    background-color:#808080;
}

/**********************/
/* 9. Dialog Boxes */

QDialog {
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(233, 233, 233, 255));
}

QDialog QScrollArea {
    background: transparent;
}

QDialog QTabWidget {
    border-bottom:1px solid #333;
}

QDialog QTabWidget::pane {
    border: 1px solid #d7d7d7;
    color:#818181;
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));
}

QDialog QTabWidget QTabBar::tab {
    background-color:#f2f0f0;
    color:#333;
    padding-left:10px;
    padding-right:10px;
    padding-top:5px;
    padding-bottom:5px;
    border-top: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:first {
    border-left: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:last {
    border-right: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:selected, QDialog QTabWidget QTabBar::tab:hover {
    background-color:#ffffff;
    color:#333;
}

QDialog HelpButton {
    background-color: transparent;
    color:#333;
}

QDialog QWidget { /* Remove Annoying Focus Rectangle */
    outline: 0;
}

QDialog #settings_tab {
    min-width: 600px;
}

MasternodeDialog {
    min-height: 650px;
}

MasternodeDialog #dip3_warn {
    color: #FF0000;
}

Dip3TabWidget {
    border-bottom:1px solid #333;
}

Dip3TabWidget::pane {
    border: 1px solid #d7d7d7;
    color:#818181;
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));
}

Dip3TabWidget Dip3TabBar::tab {
    background-color:#f2f0f0;
    color:#333;
    padding-left:10px;
    padding-right:10px;
    padding-top:5px;
    padding-bottom:5px;
    border-top: 1px solid #d7d7d7;
}

Dip3TabWidget Dip3TabBar::tab:first {
    border-left: 1px solid #d7d7d7;
}

Dip3TabWidget Dip3TabBar::tab:last {
    border-right: 1px solid #d7d7d7;
}

Dip3TabWidget Dip3TabBar::tab:selected, Dip3TabWidget Dip3TabBar::tab:hover {
    background-color:#ffffff;
    color:#333;
}

QWizard {
    background-color:#f2f0f0;
}

QWizard #err-label {
    color: #800000;
}
QWizard #info-label {
    color: #008000;
}
"""


pkg_dir_for_css = pkg_dir.replace(os.sep, '/')
sibcoin_stylesheet = sibcoin_stylesheet.replace('{pkg_dir}', '%s' % pkg_dir_for_css)
