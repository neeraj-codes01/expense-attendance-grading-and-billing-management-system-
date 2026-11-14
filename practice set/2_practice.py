import numpy as np
import pandas as pd
days=["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]
sales=[1500,1200,1000,500,600,1500,400]
arr=np.array(sales)
print("total",np.sum(arr))
print("maximum",np.max(arr))
print("minimum",np.min(arr))
print("mean",np.average(arr))

df=pd.DataFrame({
    "day":days,
    "sales":arr
})
print("\n completed data")
print(df)
print("\n sales above 1500")
print(df[df["sales"]>1500])
print("\n descending order")
print(df.sort_values(by="sales",ascending=False))