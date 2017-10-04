#!/usr/bin/env python3
"""using files"""

import sys
from pprint import pprint


ipsum1 = "Rerum pariatur aliquam corrupti possimus ipsum itaque. Voluptatem officia doloremque quos esse quo voluptatem quo. Rem est alias velit perspiciatis. Ipsum quo ea aliquam.\n"
ipsum2 = "Quia ut rerum minima tempore. Sunt in nisi totam magnam consequatur. Impedit alias cum provident ut illum esse.\n"
ipsum3 = "Quam sunt nemo sed ut laborum velit. Corrupti rerum reiciendis temporibus numquam ducimus eveniet. Voluptatum et in recusandae.\n"
ipsum4 = "Iusto ipsam nihil enim neque rerum modi. Consectetur officia ut voluptas laudantium. Enim fugiat voluptas quisquam odit veniam similique.\n"
ipsum5 = "Illum quidem fuga voluptatem atque. Incidunt magnam alias ad at ut et est et. Repudiandae voluptatem quisquam est. A voluptatem vel modi. Officia aut laborum non voluptates dolor ex error.\n"


def main():
    f = open("temp.txt", mode="wt", encoding="utf-8")
    f.write(ipsum1)
    f.write(ipsum2)
    f.write(ipsum3)
    f.write(ipsum4)
    f.write(ipsum5)
    f.close()

    g = open("temp.txt", mode="rt", encoding="utf-8")
    print(g.read(len(ipsum1)))
    print(g.readline())
    print(g.readlines())
    g.close()

if __name__ == '__main__':
    main()