# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import pymysql
import student



def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    db = pymysql.connect(host="db.abmcar.top", port=10019, user="nyist", password="password=NULL0", database="NYIST_ACM")
    cursor = db.cursor()
    sqlQueue = "select * from ranking"
    cursor.execute(sqlQueue)
    results = cursor.fetchall()
    studentList = []
    for row in results:
        nowStudent = student.Student(row[0], row[1])
        nowStudent.name_zzulioj = row[9]
        nowStudent.set_solve_zzulioj()
        # nowStudent.solve_zzulioj = zzuiloj.get_solve_num('abmcar')
        studentList.append(nowStudent)
        print(row)
        print(studentList[len(studentList) - 1].solve_zzulioj)


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
