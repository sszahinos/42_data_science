
from time import sleep
from tqdm import tqdm

def ft_progress(list):
	return tqdm(list)

def start_loading():
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		sleep(0.01)
	print()
	print(ret)

if __name__ == "__main__":
    start_loading()