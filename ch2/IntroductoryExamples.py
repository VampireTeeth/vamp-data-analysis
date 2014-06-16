import json
from collections import defaultdict, Counter
from pandas import DataFrame
import matplotlib.pyplot as plt

def getCounts(seq):
    counts = defaultdict(int)
    for x in seq:
        counts[x] += 1
    return counts


def topCounts(d, n = 10):
    c = Counter(d)
    return c.most_common(n)

def main():
    path = 'usagov_bitly_data2013-05-17-1368832207'
    records = [json.loads(line) for line in open(path)]
    tzs = [rec['tz'] for rec in records if 'tz' in rec]
    counts = getCounts(tzs)
    print counts
    top10 = topCounts(counts)
    print top10

    """Pandas DataFrame demo"""
    frame = DataFrame(records)
    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'
    tz_counts = clean_tz.value_counts()
    print tz_counts[:10]
    tz_counts[:10].plot(kind='barh', rot=0)
    plt.show()




if __name__ == '__main__':
    main()

