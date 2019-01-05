import os
import datetime
import fnmatch
import postgresql
import db_query
import folder_path


DB = postgresql.open(db_query.connection_string())
FOLDER_PATH = folder_path.folder_path()


def convert_buy_in(buy_in):
    if buy_in == '0.23':
        buy_in = '0.25'
    return buy_in


def parser():
    try:
        file_name = "TS" + str(datetime.datetime.now().date().strftime("%Y%m%d")) + '*.txt'
        for file in os.listdir(FOLDER_PATH):
            if fnmatch.fnmatch(file, file_name):
                file = open(os.path.join(FOLDER_PATH, file), mode='r', encoding='utf-8-sig')
                lines = file.readlines()
                file.close()
                buy_in = convert_buy_in(lines[1][9:13])
                prizepool = lines[3][19:23]
                place = lines[-3][16:17]
                date = lines[4][19:29]
                format_str = '%Y/%m/%d'
                date = datetime.datetime.strptime(date, format_str).date()
                try:
                    int(place)
                except ValueError:
                    continue
                db_query.insert_data_into_db(buy_in, prizepool, place, date, DB)
    except Exception as e:
        print(e)



parser()





