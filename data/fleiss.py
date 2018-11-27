import csv

def main():
    N = 0
    Nn = 0
    head = True
    Po = 0 # Po Sum
    nj = {} # Keep track of class (column) sums
    headers = []
    with open('twitter-inclass-annotations-easy.csv') as inf:
        iCSV = csv.reader(inf)
        for row in iCSV:
            if head:
                head = False
                for name in row[1:]:
                    nj[name] = 0
                headers = row[1:]
            else:
                Pi = 0
                n = 0
                index = 0
                for i in row[1:]:
                    Pi += float(i) * (float(i)-1)
                    n += float(i)
                    nj[headers[index]] += float(i)
                    index += 1
                Pi = (1/(n*(n-1))) * Pi # Normalize Pi (i-th items agreement)
                Nn += n # Keep track of sum of all annotations
                Po += Pi # Add the i-ths items agreement to Po
                N += 1 # Keep track of number of tweets

    Po = (1/N) * Po # Normalize Po

    Pe = 0 # Pe Sum
    for class_name, count in nj.items():
        pj = (1/Nn) * count # normalize pj
        Pe += pj**2 # pj squared

    kappa = (Po - Pe)/(1-Pe)

    print("Po: {}".format(Po))
    print("Pe: {}".format(Pe))
    print("Fleiss' Kappa: {}".format(kappa))

main()
