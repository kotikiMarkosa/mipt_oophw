import sys
import numpy as np
my_data = []
with open(sys.argv[1], 'r') as data_file:
    for line in data_file:
        my_data.append(float(line))
with open(sys.argv[2], 'w') as moments_file:
    moments_file.write(str(np.mean(my_data)) + '\n' + str(np.var(my_data, ddof = 1)))
        