import pymysql
import student
import json

now_json = {
    "code": 0,
    "msg": "",
    "count": 300,
    "data": [
    ]
}

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

        nowStudent.name_nyoj = row[8]
        nowStudent.set_solve_nyoj()
        sql_update = 'update ranking set solve_nyoj=\'' + str(nowStudent.solve_nyoj) + '\' where sno=\'' + str(
            nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        nowStudent.name_fuquan = row[12]
        # nowStudent.set_solve_fuquan()
        sql_update = 'update ranking set solve_fuquan=\'' + str(nowStudent.solve_fuquan) + '\' where sno=\'' + str(
            nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        nowStudent.name_vjudge = row[15]
        nowStudent.set_solve_vjudge()
        sql_update = 'update ranking set solve_vjudge=\'' + str(nowStudent.solve_vjudge) + '\' where sno=\'' + str(
            nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        nowStudent.name_luogu = row[16]
        nowStudent.set_solve_luogu()
        sql_update = 'update ranking set solve_luogu=\'' + str(nowStudent.solve_luogu) + '\' where sno=\'' + str(
            nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        nowStudent.name_jzoj = row[19]
        nowStudent.set_solve_jzoj()
        sql_update = 'update ranking set solve_jzoj=\'' + str(nowStudent.solve_jzoj) + '\' where sno=\'' + str(
            nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        nowStudent.get_tot_solve()
        sql_update = 'update ranking set totSolve=\'' + str(nowStudent.tot_solve) + '\' where sno=\'' + str(
            nowStudent.sno) + '\''
        print(sql_update)
        cursor.execute(sql_update)
        db.commit()

        now_json["data"].append({
            "sno": nowStudent.sno
            ,"name": nowStudent.name
            ,"solve_zzulioj": nowStudent.solve_zzulioj
            ,"solve_codeforces": nowStudent.solve_codeforces
            ,"rating_codeforces": nowStudent.rating_codeforces
            ,"solve_nowcoder": nowStudent.solve_nowcoder
            ,"solve_nyoj": nowStudent.solve_nyoj
            ,"solve_fuquanoj": nowStudent.solve_fuquan
            ,"solve_luogu": nowStudent.solve_luogu
            ,"solve_vjudge": nowStudent.solve_vjudge
            ,"solve_jzoj": nowStudent.solve_jzoj
            ,"totSolve": nowStudent.tot_solve
            ,"fakeName": row[14]
        })
        # nowStudent.solve_zzulioj = zzuiloj.get_solve_num('abmcar')
        studentList.append(nowStudent)
        print (json.dumps(now_json, sort_keys=True, indent=2))
        # print(studentList[len(studentList) - 1].tot_solve)
        # print(studentList[len(studentList) - 1].rating_codeforces)
    f = open(file="data.json", mode='w')
    f.write(json.dumps(now_json, sort_keys=True, indent=2))
