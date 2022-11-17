
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    hd = ["Origin", "Destination", "Origin City", "Destination City", "Passengers", "Seats", "Flights", "Distance",
          "Fly Date", "Origin Population", "Destination Population"]
    dat = pd.read_csv(r"C:\Users\Dow\Downloads\chimps_16091-2010-08-03_17-08-31\flight_edges.tsv", sep="\t", names=hd)
    dat2 = dat[dat["Destination"] == "MFR"]

    for i in dat2.columns:
        if i != "Passengers" and i != "Fly Date" and i != "Flights":
            del dat2[i]

    dat2.loc[:, "Fly Date"] = pd.to_datetime(dat2.loc[:, "Fly Date"].copy(), format="%Y%m")

    dat2.set_index("Fly Date", inplace=True)
    dat2 = dat2.sort_index()
    print("MFR Month-Passenger")
    print(dat2.head(10))
    print(dat2.groupby("Fly Date").sum().head(10))



