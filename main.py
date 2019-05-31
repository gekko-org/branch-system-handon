def add(a:int,b:int) -> int:
    return a+b
def seki(a:int,b:int) -> int:
    return a*b
def sub(a: int, b: int) -> int:
    return a - b


if __name__ == '__main__':
    print(f'2+3={add(2, 3)}')
    print(f'2-3={sub(2, 3)}')
    print(f'2*3={seki(2,3)}')

