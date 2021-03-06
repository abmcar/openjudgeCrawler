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
        self.name_jzoj = None
        self.solve_jzoj = 0
        self.extra_codeforces = 0
        self.fake_name = None
        self.name_hduoj = None
        self.solve_hduoj = 0
        self.name_poj = None
        self.solve_poj = 0

    def set_solve_zzulioj(self):
        if self.name_zzulioj is not None:
            self.solve_zzulioj = crawlerUtil.get_zzulioj_solve(self.name_zzulioj)
        else:
            if self.fake_name is not None:
                self.solve_zzulioj = crawlerUtil.get_zzulioj_solve(self.fake_name)

    def set_solve_nowcoder(self):
        if self.name_nowcoder is not None:
            self.solve_nowcoder = crawlerUtil.get_nowcoder_solve(self.name_nowcoder)
        else:
            if self.fake_name is not None:
                self.solve_nowcoder = crawlerUtil.get_nowcoder_solve(self.fake_name)

    def set_solve_codeforces(self):
        if self.name_codeforces is not None:
            self.solve_codeforces = crawlerUtil.get_codeforces_solve(self.name_codeforces)
        else:
            if self.fake_name is not None:
                self.solve_codeforces = crawlerUtil.get_codeforces_solve(self.fake_name)

    def set_rating_codeforces(self):
        if self.name_codeforces is not None:
            self.rating_codeforces = crawlerUtil.get_codeforces_rating(self.name_codeforces)
        else:
            if self.fake_name is not None:
                self.rating_codeforces = crawlerUtil.get_codeforces_rating(self.fake_name)

    def set_solve_nyoj(self):
        if self.name_nyoj is not None:
            self.solve_nyoj = crawlerUtil.get_nyoj_solve(self.name_nyoj)
        else:
            if self.fake_name is not None:
                self.solve_nyoj = crawlerUtil.get_nyoj_solve(self.fake_name)

    def set_solve_fuquan(self):
        if self.name_fuquan is not None:
            self.solve_fuquan = crawlerUtil.get_fuquan_solve(self.name_fuquan)
        else:
            if self.fake_name is not None:
                self.solve_fuquan = crawlerUtil.get_fuquan_solve(self.fake_name)

    def set_solve_luogu(self):
        if self.name_luogu is not None:
            self.solve_luogu = crawlerUtil.get_luogu_solve(self.name_luogu)
        else:
            if self.fake_name is not None:
                self.solve_luogu = crawlerUtil.get_luogu_solve(self.fake_name)

    def set_solve_vjudge(self):
        if self.name_vjudge is not None:
            self.solve_vjudge = crawlerUtil.get_vjudge_solve(self.name_vjudge)
        else:
            if self.fake_name is not None:
                self.solve_vjudge = crawlerUtil.get_vjudge_solve(self.fake_name)

    def set_solve_jzoj(self):
        if self.name_jzoj is not None:
            self.solve_jzoj = crawlerUtil.get_jzoj_solve(self.name_jzoj)
        else:
            if self.fake_name is not None:
                self.solve_jzoj = crawlerUtil.get_jzoj_solve(self.fake_name)

    def set_solve_poj(self):
        if self.name_poj is not None:
            self.solve_poj = crawlerUtil.get_poj_solve(self.name_poj)
        else:
            if self.fake_name is not None:
                self.solve_poj = crawlerUtil.get_poj_solve(self.fake_name)

    def set_solve_hduoj(self):
        if self.name_hduoj is not None:
            self.solve_hduoj = crawlerUtil.get_hduoj_solve(self.name_hduoj)
        else:
            if self.fake_name is not None:
                self.solve_hduoj = crawlerUtil.get_hduoj_solve(self.fake_name)

    def get_tot_solve(self):
        self.tot_solve = self.solve_hduoj + self.solve_poj + self.solve_zzulioj + self.solve_nyoj + self.solve_nowcoder + self.solve_codeforces + self.solve_fuquan + self.solve_luogu + self.solve_vjudge + self.solve_jzoj

    def get_extra_codeforces(self):
        nowRating = self.rating_codeforces
        if nowRating >= 300:
            self.extra_codeforces = 5
        if nowRating >= 500:
            self.extra_codeforces = 10
        if nowRating >= 700:
            self.extra_codeforces = 25
        if nowRating >= 800:
            self.extra_codeforces = 50
        if nowRating >= 950:
            self.extra_codeforces = 100


def test():
    print("test")
