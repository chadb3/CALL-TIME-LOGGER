from src import *
from time import sleep

def main():
    print("TEST")
    a = Call(1)
    sleep(60)
    b = Call(2)
    sleep(60)
    c = Call(3)
    print("{}\n{}\n{}\n".format(a,b,c))
    return 0

if __name__ == "__main__":
	main()