from openjudgeCrawler.crawler import zzuiloj
from openjudgeCrawler.crawler import nowcoder
from openjudgeCrawler.crawler import codeforces


def get_zzulioj_solve(uid):
    return zzuiloj.get_solve_num(uid)


def get_nowcoder_solve(uid):
    return nowcoder.get_solve_num(uid)


def get_codeforces_solve(uid):
    return codeforces.get_solve_num(uid)


def get_codeforces_rating(uid):
    return codeforces.get_rating(uid)
