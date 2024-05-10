#!/usr/bin/env python

import pandas as pd
def main() :
    drivers_df: pd.DataFrame = pd.read_csv('drivers.csv')

    results_df: pd.DataFrame = pd.read_csv('results.csv')
    
    results_df = results_df[results_df['positionOrder'] == 1]
    merged_df: pd.DataFrame = results_df.merge(drivers_df, on='driverId', how='left')
    
    answer: pd.DataFrame = merged_df.groupby(['nationality'],as_index=False).size().sort_values(by='size', ascending=False).head(10)
    print(answer)
if __name__ == "__main__":
    main()
