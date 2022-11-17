
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    hd = ["Origin", "Destination", "Origin City", "Destination City", "Passengers", "Seats", "Flights", "Distance",
          "Fly Date", "Origin Population", "Destination Population"]
    dat = pd.read_csv(r"C:\Users\Dow\Downloads\chimps_16091-2010-08-03_17-08-31\flight_edges.tsv", sep="\t", names=hd)

    dat2 = dat[dat["Destination"] == "MFR"]
    dat2 = dat2[['Fly Date', 'Passengers', 'Flights']]
    dat2.loc[:, "Fly Date"] = pd.to_datetime(dat2.loc[:, "Fly Date"].copy(), format="%Y%m")
    dat2.set_index("Fly Date", inplace=True)
    dat2 = dat2.sort_index()
    dat2 = dat2.groupby("Fly Date").sum()

    #print(dat2.head(20))
    dat2_12m_roll = dat2["Passengers"].rolling(window=12, min_periods=0).mean()
    print(dat2_12m_roll.head(20))

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(dat2['Passengers'], marker='.', markersize=2, color='b', linestyle='None', label='Monthly')
    ax.plot(dat2_12m_roll, label='Rolling Mean', linewidth=2)

    ax.legend()
    ax.set_xlabel('Month')
    ax.set_ylabel('Passengers')
    plt.show()


