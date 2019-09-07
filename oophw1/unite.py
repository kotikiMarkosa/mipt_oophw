import sys
import glob
print(sys.argv[1])
if sys.argv[2] == '*':
    filenames_list = glob.glob("./*.*")
else:
    filenames_list = sys.argv[2:]
    
with open(sys.argv[1], 'w') as out:
    for file_name in filenames_list:
        with open('./' + file_name, 'r') as inp:
            for line in inp:
                out.write(line)
            out.write('\n')
            print(file_name)
print('Done!')