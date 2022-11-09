
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # TODO: ABCDEFG
    hd = ["Origin", "Destination", "Origin City", "Destination City", "Passengers", "Seats", "Flights", "Distance", "Fly Date",
          "Origin Population", "Destination Population"]
    dat = pd.read_csv(r"C:\Users\Dow\Downloads\chimps_16091-2010-08-03_17-08-31\flight_edges.tsv", sep="\t", names=hd)


    #print(dat["Passengers"][:20])
    #dat["Test"] = dat["Passengers"].rolling(window=10, min_periods=10).mean()

    #print(dat[(dat["Passengers"] != 0) & (dat["Seats"] == 0)]["Passengers"])
    #print(dat.loc[1695204,["Origin", "Destination"]])
    #print(len(dat[dat["Seats"] == 0]))
    #print(len(dat[(dat["Passengers"] == 0) & (dat["Seats"] != 0)]))
    #print(len(dat[dat['Passengers'].equals(dat['Seats'])]))
    #print(dat["Destination"])
    #print(dat.info())
    #print(dat["Test"][:20])
    #dat["Distance", "Destination Population"]
    test = dat.head(20)
    test.plot.scatter(x='Passengers', y='Origin',  c='Red')
    plt.show()

