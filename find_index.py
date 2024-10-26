def main(a, b):
    
    result = 0
    if b in a:
        result = a.index(b)
        return result
    else:
        for i in a:
            if b < i:
                result = a.index(i)
                break
            else:
                result = len(a)
               
    return result
        
if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = int(input())
    
    result = main(a, b)
    print(result)