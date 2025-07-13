def main():
    first_line = input().strip()
    N, M = map(int, first_line.split())

    second_line = input().strip()
    numbers = list(map(int, second_line.split()))

    result = 1

    # 모든 숫자를 순회하면서
    for num in numbers:
        # num을 M으로 나눈 나머지를 구한 후 결과에 곱하고 다시 M으로 나눈 나머지를 구함
        # idea: (A × B) % M = ((A % M) × (B % M)) % M 
        result = (result * (num % M)) % M
    print(result)

if __name__ == "__main__":
    main()
