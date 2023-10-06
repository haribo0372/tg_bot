import psycopg2
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                             QTableWidgetItem, QPushButton, QMessageBox)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._connect_to_db()
        self.setWindowTitle("SiiiiUUUU")
        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)
        self._create_shedule_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="tg_bot_db",
                                     user="postgres",
                                     password="plombier520796",
                                     host="localhost",
                                     port="5432")
        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
        self.shedule_tab_cht = QWidget()
        self.tabs.addTab(self.shedule_tab_cht, "timetable_cht")

        self.shedule_tab_necht = QWidget()
        self.tabs.addTab(self.shedule_tab_necht, "timetable_necht")

        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "teacher_subject")

        self.monday_gbox = QGroupBox("Monday")
        self.tuesday_gbox = QGroupBox("Tuesday")
        self.wednesday_gbox = QGroupBox("Wednesday")
        self.thursday_gbox = QGroupBox("Thursday")
        self.friday_gbox = QGroupBox("Friday")
        self.saturday_gbox = QGroupBox("Saturday")

        self.monday_gbox_necht = QGroupBox("Monday")
        self.tuesday_gbox_necht = QGroupBox("Tuesday")
        self.wednesday_gbox_necht = QGroupBox("Wednesday")
        self.thursday_gbox_necht = QGroupBox("Thursday")
        self.friday_gbox_necht = QGroupBox("Friday")
        self.saturday_gbox_necht = QGroupBox("Saturday")

        self.teacher_gbox = QGroupBox('Teacher')
        self.subject_gbox = QGroupBox('Subject')

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox_necht = QVBoxLayout()
        self.shbox1_necht = QHBoxLayout()
        self.shbox3_necht = QHBoxLayout()
        self.shbox2_necht = QHBoxLayout()

        self.svbox_ts = QVBoxLayout()
        self.svbox_ts1 = QHBoxLayout()
        self.svbox_ts2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox2)
        self.shbox1.addWidget(self.monday_gbox)
        self.shbox1.addWidget(self.tuesday_gbox)
        self.shbox1.addWidget(self.wednesday_gbox)
        self.shbox3.addWidget(self.thursday_gbox)
        self.shbox3.addWidget(self.friday_gbox)
        self.shbox3.addWidget(self.saturday_gbox)

        self.svbox_necht.addLayout(self.shbox1_necht)
        self.svbox_necht.addLayout(self.shbox3_necht)
        self.svbox_necht.addLayout(self.shbox2_necht)
        self.shbox1_necht.addWidget(self.monday_gbox_necht)
        self.shbox1_necht.addWidget(self.tuesday_gbox_necht)
        self.shbox1_necht.addWidget(self.wednesday_gbox_necht)
        self.shbox3_necht.addWidget(self.thursday_gbox_necht)
        self.shbox3_necht.addWidget(self.friday_gbox_necht)
        self.shbox3_necht.addWidget(self.saturday_gbox_necht)

        self.svbox_ts.addLayout(self.svbox_ts1)
        self.svbox_ts.addLayout(self.svbox_ts2)
        self.svbox_ts1.addWidget(self.teacher_gbox)
        self.svbox_ts1.addWidget(self.subject_gbox)

        self._create_monday_table()
        self._create_tuesday_table()
        self._create_wednesday_table()
        self._create_thursday_table()
        self._create_friday_table()
        self._create_saturday_table()

        self._create_monday_table_necht()
        self._create_tuesday_table_necht()
        self._create_wednesday_table_necht()
        self._create_thursday_table_necht()
        self._create_friday_table_necht()
        self._create_saturday_table_necht()

        self._create_teacher_table()
        self._create_subject_table()

        self.update_shedule_button = QPushButton("Update")
        self.update_shedule_button1 = QPushButton("Update")
        self.update_shedule_button2 = QPushButton("Update")

        self.shbox2.addWidget(self.update_shedule_button1)

        self.shbox2_necht.addWidget(self.update_shedule_button2)

        self.svbox_ts2.addWidget(self.update_shedule_button)

        self.update_shedule_button.clicked.connect(self._update_shedule)
        self.update_shedule_button1.clicked.connect(self._update_shedule)
        self.update_shedule_button2.clicked.connect(self._update_shedule)

        self.shedule_tab_cht.setLayout(self.svbox)
        self.shedule_tab_necht.setLayout(self.svbox_necht)
        self.shedule_tab.setLayout(self.svbox_ts)

    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.teacher_table.setColumnCount(6)

        self.teacher_table.setHorizontalHeaderLabels(["id", "Full_name", "prof", "Subject", "", ""])

        self._update_teacher_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.teacher_table)

        self.teacher_gbox.setLayout(self.mvbox)

    def _create_subject_table(self):
        self.subject_table = QTableWidget()
        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.subject_table.setColumnCount(2)

        self.subject_table.setHorizontalHeaderLabels(["Subject name", ""])

        self._update_subject_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.subject_table)

        self.subject_gbox.setLayout(self.mvbox)

    def _update_subject_table(self):
        self.cursor.execute("SELECT * FROM subject")
        records = list(self.cursor.fetchall())
        ri = 0
        self.subject_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            deleteButton = QPushButton("DELETE")
            self.subject_table.setItem(i, 0,
                                       QTableWidgetItem(str(r[0])))
            ri = i
            self.subject_table.setCellWidget(i, 1, deleteButton)
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_subject(num))

        insertButton = QPushButton("INSERT")

        self.subject_table.setItem(ri + 1, 0,
                                   QTableWidgetItem(str()))

        self.subject_table.setCellWidget(ri + 1, 1, insertButton)
        insertButton.clicked.connect(lambda ch, num=ri: self._insert_into_table_subject(num + 1))
        self.subject_table.resizeRowsToContents()

    def _update_teacher_table(self):
        self.cursor.execute("SELECT * FROM teacher")
        records = list(self.cursor.fetchall())
        ri = 0
        self.teacher_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            deleteButton = QPushButton('DELETE')
            self.teacher_table.setItem(i, 0,
                                       QTableWidgetItem(str(r[0])))
            self.teacher_table.setItem(i, 1,
                                       QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem(i, 2,
                                       QTableWidgetItem(str(r[2])))
            self.teacher_table.setItem(i, 3,
                                       QTableWidgetItem(str(r[3])))

            self.teacher_table.setCellWidget(i, 4, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_teacher_from_table_teacher(num))

            self.teacher_table.setCellWidget(i, 5, deleteButton)
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_teacher(num))
            ri = i

        self.teacher_table.setItem(ri + 1, 0,
                                   QTableWidgetItem(str()))
        self.teacher_table.setItem(ri + 1, 1,
                                   QTableWidgetItem(str()))
        self.teacher_table.setItem(ri + 1, 2,
                                   QTableWidgetItem(str()))
        self.teacher_table.setItem(ri + 1, 3,
                                   QTableWidgetItem(str()))

        insertButton = QPushButton('INSERT')
        self.teacher_table.setCellWidget(ri + 1, 5, insertButton)
        insertButton.clicked.connect(lambda ch, num=ri + 1: self._insert_teacher(num))
        self.teacher_table.resizeRowsToContents()

    def _change_teacher_from_table_teacher(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE teacher SET full_name = '{0}' , subject = '{1}' , prof = '{2}' "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _insert_into_table_subject(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("INSERT INTO subject (name) VALUES('{0}')".format(row[0]))
            self.conn.commit()
            self._update_subject_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_subject(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("DELETE FROM subject WHERE name = '{0}'".format(row[0]))
            self.conn.commit()
            self._update_subject_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _insert_teacher(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("INSERT INTO teacher (full_name, prof, subject) "
                                "VALUES ('{0}', '{1}', '{2}');".format(row[1], row[2], row[3]))
            self.conn.commit()
            self._update_teacher_table()
            self._update_subject_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_teacher(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("DELETE FROM teacher WHERE id = '{0}'".format(row[0]))
            self.conn.commit()
            self._update_teacher_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.monday_table.setColumnCount(6)

        self.monday_table.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)

        self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tuesday_table.setColumnCount(6)

        self.tuesday_table.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)

        self.tuesday_gbox.setLayout(self.mvbox)

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.wednesday_table.setColumnCount(6)

        self.wednesday_table.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)

        self.wednesday_gbox.setLayout(self.mvbox)

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.thursday_table.setColumnCount(6)

        self.thursday_table.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)

        self.thursday_gbox.setLayout(self.mvbox)

    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.friday_table.setColumnCount(6)

        self.friday_table.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)

        self.friday_gbox.setLayout(self.mvbox)

    def _create_saturday_table(self):
        self.saturday_table = QTableWidget()
        self.saturday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.saturday_table.setColumnCount(6)

        self.saturday_table.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_saturday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.saturday_table)

        self.saturday_gbox.setLayout(self.mvbox)

    def _update_monday_table(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_cht WHERE day='monday'")
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[1])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 4,
                                      QTableWidgetItem(str(r[4])))

            self.monday_table.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_monday(num))
        self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_cht WHERE day='tuesday'")
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.tuesday_table.setItem(i, 0,
                                       QTableWidgetItem(str(r[0])))
            self.tuesday_table.setItem(i, 1,
                                       QTableWidgetItem(str(r[1])))
            self.tuesday_table.setItem(i, 2,
                                       QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 3,
                                       QTableWidgetItem(str(r[3])))
            self.tuesday_table.setItem(i, 4,
                                       QTableWidgetItem(str(r[4])))

            self.tuesday_table.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_tuesday(num))
        self.tuesday_table.resizeRowsToContents()

    def _update_wednesday_table(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_cht WHERE day='wednesday'")
        records = list(self.cursor.fetchall())

        self.wednesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.wednesday_table.setItem(i, 0,
                                         QTableWidgetItem(str(r[0])))
            self.wednesday_table.setItem(i, 1,
                                         QTableWidgetItem(str(r[1])))
            self.wednesday_table.setItem(i, 2,
                                         QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 3,
                                         QTableWidgetItem(str(r[3])))
            self.wednesday_table.setItem(i, 4,
                                         QTableWidgetItem(str(r[4])))

            self.wednesday_table.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_wednesday(num))
        self.wednesday_table.resizeRowsToContents()

    def _update_thursday_table(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_cht WHERE day='thursday'")
        records = list(self.cursor.fetchall())

        self.thursday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.thursday_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
            self.thursday_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
            self.thursday_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 3,
                                        QTableWidgetItem(str(r[3])))
            self.thursday_table.setItem(i, 4,
                                        QTableWidgetItem(str(r[4])))

            self.thursday_table.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_thursday(num))
        self.thursday_table.resizeRowsToContents()

    def _update_friday_table(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_cht WHERE day='friday'")
        records = list(self.cursor.fetchall())

        self.friday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.friday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.friday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[1])))
            self.friday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[3])))
            self.friday_table.setItem(i, 4,
                                      QTableWidgetItem(str(r[4])))

            self.friday_table.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_friday(num))
        self.friday_table.resizeRowsToContents()

    def _update_saturday_table(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_cht WHERE day='saturday'")
        records = list(self.cursor.fetchall())

        self.saturday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.saturday_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
            self.saturday_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
            self.saturday_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[2])))
            self.saturday_table.setItem(i, 3,
                                        QTableWidgetItem(str(r[3])))
            self.saturday_table.setItem(i, 4,
                                        QTableWidgetItem(str(r[4])))

            self.saturday_table.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_saturday(num))
        self.saturday_table.resizeRowsToContents()

    def _change_day_from_table_monday(self, rowNum):
        row = list()
        for i in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_cht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' , "
                                "tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_tuesday(self, rowNum):
        row = list()
        for i in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.tuesday_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_cht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' , "
                                "tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_wednesday(self, rowNum):
        row = list()
        for i in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_cht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' , "
                                "tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_thursday(self, rowNum):
        row = list()
        for i in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_cht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' , "
                                "tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_friday(self, rowNum):
        row = list()
        for i in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_cht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' , "
                                "tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_saturday(self, rowNum):
        row = list()
        for i in range(self.saturday_table.columnCount()):
            try:
                row.append(self.saturday_table.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_cht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' , "
                                "tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _create_monday_table_necht(self):
        self.monday_table_necht = QTableWidget()
        self.monday_table_necht.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.monday_table_necht.setColumnCount(6)

        self.monday_table_necht.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_monday_table_necht()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table_necht)

        self.monday_gbox_necht.setLayout(self.mvbox)

    def _create_tuesday_table_necht(self):
        self.tuesday_table_necht = QTableWidget()
        self.tuesday_table_necht.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tuesday_table_necht.setColumnCount(6)

        self.tuesday_table_necht.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_tuesday_table_necht()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table_necht)

        self.tuesday_gbox_necht.setLayout(self.mvbox)

    def _create_wednesday_table_necht(self):
        self.wednesday_table_necht = QTableWidget()
        self.wednesday_table_necht.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.wednesday_table_necht.setColumnCount(6)

        self.wednesday_table_necht.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_wednesday_table_necht()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table_necht)

        self.wednesday_gbox_necht.setLayout(self.mvbox)

    def _create_thursday_table_necht(self):
        self.thursday_table_necht = QTableWidget()
        self.thursday_table_necht.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.thursday_table_necht.setColumnCount(6)

        self.thursday_table_necht.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_thursday_table_necht()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table_necht)

        self.thursday_gbox_necht.setLayout(self.mvbox)

    def _create_friday_table_necht(self):
        self.friday_table_necht = QTableWidget()
        self.friday_table_necht.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.friday_table_necht.setColumnCount(6)

        self.friday_table_necht.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_friday_table_necht()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table_necht)

        self.friday_gbox_necht.setLayout(self.mvbox)

    def _create_saturday_table_necht(self):
        self.saturday_table_necht = QTableWidget()
        self.saturday_table_necht.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.saturday_table_necht.setColumnCount(6)

        self.saturday_table_necht.setHorizontalHeaderLabels(["id", "Subject", "Time", "Room_numb", "Teacher", ""])

        self._update_saturday_table_necht()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.saturday_table_necht)

        self.saturday_gbox_necht.setLayout(self.mvbox)

    def _update_monday_table_necht(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_necht WHERE day='monday'")
        records = list(self.cursor.fetchall())

        self.monday_table_necht.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.monday_table_necht.setItem(i, 0,
                                            QTableWidgetItem(str(r[0])))
            self.monday_table_necht.setItem(i, 1,
                                            QTableWidgetItem(str(r[1])))
            self.monday_table_necht.setItem(i, 2,
                                            QTableWidgetItem(str(r[2])))
            self.monday_table_necht.setItem(i, 3,
                                            QTableWidgetItem(str(r[3])))
            self.monday_table_necht.setItem(i, 4,
                                            QTableWidgetItem(str(r[4])))

            self.monday_table_necht.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_monday_necht(num))
        self.monday_table_necht.resizeRowsToContents()

    def _update_tuesday_table_necht(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_necht WHERE day='tuesday'")
        records = list(self.cursor.fetchall())

        self.tuesday_table_necht.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.tuesday_table_necht.setItem(i, 0,
                                             QTableWidgetItem(str(r[0])))
            self.tuesday_table_necht.setItem(i, 1,
                                             QTableWidgetItem(str(r[1])))
            self.tuesday_table_necht.setItem(i, 2,
                                             QTableWidgetItem(str(r[2])))
            self.tuesday_table_necht.setItem(i, 3,
                                             QTableWidgetItem(str(r[3])))
            self.tuesday_table_necht.setItem(i, 4,
                                             QTableWidgetItem(str(r[4])))

            self.tuesday_table_necht.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_tuesday_necht(num))
        self.tuesday_table_necht.resizeRowsToContents()

    def _update_wednesday_table_necht(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_necht WHERE day='wednesday'")
        records = list(self.cursor.fetchall())

        self.wednesday_table_necht.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.wednesday_table_necht.setItem(i, 0,
                                               QTableWidgetItem(str(r[0])))
            self.wednesday_table_necht.setItem(i, 1,
                                               QTableWidgetItem(str(r[1])))
            self.wednesday_table_necht.setItem(i, 2,
                                               QTableWidgetItem(str(r[2])))
            self.wednesday_table_necht.setItem(i, 3,
                                               QTableWidgetItem(str(r[3])))
            self.wednesday_table_necht.setItem(i, 4,
                                               QTableWidgetItem(str(r[4])))

            self.wednesday_table_necht.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_wednesday_necht(num))
        self.wednesday_table_necht.resizeRowsToContents()

    def _update_thursday_table_necht(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_necht WHERE day='thursday'")
        records = list(self.cursor.fetchall())

        self.thursday_table_necht.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.thursday_table_necht.setItem(i, 0,
                                              QTableWidgetItem(str(r[0])))
            self.thursday_table_necht.setItem(i, 1,
                                              QTableWidgetItem(str(r[1])))
            self.thursday_table_necht.setItem(i, 2,
                                              QTableWidgetItem(str(r[2])))
            self.thursday_table_necht.setItem(i, 3,
                                              QTableWidgetItem(str(r[3])))
            self.thursday_table_necht.setItem(i, 4,
                                              QTableWidgetItem(str(r[4])))

            self.thursday_table_necht.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_thursday_necht(num))
        self.thursday_table_necht.resizeRowsToContents()

    def _update_friday_table_necht(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_necht WHERE day='friday'")
        records = list(self.cursor.fetchall())

        self.friday_table_necht.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.friday_table_necht.setItem(i, 0,
                                            QTableWidgetItem(str(r[0])))
            self.friday_table_necht.setItem(i, 1,
                                            QTableWidgetItem(str(r[1])))
            self.friday_table_necht.setItem(i, 2,
                                            QTableWidgetItem(str(r[2])))
            self.friday_table_necht.setItem(i, 3,
                                            QTableWidgetItem(str(r[3])))
            self.friday_table_necht.setItem(i, 4,
                                            QTableWidgetItem(str(r[4])))

            self.friday_table_necht.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_friday_necht(num))
        self.friday_table_necht.resizeRowsToContents()

    def _update_saturday_table_necht(self):
        self.cursor.execute("SELECT id, subject, start_time, room_numb, tp FROM timetable_necht WHERE day='saturday'")
        records = list(self.cursor.fetchall())

        self.saturday_table_necht.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            joinButton = QPushButton("Join")
            self.saturday_table_necht.setItem(i, 0,
                                              QTableWidgetItem(str(r[0])))
            self.saturday_table_necht.setItem(i, 1,
                                              QTableWidgetItem(str(r[1])))
            self.saturday_table_necht.setItem(i, 2,
                                              QTableWidgetItem(str(r[2])))
            self.saturday_table_necht.setItem(i, 3,
                                              QTableWidgetItem(str(r[3])))
            self.saturday_table_necht.setItem(i, 4,
                                              QTableWidgetItem(str(r[4])))

            self.saturday_table_necht.setCellWidget(i, 5, joinButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table_saturday_necht(num))
        self.saturday_table_necht.resizeRowsToContents()

    def _change_day_from_table_monday_necht(self, rowNum):
        row = list()
        for i in range(self.monday_table_necht.columnCount()):
            try:
                row.append(self.monday_table_necht.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_necht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' "
                                ", tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_tuesday_necht(self, rowNum):
        row = list()
        for i in range(self.tuesday_table_necht.columnCount()):
            try:
                row.append(self.tuesday_table_necht.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_necht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' "
                                ", tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_wednesday_necht(self, rowNum):
        row = list()
        for i in range(self.wednesday_table_necht.columnCount()):
            try:
                row.append(self.wednesday_table_necht.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_necht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' "
                                ", tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_thursday_necht(self, rowNum):
        row = list()
        for i in range(self.thursday_table_necht.columnCount()):
            try:
                row.append(self.thursday_table_necht.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_necht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' "
                                ", tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_friday_necht(self, rowNum):
        row = list()
        for i in range(self.friday_table_necht.columnCount()):
            try:
                row.append(self.friday_table_necht.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_necht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' "
                                ", tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table_saturday_necht(self, rowNum):
        row = list()
        for i in range(self.saturday_table_necht.columnCount()):
            try:
                row.append(self.saturday_table_necht.item(rowNum, i).text())

            except:
                row.append(None)
        try:
            print(row)
            self.cursor.execute("UPDATE timetable_necht SET  subject = '{0}' , room_numb = '{1}' , start_time = '{2}' "
                                ", tp = {4} "
                                "WHERE id = {3}".format(row[1], row[3], row[2], int(row[0]), int(row[4])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _update_shedule(self):
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()
        self._update_saturday_table()

        self._update_monday_table_necht()
        self._update_tuesday_table_necht()
        self._update_wednesday_table_necht()
        self._update_thursday_table_necht()
        self._update_friday_table_necht()
        self._update_saturday_table_necht()

        self._update_teacher_table()
        self._update_subject_table()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
