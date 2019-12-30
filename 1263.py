def main():
    N, M = map(int, input().split())
    cand = []
    vote = []

    for i in range(0, M):
        vote.insert(1, int(input()))

    for i in range (0, N):
        cand.insert(1, vote.count(cand[i]));

    for i in range(1, N+1):
        cand[i] = cand[i] * 100 / M;
        print(round(cand[i], 2))




if __name__ == '__main__':
    main();
