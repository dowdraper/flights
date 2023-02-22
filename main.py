#! /usr/bin/env python3

# Created: 12/15/22
# Author : Brett Warren
# Project: flights
# File   : main.py

"""
Description:
This is Dow's project. He should fill this in, I'm just getting him started.
"""
import pandas as pd
from matplotlib import pyplot as plt


def main():
    import sklearn.metrics

#     hd = ["Origin", "Destination", "Origin City", "Destination City", "Passengers", "Seats", "Flights", "Distance",
#           "Fly Date", "Origin Population", "Destination Population"]
#     # dat = pd.read_csv(r"C:\Users\Dow\Downloads\chimps_16091-2010-08-03_17-08-31\flight_edges.tsv", sep="\t", names=hd)
#     dat = pd.read_csv(r"flight_edges.tsv", sep="\t", names=hd)
#
#     dat2 = dat[dat["Destination"] == "MFR"]
#     dat2 = dat2[['Fly Date', 'Passengers', 'Flights']]
#     dat2.loc[:, "Fly Date"] = pd.to_datetime(dat2.loc[:, "Fly Date"].copy(), format="%Y%m")
#     dat2.set_index("Fly Date", inplace=True)
#     dat2 = dat2.sort_index()
#     dat2 = dat2.groupby("Fly Date").sum()
#     dat2['Average'] = dat2['Passengers'] / dat2['Flights']
#
#     # print(dat2.head(20))
#
#     dat2test = dat2[['Passengers']].resample('Y').mean()
#
#     # print(dat2test.head(20))
#
#     # Comment out the line below, and instead of min_periods here, try
#     # center=True. Keep the rest the same and see what that looks like.
#     dat2_12m_roll = dat2["Passengers"].rolling(window=12, min_periods=0).mean()
#     # print(dat2_12m_roll.head(20))
#     dat2_12m_roll2 = dat2["Passengers"].rolling(window=12, center=True).mean()
#     # So, that's rolling, let's try resampling too. Let me know if you need help
#     # with the syntax.
#
#     dat2_diff = dat2['Passengers'].diff()
#     pre = dat2_diff[dat2_diff.index < pd.Timestamp(year=2001, month=9, day=1)]
#     post = dat2_diff[dat2_diff.index >= pd.Timestamp(year=2001, month=9, day=1)]
#     differenceMeanPre = pre.groupby(pre.index.month).mean()
#     differenceMeanPost = post.groupby(post.index.month).mean()
#     # print(differenceMean.head(20))
#     # print(dat2_12m_roll2.head(20))
#
#     # fig, ax = plt.subplots(figsize=(12, 5))
#     # ax.plot(dat2['Passengers'], marker='.', markersize=2, color='b', linestyle='None', label='Monthly')
#     # ax.plot(dat2_12m_roll, label='Rolling Mean', linewidth=2)
#
#     print(differenceMeanPre, "\n", differenceMeanPost)
#     plt.axhline(linestyle='--', color='k')
#     plt.plot(differenceMeanPre, label='Differencing Mean pre-9/11', linewidth=2, color='b')
#     plt.plot(differenceMeanPost, label='Differencing Mean post-9/11', linewidth=2, color='r')
#
#     # ax.plot(dat2_diff, label='Differencing', linewidth=2, color='r')
#     # ax.plot(dat2_12m_roll2, label='Rolling Mean (Centered)', linewidth=2, color='r')
#     # ax.plot(dat2test['Passengers'], label='Resampled Mean', linewidth=2, color='g')
#
#     # ax.legend()
#     # ax.set_xlabel('Month')
#     # ax.set_ylabel('Passengers')
#
#     plt.xlabel("Month")
#     plt.ylabel("Passengers")
#     plt.legend()
#     plt.show()
#
#     # ^^^ That plot showed an upward trend over all years, right? A time series
#     # with a trend is non-stationary, one without (or removed) is stationary.
#     # We might want to look into de-trending the full line so that we can assess
#     # any monthly variations. How do we remove a trend from a time series...
#     # Differencing. It's pretty simple, essentially we are going to do this:
#     # PAM: Passengers At Month
#     # PAM_x = original_PAM_x - original_PAM_x-1
#     #
#     # Take dat2 and create another df with the differences. This is called
#     # first-order differencing, so you may want to call it something like that.
#     # Try to graph your first-order differences. Because we are looking at
#     # differences, you should expect your plotted line to go above and below the
#     # x-axis.
#     #
#     # Let me know if you have any questions or need any help!
#
#     # dat2["PAM"] = dat2["Passengers"] -
#
#
#
#
if __name__ == '__main__':
     main()