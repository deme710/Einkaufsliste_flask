import pymysql.cursors


def get_items():
    """
    Read a sql database and return the list of
    to-do items.
    """
    # database connection
    connection = pymysql.connect(host="sql.freedb.tech",
                                 user="freedb_heroku-app",
                                 passwd="!3%5tex9Y9pf25Y",
                                 database="freedb_Einkaufsliste",
                                 cursorclass=pymysql.cursors.DictCursor)

    old_items = []
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `item` FROM `Einkaufsliste`"
            cursor.execute(sql)
            old_items_raw = cursor.fetchall()
            for dictionary in old_items_raw:
                old_items.append(dictionary["item"])
    return old_items


def write_items(items_arg):
    """" Write the to-do items list into the sql database."""
    # database connection
    connection = pymysql.connect(host="sql.freedb.tech",
                                 user="freedb_heroku-app",
                                 passwd="!3%5tex9Y9pf25Y",
                                 database="freedb_Einkaufsliste",
                                 cursorclass=pymysql.cursors.DictCursor)

    items_sql = []
    for index, item in zip(range(0, len(items_arg)), items_arg):
        buffer = [index, item]
        items_sql.append(buffer)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Einkaufsliste")
            cursor.executemany("INSERT INTO Einkaufsliste(id, item) VALUES (%s, %s)",
                               items_sql)
            connection.commit()


if __name__ == "__main__":
    print("Hello")
    # database connection
    connection = pymysql.connect(host="sql.freedb.tech",
                                 user="freedb_heroku-app",
                                 passwd="!3%5tex9Y9pf25Y",
                                 database="freedb_Einkaufsliste",
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `id`, `item` FROM `Einkaufsliste`"
            cursor.execute(sql)
            print(cursor.fetchall())
