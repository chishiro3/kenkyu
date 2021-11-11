import sys

import matplotlib.pyplot as plt

fn = sys.argv[1]
lines = open(fn, 'r').readlines()
ds = [int(line.strip().split(':')[-1]) for line in lines]
plt.figure()
plt.plot(range(len(ds)), ds)
plt.xlabel('frame')
plt.ylabel('distance[mm]')
plt.savefig(f'{fn}.png')
plt.show()
