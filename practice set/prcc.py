import pandas as pd
import numpy as np
score=[78,85,59,97,34,56,95]
subjects=["math","science","english","computer","pychics","history","hindi"]
arr=np.array(score)
print("score",np.sum(arr))
print("max",np.max(arr))
print("min",np.min(arr))
print("mean",np.mean(arr))
df=pd.DataFrame({
    "score":score,
    "subject":subjects
})
print("\n complete score")
print(df)

print("\nscore below 60(failed subject")
print(df[df["score"]<60])

print("\n descending order")
print(df.sort_values(by="score",ascending=False))