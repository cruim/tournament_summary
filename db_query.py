def connection_string():
    return 'pq://postgres:postgres@localhost:5432/postgres'


def insert_data_into_db(buy_in, prizepool, place, created_on, db):
    insert = db.prepare("insert into tournament_summary (buy_in, prizepool, place, created_on) values($1,$2)")
    insert(buy_in, prizepool, place, created_on)
