import datetime

def main():
    ages = []
    dates = []
    spisok = []
    n = int(input())
    for i in range(n):
        d1, d2, d3 = input().split()
        dates = [d1, d2, datetime.datetime.strptime(d3, '%d.%m.%Y')]
        spisok.extend([dates])
        d1 = datetime.datetime.strptime(d1, '%d.%m.%Y')
        d3 = datetime.datetime.strptime(d3, '%d.%m.%Y')
        age = (d3 - d1).days
        ages.append(age)
    maxage = max(ages)
    maxageindex = ages.index(max(ages)) + 1
    for i in range(n):
        if ages[i] == maxage:
            if spisok[i][2] < spisok[ages.index(max(ages))][2]:
                maxageindex = i + 1

    print(maxageindex)

if __name__ == '__main__':
    main()