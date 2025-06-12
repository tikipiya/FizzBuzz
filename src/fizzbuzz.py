def fizzbuzz(n: int) -> str:
    
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def main():
    """
    1から100までのFizzBuzzを実行するメイン関数
    """
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main() 