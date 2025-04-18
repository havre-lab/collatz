def hotpo(num):
    if num%2==0:
        return num//2
    else:
        return num*3+1
if __name__ == "__main__":
    import sys
    print(hotpo(int(sys.argv[1])))