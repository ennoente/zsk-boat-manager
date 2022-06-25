from mysql import connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector import MySQLConnection
from models.constants import BOAT_TABLE_NAMES, BOAT_NAMES

DB_NAME = "boats"
#TABLE_NAME = "sessions"

CREATE_DATABASE_SQL = f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`"

CREATE_SESSION_TABLE_SQL = "CREATE TABLE IF NOT EXISTS `{}`(`id` int(11) NOT NULL AUTO_INCREMENT," \
                           "`trainer_name` varchar(128) NOT NULL," \
                           "`begin` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP," \
                           "`end` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP," \
                           "`comment` varchar(256)," \
                           "`amount_refueled` float(3,2) NOT NULL, PRIMARY KEY (`id`))"

INSERT_CHECK_IN_SQL = "INSERT INTO {} (trainer_name, comment, amount_refueled) " \
                      "VALUES (\"{}\", \"{}\", \"{}\")"

UPDATE_CHECK_OUT_SQL = "UPDATE {} SET `end` = CURRENT_TIMESTAMP " \
                       "WHERE `trainer_name` = \"{}\" AND `begin` = `end`"

IS_TRAINER_CURRENTLY_CHECKED_IN_SQL = "SELECT COUNT(*) FROM {} WHERE `trainer_name` = \"{}\" AND `begin` = `end`"

IS_BOAT_CURRENTLY_CHECKED_IN_SQL = "SELECT COUNT(*) FROM {} WHERE `begin` = `end`"

GET_ALL_ROWS_OF_TABLE_SQL = "SELECT * FROM {}"


class SqlManager:
    connection: MySQLConnection
    cursor: MySQLCursor

    def initialize(self):
        connection = connector.connect(
            host="db",
            user="root",
            password="root",
        )

        self.connection = connection
        self.cursor = connection.cursor()

        self.create_database_if_exists()
        for table_name in BOAT_TABLE_NAMES:
            self.create_table_if_exists(table_name=table_name)

        print("Successfully initialized mysql connection.")

    def create_database_if_exists(self):
        print("Creating database...")
        self.cursor.execute(CREATE_DATABASE_SQL)
        print(f"Created database {DB_NAME}")
        self.cursor.execute(f"USE {DB_NAME}")
        print(f"Using database '{DB_NAME}'")
        return

    def create_table_if_exists(self, table_name: str):
        print("Creating table...")
        sql = CREATE_SESSION_TABLE_SQL.format(table_name)
        self.cursor.execute(sql)
        print(f"Created table {table_name}")

    def check_in(self, boat_name, trainer_name: str, comment: str, amount_refueled: float):
        table_name = self.convert_boat_name_to_table(boat_name=boat_name)
        sql = INSERT_CHECK_IN_SQL.format(table_name, trainer_name, comment, amount_refueled)

        self.cursor.execute(sql)
        self.connection.commit()

    def check_out(self, boat_name: str, trainer_name: str):
        table_name = self.convert_boat_name_to_table(boat_name=boat_name)
        sql = UPDATE_CHECK_OUT_SQL.format(table_name, trainer_name)

        self.cursor.execute(sql)
        self.connection.commit()
        return

    def is_boat_currently_checked_in(self, boat_name: str) -> bool:
        table_name = self.convert_boat_name_to_table(boat_name=boat_name)
        sql = IS_BOAT_CURRENTLY_CHECKED_IN_SQL.format(table_name)

        self.cursor.execute(sql)
        result = self.cursor.fetchone()

        return result[0] > 0

    def is_trainer_currently_checked_in(self, trainer_name: str, boat_name: str) -> bool:
        table_name = self.convert_boat_name_to_table(boat_name=boat_name)
        sql = IS_TRAINER_CURRENTLY_CHECKED_IN_SQL.format(table_name, trainer_name)

        self.cursor.execute(sql)
        result = self.cursor.fetchone()

        return result[0] > 0

    def get_all_entries_for_boat(self, boat_name: str):
        table_name = self.convert_boat_name_to_table(boat_name=boat_name)
        sql = GET_ALL_ROWS_OF_TABLE_SQL.format(table_name)

        self.cursor.execute(sql)
        resulting_rows = self.cursor.fetchall()

        return resulting_rows

    def convert_boat_name_to_table(self, boat_name: str) -> str:
        index = BOAT_NAMES.index(boat_name)
        return BOAT_TABLE_NAMES[index]