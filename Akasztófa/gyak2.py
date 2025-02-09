# ```
# import sys
# hobbik = {}
# for sor in sys.stdin:
#     adatok = sor.strip().split(":")
#     adat = adatok[1].strip().split(",")
#     for hobbi in adat:
#         if hobbi in hobbik:
#             hobbik[hobbi] += 1
#         else:
#             hobbik[hobbi] = 1
# for kulcs, ertek in sorted(hobbik.items()):
#     print(f'{kulcs}: {ertek} fő')
# ```

import sys
hobbik = {}
for sor in sys.stdin:
    adatok = sor.strip().split(":")
    adat= adatok[1].split(",")
    for hobbi in adat:
        if hobbi in hobbik:
            hobbik[hobbi] += 1
        else:
            hobbik[hobbi] = 1
for kulcs, ertek in sorted(hobbik.items()):
    print(f"{kulcs}: {ertek} fő")