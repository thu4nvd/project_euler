#!/usr/bin/env python3

'''
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
'''


def solve(n):
    result = 1
    for i in range(n + 1, 2 * n + 1):
        result = result * i
    for i in range(1, n + 1):
        result = result / i

    return int(result)


def main():
    print(solve(20))


if __name__ == "__main__":
    main()
