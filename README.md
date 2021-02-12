# CPU_benchmark
there are 3 config options at the top of the script lines 7-9
work_size is the size of the work. You can put any number there. "2 ** 15" just means 2^15 = 32768 the larger the number the more acurate the test but also the longer the test will last.
if multicore = True then it will use all the cores. if multicore = False then it will only use 1 core.
use_tqdm if its true the only thing it does is add a loading bar 
