from openjudgeCrawler.util import crawlerUtil


class Student:
    def __init__(self, sno, name):
        self.solve_zzulioj = None
        self.name_zzulioj = None
        self.solve_nyoj = None
        self.name_nyoj = None
        self.solve_nowcoder = None
        self.name_nowcoder = None
        self.solve_codeforces = None
        self.rating_codeforces = None
        self.name_codeforces = None
        self.sno = sno
        self.name = name

    def set_solve_zzulioj(self):
        if self.name_zzulioj is not None:
            self.solve_zzulioj = crawlerUtil.get_zzulioj_solve(self.name_zzulioj)


def test():
    print("test")
