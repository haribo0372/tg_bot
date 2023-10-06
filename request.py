import psycopg2


def prof(a):
    p = None
    if a == 'devops':
        p = 'DevOps'
    elif a == 'pp':
        p = 'Проектный практикум'
    elif a == 'bd':
        p = 'Математические основы баз данных'
    elif a == 'english':
        p = 'Иностранный язык'
    elif a == 'fiziks':
        p = 'Физика'
    elif a == 'fizkult':
        p = 'Игровые виды спорта'
    elif a == 'vvit':
        p = 'Введение в информационные технологии'
    elif a == 'history':
        p = 'История'
    elif a == 'math':
        p = 'Высшая математика'
    else:
        p = 'None'
    return p


def number_para(t) -> int:
    if t == '09:30':
        return 1
    elif t == '11:20':
        return 2
    elif t == '13:10':
        return 3
    elif t == '15:25':
        return 4
    elif t == '17:15':
        return 5


def dayz(d) -> str:
    if d == 'monday':
        return 'ПОНЕДЕЛЬНИК'
    elif d == 'tuesday':
        return 'ВТОРНИК'
    elif d == 'wednesday':
        return 'СРЕДА'
    elif d == 'thursday':
        return 'ЧЕТВЕРГ'
    elif d == 'friday':
        return 'ПЯТНИЦА'
    elif d == 'saturday':
        return 'СУББОТА'


def finish_pt(t) -> str:
    if t == '09:30':
        return ' - 11:05'
    elif t == '11:20':
        return ' - 12:55'
    elif t == '13:10':
        return ' - 14:45'
    elif t == '15:25':
        return ' - 17:00'
    elif t == '17:15':
        return ' - 18:50'


conn = psycopg2.connect(database="tg_bot_db",
                        user="postgres",
                        password="plombier520796",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

cursor.execute("SELECT day, timetable_cht.subject, room_numb, start_time, full_name, prof FROM timetable_cht, "
               "teacher WHERE timetable_cht.tp = teacher.id;")
records = list(cursor.fetchall())
str_cht = ""
count = 0
s = [0, 5, 10, 15, 20, 25]
for i in range(0, 30):
    day = str(records[i][0])
    subject = str(records[i][1])
    room = str(records[i][2])
    st = str(records[i][3])
    name_t = str(records[i][4])
    profile = str(records[i][5])
    for numb in s:
        if count == numb:
            str_cht += '<b>' + dayz(day) + '</b>\n'
    while day:
        subject = prof(subject)
        num_para = number_para(st)
        finish_para = finish_pt(st)
        if subject == 'None' or room == 'None':
            subject = 'Нет пары'
            str_cht += '<i>' + str(num_para) + ". {0}{1}</i>\n{2}\n\n".format(st, finish_para, subject)
            i += 1
            count += 1
            if st == '17:15':
                str_cht += '\n'
            break
        else:
            str_cht += '<i>' + str(num_para) + ". {0}{1}</i>\n{2}\n{5}\n{4} в кабинете № {3}\n\n".format(st,
                                                                                                         finish_para,
                                                                                                         subject,
                                                                                                         room, profile,
                                                                                                         name_t)
            i += 1
            count += 1
            if st == '17:15':
                str_cht += '\n'
            break

cursor.execute("SELECT day, timetable_necht.subject, room_numb, start_time, full_name, prof FROM "
               "timetable_necht,"
               "teacher WHERE timetable_necht.tp = teacher.id;")
records = list(cursor.fetchall())
str_necht = ""
count = 0
s = [0, 5, 10, 15, 20, 25]
for i in range(0, 30):
    day = str(records[i][0])
    subject = str(records[i][1])
    room = str(records[i][2])
    st = str(records[i][3])
    name_t = str(records[i][4])
    profile = str(records[i][5])
    for numb in s:
        if count == numb:
            str_necht += '<b>' + dayz(day) + '</b>\n'
    while day:
        subject = prof(subject)
        num_para = number_para(st)
        finish_para = finish_pt(st)
        if subject == 'None' or room == 'None':
            subject = 'Нет пары'
            str_necht += '<i>' + str(num_para) + ". {0}{1}</i>\n{2}\n\n".format(st, finish_para, subject)
            i += 1
            count += 1
            if st == '17:15':
                str_necht += '\n'
            break
        else:
            str_necht += '<i>' + str(num_para) + ". {0}{1}</i>\n{2}\n{5}\n{4} в кабинете № {3}\n\n".format(st,
                                                                                                           finish_para,
                                                                                                           subject,
                                                                                                           room,
                                                                                                           profile,
                                                                                                           name_t)
            i += 1
            count += 1
            if st == '17:15':
                str_necht += '\n'
            break
