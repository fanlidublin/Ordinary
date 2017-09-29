# _*_ encoding:utf-8 _*_
__author__ = 'lifan'
__date__ = '29/09/2017 18:52'


def Cc(n, m, i):
    if (i == 1):
        return (n + m - 1) % n
    else:
        return (solve(n - 1, m, i - 1) + m) % n


if __name__ == '__main__':
    for i in range(1, 101):
        print(Cc(100, 7, i) + 1)
