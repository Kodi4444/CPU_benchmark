import concurrent.futures
import time
import cpuinfo
import tqdm

# config ###########################################################################################
work_size = 2 ** 15
multicore = True
use_tqdm = True
# config ###########################################################################################


# work_list gen #########
work_list = list(range(work_size))
# work_list gen #########


def convert_seconds(sec):
    seconds = sec
    minutes = 0
    hours = 0
    while seconds > 60:
        seconds -= 60
        minutes += 1
    seconds = round(seconds, 2)

    while minutes > 60:
        minutes -= 60
        hours += 1

    print('# hours', hours)
    print('# minutes', minutes)
    print('# seconds', seconds)


def calc(x):
    return x**x


start = time.time()

if multicore:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        if use_tqdm:
            list(tqdm.tqdm(executor.map(calc, work_list), total=len(work_list)))
        else:
            executor.map(calc, work_list)


else:
    if use_tqdm:
        for e in tqdm.tqdm(work_list):
            calc(e)
    else:
        for e in work_list:
            calc(e)

end = time.time()

print('# CPU =', cpuinfo.get_cpu_info()['brand_raw'])
print('# work_size =', work_size, 'or', f'{work_size:,}')
print('# use_tqdm =', use_tqdm)
convert_seconds(round(end - start, 2))
print('# total seconds', round(end - start, 2))

# CPU = AMD Ryzen 9 3900X 12-Core Processor
# work_size = 32768 or 32,768
# use_tqdm = True
# hours 0
# minutes 0
# seconds 10.3
# total seconds 10.3

# CPU = AMD Ryzen 9 3900X 12-Core Processor
# work_size = 32768 or 32,768
# use_tqdm = True
# hours 0
# minutes 1
# seconds 31.92
# total seconds 91.92

# CPU = AMD Ryzen 9 3900X 12-Core Processor
# work_size = 65536 or 65,536
# use_tqdm = True
# hours 0
# minutes 0
# seconds 53.93
# total seconds 53.93
