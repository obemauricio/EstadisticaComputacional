import random

def media(x):
    return sum(x) / len(x)

if __name__ == '__main__':
    x = [random.randint(1,21) for i in range(20)]
    
    print(x)
    mu = media(x)
    

    print(mu)