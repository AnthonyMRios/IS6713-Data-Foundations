import csv
from collections import Counter

def main():
    items = set()
    with open('pos') as in_file:
        iCSV = csv.reader(in_file, delimiter=',')
        for row in iCSV:
            for i in row:
                items.add(i)

    items = sorted(list(items))
    with open('pos') as in_file:
        iCSV = csv.reader(in_file, delimiter=',')
        empty = {}
        for i in items:
            empty[i] = 0
        first = True
        tot = 0
        print("tweet id,{}".format(','.join(items)))
        for row in iCSV:
            if first:
                first = False
                continue
            cnt = Counter(row[0:])
            order = []
            for i in items:
                order.append(str(cnt[i]))
            print('{},{}'.format(tot,','.join(order)))
            tot += 1
            

main()
