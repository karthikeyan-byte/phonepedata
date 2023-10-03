import csv
import sqlite3
import pandas as pd
   
   
   
df1 = pd.read_csv("agg_trans.csv")
df2=pd.read_csv("agg_user.csv")
df3=pd.read_csv("map_trans.csv")
df4=pd.read_csv("map_user.csv")
df5=pd.read_csv("top_trans.csv")
df6=pd.read_csv("top_user.csv")


conn = sqlite3.connect("phonepe.db")

df1.to_sql("agg_transc", conn, if_exists="append",index=False)
df2.to_sql("agg_user", conn, if_exists="append",index=False)
df3.to_sql("map_trans", conn, if_exists="append",index=False)
df4.to_sql("map_user", conn, if_exists="append",index=False)
df5.to_sql("top_trans", conn, if_exists="append",index=False)
df6.to_sql("top_user", conn, if_exists="append",index=False)



conn.commit()
conn.close()





