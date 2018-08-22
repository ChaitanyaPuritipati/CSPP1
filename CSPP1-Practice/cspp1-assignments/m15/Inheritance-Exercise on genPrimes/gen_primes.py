#define the gen_primes function here
def genPrimes(a):
    prime = 2
    counter = 0
    while counter < a:
        flag = 0
        for i in range(1, prime):
            if prime%i == 0:
                flag += 1
        if flag == 1:
            yield prime
            counter += 1
        prime += 1                  

def main():
	data=input()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes(a)
	for i in range(a):
	    p=primeGenerator.__next__()
	    if(i%b==0):
	        print(p)
	
if __name__== "__main__":
	main()
