#!/usr/bin/env python3

'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


https://projecteuler.net/problem=17
'''

def sol():
        unoNueve = "onetwothreefourfivesixseveneightnine"
        onceDiezNueve = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
        veinteNoventa = "twentythirtyfortyfiftysixtyseventyeightyninety"
        cienNovechento = "hundredand"
        mil = "onethousand"
        one99 = len(unoNueve)*9 + len(onceDiezNueve) + len(veinteNoventa)*10
        return one99*10 + len(unoNueve)*100 + len("hundred")*9 + len("hundredand")*99*9 + len("onethousand")


def main():
    print(sol())


if __name__ == "__main__":
    main()