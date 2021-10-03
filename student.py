from util import crawlerUtil


class Student:
    def __init__(self, sno, name):
        self.solve_zzulioj = 0
        self.name_zzulioj = None
        self.solve_nyoj = 0
        self.name_nyoj = None
        self.solve_nowcoder = 0
        self.name_nowcoder = None
        self.solve_codeforces = 0
        self.rating_codeforces = 0
        self.name_codeforces = None
        self.solve_fuquan = 0
        self.name_fuquan = None
        self.sno = sno
        self.name = name
        self.tot_solve = 0
        self.solve_luogu = 0
        self.name_luogu = None
        self.solve_vjudge = 0
        self.name_vjudge = None

    def set_solve_zzulioj(self):
        if self.name_zzulioj is not None:
            self.solve_zzulioj = crawlerUtil.get_zzulioj_solve(self.name_zzulioj)

    def set_solve_nowcoder(self):
        if self.name_nowcoder is not None:
            self.solve_nowcoder = crawlerUtil.get_nowcoder_solve(self.name_nowcoder)

    def set_solve_codeforces(self):
        if self.name_codeforces is not None:
            self.solve_codeforces = crawlerUtil.get_codeforces_solve(self.name_codeforces)

    def set_rating_codeforces(self):
        if self.name_codeforces is not None:
            self.rating_codeforces = crawlerUtil.get_codeforces_rating(self.name_codeforces)

    def set_solve_nyoj(self):
        if self.name_nyoj is not None:
            self.solve_nyoj = crawlerUtil.get_nyoj_solve(self.name_nyoj)

    def set_solve_fuquan(self):
        if self.name_fuquan is not None:
            self.solve_fuquan = crawlerUtil.get_fuquan_solve(self.name_fuquan)

    def set_solve_luogu(self):
        if self.name_luogu is not None:
            self.solve_luogu = crawlerUtil.get_luogu_solve(self.name_luogu)

    def set_solve_vjudge(self):
        if self.name_vjudge is not None:
            self.solve_vjudge = crawlerUtil.get_vjudge_solve(self.name_vjudge)

    def get_tot_solve(self):
        self.tot_solve = self.solve_zzulioj + self.solve_nyoj + self.solve_nowcoder + self.solve_codeforces + self.solve_fuquan + self.solve_luogu + self.solve_vjudge


def test():
    print("test")
