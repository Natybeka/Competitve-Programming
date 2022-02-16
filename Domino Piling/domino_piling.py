import sys
def count_dominoes():
	rows = int(sys.argv[1])
	cols = int(sys.argv[2])
	return (rows * cols) // 2

if __name__ == '__main__':
	print(count_dominoes())

