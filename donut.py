#Linux command: python donut.py

import math
import time

k = 0

def main():
    A, B = 0, 0
    z = [0] * 1760
    b = [' '] * 1760

    print("\x1b[2J", end='', flush=True)

    while True:
        b = [' '] * 1760
        z = [0] * 1760
        for j in range(0, 628, 7):
            for i in range(0, 628, 2):
                sini, cosj, sinA, sinj, cosA, cosj2, mess, cosi, cosB, sinB, t = [0] * 11

                sini = math.sin(i)
                cosj = math.cos(j)
                sinA = math.sin(A)
                sinj = math.sin(j)
                cosA = math.cos(A)
                cosj2 = cosj + 2
                mess = 1 / (sini * cosj2 * sinA + sinj * cosA + 5)
                cosi = math.cos(i)
                cosB = math.cos(B)
                sinB = math.sin(B)
                t = sini * cosj2 * cosA - sinj * sinA

                x = int(40 + 30 * mess * (cosi * cosj2 * cosB - t * sinB))
                y = int(12 + 15 * mess * (cosi * cosj2 * sinB + t * cosB))
                o = x + 80 * y
                N = int(8 * ((sinj * sinA - sini * cosj * cosA) * cosB - sini * cosj * sinA - sinj * cosA - cosi * cosj * sinB))

                if 22 > y > 0 and 80 > x > 0 and mess > z[o]:
                    z[o] = mess
                    b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

        print("\x1b[H", end='', flush=True)
        for k in range(1760):
            print(b[k], end=(' ' if k % 80 else '\n'), flush=True)

        A += 0.04
        B += 0.02
        time.sleep(0.01)

if __name__ == '__main__':
    main()
