import csv
from collections import Counter

def main():
    with open('twitter-inclass-annotations.csv') as in_file:
        iCSV = csv.reader(in_file, delimiter=',')
        empty = {}
        items = ['mixed','neutral','unknown','negative','positive']
        for i in items:
            empty[i] = 0
        first = True
        tot = 0
        print("tweet id,{}".format(','.join(items)))
        for row in iCSV:
            if first:
                first = False
                continue
            cnt = Counter(row[1:])
            order = []
            for i in items:
                order.append(str(cnt[i]))
            print('{},{}'.format(tot,','.join(order)))
            tot += 1
            

main()
