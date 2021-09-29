import pymysql
import student

if __name__ == '__main__':
    db = pymysql.connect(host="db.abmcar.top", port=10019, user="nyist", password="password=NULL0",
                         database="NYIST_ACM")
    cursor = db.cursor()
    sqlQueue = "select * from ranking"
    cursor.execute(sqlQueue)
    results = cursor.fetchall()
    studentList = []
    for row in results:
        print(row)
        nowStudent = student.Student(row[0], row[1])

        nowStudent.name_zzulioj = row[9]
        nowStudent.set_solve_zzulioj()
        sql_update = 'update ranking set solve_zzulioj=\'' + str(nowStudent.solve_zzulioj) + '\' where sno=\'' + str(
            nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        nowStudent.name_nowcoder = row[11]
        nowStudent.set_solve_nowcoder()
        sql_update = 'update ranking set solve_nowcoder=\'' + str(nowStudent.solve_nowcoder) + '\' where sno=\'' + str(
            nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        nowStudent.name_codeforces = row[10]
        nowStudent.set_solve_codeforces()
        nowStudent.set_rating_codeforces()
        sql_update = 'update ranking set solve_codeforces=\'' + str(
            nowStudent.solve_codeforces) + '\' where sno=\'' + str(nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()
        sql_update = 'update ranking set rating_codeforces=\'' + str(
            nowStudent.rating_codeforces) + '\' where sno=\'' + str(nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        nowStudent.get_tot_solve()
        sql_update = 'update ranking set totSolve=\'' + str(nowStudent.tot_solve) + '\' where sno=\'' + str(
            nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        # nowStudent.solve_zzulioj = zzuiloj.get_solve_num('abmcar')
        studentList.append(nowStudent)
        # print(studentList[len(studentList) - 1].tot_solve)
        # print(studentList[len(studentList) - 1].rating_codeforces)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
