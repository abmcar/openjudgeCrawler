import pymysql

if __name__ == '__main__':
    db = pymysql.connect(host="db.abmcar.top", port=10019, user="nyist", password="password=NULL0",
                         database="NYIST_ACM")
    cursor = db.cursor()
