from crawler import zzuiloj
from crawler import nowcoder
from crawler import codeforces
from crawler import fuquanoj
from crawler import nyoj
from crawler import luogu
from crawler import vjudge
from crawler import jzoj
from crawler import hduoj
from crawler import poj


def get_zzulioj_solve(uid):
    return zzuiloj.get_solve_num(uid)


def get_nowcoder_solve(uid):
    return nowcoder.get_solve_num(uid)


def get_codeforces_solve(uid):
    return codeforces.get_solve_num(uid)


def get_codeforces_rating(uid):
    return codeforces.get_rating(uid)


def get_nyoj_solve(uid):
    return nyoj.get_solve_num(uid)


def get_fuquan_solve(uid):
    return fuquanoj.get_solve_num(uid)


def get_luogu_solve(uid):
    return luogu.get_solve_num(uid)


def get_vjudge_solve(uid):
    return vjudge.get_solve_num(uid)


def get_jzoj_solve(uid):
    return jzoj.get_solve_num(uid)


def get_hduoj_solve(uid):
    return hduoj.get_solve_num(uid)


def get_poj_solve(uid):
    return poj.get_solve_num(uid)
