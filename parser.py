import os
import datetime
import fnmatch
import postgresql
import db_query


DB = postgresql.open(db_query.connection_string())


file_name = "TS" + str(datetime.datetime.now().date().strftime("%Y%m%d")) + '*.txt'
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, file_name):
        file = open(file, mode='r', encoding='utf-8-sig')
        lines = file.readlines()
        file.close()
        my_dict = {}
        my_list = []
        buy_in = lines[1][9:13]
        prizepool = lines[3][19:23]
        place = lines[-3][16:17]
        date = lines[4][19:29]
        format_str = '%Y/%m/%d'
        date = datetime.datetime.strptime(date, format_str).date()
        db_query.insert_data_into_db(buy_in, prizepool, place, date, DB)

