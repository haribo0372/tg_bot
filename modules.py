from request import cursor, dayz, number_para, finish_pt, prof


def days(d) -> str:
    if d == 'Monday':
        return 'monday'
    elif d == 'Tuesday':
        return 'tuesday'
    elif d == 'Wednesday':
        return 'wednesday'
    elif d == 'Thursday':
        return 'thursday'
    elif d == 'Friday':
        return 'friday'
    elif d == 'Saturday':
        return 'saturday'
    elif d == 'Sunday':
        return 'monday'


def tomorrow_day(d) -> str:
    if d == 'Monday':
        return 'tuesday'
    elif d == 'Tuesday':
        return 'wednesday'
    elif d == 'Wednesday':
        return 'thursday'
    elif d == 'Thursday':
        return 'friday'
    elif d == 'Friday':
        return 'saturday'
    elif d == 'Saturday':
        return 'monday'
    elif d == 'Sunday':
        return 'monday'


def request_day_cht(i):
    cursor.execute(
        "SELECT day, timetable_cht.subject, room_numb, start_time, full_name, prof FROM timetable_cht, "
        "teacher WHERE day = '{0}' and timetable_cht.tp = teacher.id;".format(i))
    records = list(cursor.fetchall())
    a = ""
    c = 0
    for i in range(0, 5):
        day = str(records[i][0])
        subject = str(records[i][1])
        room = str(records[i][2])
        st = str(records[i][3])
        name_t = str(records[i][4])
        profile = str(records[i][5])
        if c == 0:
            a += '<b>{0}</b>\n'.format(dayz(day))
            c += 1
        while day:
            subject = prof(subject)
            num_para = number_para(st)
            finish_para = finish_pt(st)
            if subject == 'None' or room == 'None':
                subject = 'Нет пары'
                a += '<i>' + str(num_para) + ". {0}{1}</i>\n{2}\n\n".format(st, finish_para, subject)
                i += 1
                if st == '17:15':
                    a += '\n'
                break
            else:
                a += '<i>' + str(num_para) + ". {0}{1}</i>\n{2}\n{5}\n{4} в кабинете № {3}\n\n".format(st,
                                                                                                       finish_para,
                                                                                                       subject,
                                                                                                       room,
                                                                                                       profile,
                                                                                                       name_t)
                i += 1
                if st == '17:15':
                    a += '\n'
                break
    return a


def request_day_necht(i):
    cursor.execute(
        "SELECT day, timetable_necht.subject, room_numb, start_time, full_name, prof FROM timetable_necht, "
        "teacher WHERE day = '{0}' and timetable_necht.tp = teacher.id;".format(i))
    records = list(cursor.fetchall())
    a = ""
    c = 0
    for i in range(0, 5):
        day = str(records[i][0])
        subject = str(records[i][1])
        room = str(records[i][2])
        st = str(records[i][3])
        name_t = str(records[i][4])
        profile = str(records[i][5])
        if c == 0:
            a += '<b>{0}</b>\n'.format(dayz(day))
            c += 1
        while day:
            subject = prof(subject)
            num_para = number_para(st)
            finish_para = finish_pt(st)
            if subject == 'None' or room == 'None':
                subject = 'Нет пары'
                a += '<i>' + str(num_para) + ". {0}{1}</i>\n{2}\n\n".format(st, finish_para, subject)
                i += 1
                if st == '17:15':
                    a += '\n'
                break
            else:
                a += '<i>' + str(num_para) + ". {0}{1}</i>\n{2}\n{5}\n{4} в кабинете № {3}\n\n".format(st,
                                                                                                       finish_para,
                                                                                                       subject,
                                                                                                       room,
                                                                                                       profile,
                                                                                                       name_t)
                i += 1
                if st == '17:15':
                    a += '\n'
                break
    return a
