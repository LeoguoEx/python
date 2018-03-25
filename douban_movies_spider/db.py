import pymysql
import Sqls


class DB(object):

    def __init__(self, dbhosts):
        self.dbhosts = dbhosts
        db = self.connectDB()
        self.excuteSql(db, Sqls.create_table_sql)
        self.excuteSql(db, Sqls.create_requested_urls_sql)
        self.disconnectDB(db)

    def connectDB(self):
        db = pymysql.connect(host=self.dbhosts.host, port=self.dbhosts.port, user=self.dbhosts.user,
                             password=self.dbhosts.password, database=self.dbhosts.dbname,
                             charset=self.dbhosts.charset)
        return db

    def excuteSql(self, db, sql):
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except pymysql.Warning as w:
            print("Warning : %s !!!!!" % w)
            db.rollback()
        finally:
            cursor.close()

    def disconnectDB(self, db):
        if db is not None:
            db.close