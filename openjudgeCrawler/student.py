from openjudgeCrawler.util import crawlerUtil


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
        self.sno = sno
        self.name = name
        self.tot_solve = 0

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
        if self.name_zzulioj is not None:
            self.rating_codeforces = crawlerUtil.get_codeforces_rating(self.name_codeforces)

    def get_tot_solve(self):
        self.tot_solve = self.solve_zzulioj + self.solve_nyoj + self.solve_nowcoder + self.solve_codeforces


def test():
    print("test")