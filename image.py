import statistics
import random
import plotly.figure_factory as pf
import pandas as pd
df=pd.read_csv("medium_data.csv")
reading_time=df["reading_time"].tolist()

def randomdata():
    dataset=[]
    for i in range(0, 100):
        vindex=random.randint(0,len(reading_time)-1)
        v=reading_time[vindex]
        dataset.append(v)
    mean=statistics.mean(dataset)
  
    return mean
data_mean=[]
for i in range(0,1000):
    m=randomdata()
    data_mean.append(m)
graph=pf.create_distplot([data_mean],["reasult"],show_hist=False)
graph.show()     

def calculate():
    mean=statistics.mean(data_mean)
    std=statistics.stdev(data_mean)
    return {'x':mean,'y':std}
    