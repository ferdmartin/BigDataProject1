#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

for line in sys.stdin:

    line=line.strip(',')

    name= line.split(",")[-2]
    shot= '1' if line.split(",")[14] == 'made' else '0'

    defen_las=line.split(",")[15].strip('"')
    defen_fir=line.split(",")[16].strip('"')
    defen_ful=defen_fir+" "+defen_las
    defen_ful.strip("")

    print(name+','+defen_ful+'\t'+ shot)