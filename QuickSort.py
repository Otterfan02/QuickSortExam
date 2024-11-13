import pandas as pd

df = pd.read_csv('worldcities.csv')

def quickSort(list):
    pivot = list[2]
    lesser = quickSort([x for x in list[1:] if x[1] < pivot[1]])
    greater = quickSort([x for x in list[1:] if x[1] >= pivot[1]])
    return lesser + [pivot] + greater

df = quickSort(df)


