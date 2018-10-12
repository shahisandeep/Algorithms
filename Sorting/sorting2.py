import random
import time
import math


def counting_sort(list_vals):
    # finds max val in the list.
    max_val = max(list_vals);

    list_counts = [];
    list_sorted = [];
    list_counts = [0 for i in range(0, max_val + 1)];

    for i in range(0, len(list_vals)):
        list_counts[list_vals[i]] += 1;
        # adds elements in sorted order based on frequency.
    for i in range(0, max_val + 1):
        while (list_counts[i] > 0):
            list_sorted.append(i);
            list_counts[i] -= 1;

    return list_sorted;
def bucket_sort(items, digit = 5):

    buckets = []
    for i in range(10):
        buckets.append([])

    for elem in items:
        if digit > 0:
            key = (elem // (10**digit)) % 10
        else:
            key = elem % 10
        buckets[key].append(elem)
    i = 0
    for bucket in buckets:
        for elem in bucket:
            items[i] = elem
            i += 1

def radixsort(aList):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]

        for i in aList:
            tmp = i / placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1

        # move to next digit
        placement *= RADIX



if __name__ == "__main__":

    list_vals = random.sample(range(0, 2000), 1000)
    print " "
    print "#######Random#######"
    print list_vals
    print "Couting sort"
    start = time.time()
    counting_sort(list_vals)
    end = time.time()
    print "Time : ", end - start

    print "radix sort"
    start = time.time()
    radixsort(list_vals)
    end = time.time()
    print "Time : ", end - start

    print "Bucket sort"
    start = time.time()
    bucket_sort(list_vals)
    end = time.time()
    print "Time : ", end - start

    list_vals = random.sample(range(0, 2000), 1000)
    list_vals.sort()
    print " "
    print "#######increasing#######"
    print list_vals
    print "Couting sort"
    start = time.time()
    counting_sort(list_vals)
    end = time.time()
    print "Time : ", end - start

    print "radix sort"
    start = time.time()
    radixsort(list_vals)
    end = time.time()
    print "Time : ", end - start

    print "Bucket sort"
    start = time.time()
    bucket_sort(list_vals)
    end = time.time()
    print "Time : ", end - start

    print " "
    list_vals = (random.sample(range(0, 2000), 1000))

    print "#######Decreasing#######"
    print list_vals.sort(reverse= True)
    print list_vals
    print "Couting sort"
    start = time.time()
    counting_sort(list_vals)
    end = time.time()
    print "Time : ", end - start

    print "radix sort"
    start = time.time()
    radixsort(list_vals)
    end = time.time()
    print "Time : ", end - start

    print "Bucket sort"
    start = time.time()
    bucket_sort(list_vals)
    end = time.time()
    print "Time : ", end - start
