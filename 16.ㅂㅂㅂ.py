a=int(input("몇 층 찍으실건가요"))
for i in range(a+1):
    print((" "*(5-i))+(i*2-1)*"*")