# _*_ coding: utf-8 _*_
import pymysql
from Common.ReadConfig import ReadConf
from Common.Logger import Log


class Connector:
    host = ReadConf("DB", "host").read_db()
    user = ReadConf("DB", "user").read_db()
    password = ReadConf("DB", "password").read_db()
    port = ReadConf("DB", "port").read_db()
    database = ReadConf("DB", "database").read_db()
    log = Log()

    def __init__(self):
        # Define database config file
        db_data = {
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "port": int(self.port),
            "database": self.database
        }

        # Connection database and generate database cursor
        try:
            self.conn = pymysql.connect(**db_data)
            self.log.info("Connection database success")
            self.cur = self.conn.cursor()
        except Exception as e:
            self.log.error(e)

    def execute_sql(self, sql):
        """
        Define a function to execute sql grammar and return the result
        :param sql:
        :return: result
        """
        try:
            self.cur.execute(sql)
            self.log.info("Execute sql grammar success")
            result = self.cur.fetchone()

            return result
        except Exception as e:
            self.log.error(e)
            self.log.error("Execute sql fail, and the sql grammar is >> {}".format(sql))
