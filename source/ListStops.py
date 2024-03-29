import csv
import pandas as pd
from operator import itemgetter

def outputCSV():
    '''load csv and sort the location_id for both mean and medium so we can do do the calculation in a for loop'''
    data = pd.read_csv('C:\\Users\\jackc\\Desktop\\ctran\\ctran_trips_data.csv')
    df = data.groupby('location_id')['location_distance'].mean()
    result = df.sort_index(ascending=False)

    de = data.groupby('location_id')['location_distance'].median()
    result_median = de.sort_index(ascending=False)

    list = []

    '''
    the analysis is checking if the mean and medium is greater than 30, if the 
    value is greater than 30 for both then we store it in a 2-d array. 
    We then sort the 2d array by mean and display the location id, average, and median
    '''
    for x in range(result.size):
        if result.array[x] > 30:
            if result_median.array[x] > 30:
                list.append([result.index[x], result.array[x],result_median.array[x] ])
    list = sorted(list, key=itemgetter(1), reverse=True)

    #for x in list:
        #print(x)


    with open('C:\\Users\\jackc\\Desktop\\ctran\\output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['location_id','average', 'median'])
        for x in list:
            writer.writerow(x)
    file.close()
