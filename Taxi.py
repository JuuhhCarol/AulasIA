import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_parquet('taxis.parquet') 

#tirar N/A da tabela 
# df = df.dropna()

#organizador de colunas
df.rename(columns={'tpep_pickup_datetime': 'Pickup'}, inplace=True)
df.rename(columns={'tpep_dropoff_datetime': 'Dropoff'}, inplace=True)
df= df.drop(columns='store_and_fwd_flag')
df["total taxes"] =(
    df["extra"]
    +df["mta_tax"]
    +df["improvement_surcharge"]
    +df["congestion_surcharge"]
    +df["Airport_fee"]
    +df["cbd_congestion_fee"]
)

df = df.drop(
    [
        "extra",
        "mta_tax",
        "improvement_surcharge",
        "congestion_surcharge",
        "Airport_fee",
        "cbd_congestion_fee",
    ],
    axis=1,
)

df = df[(df["passenger_count"] >= 1) & (df["passenger_count"] <= 6)]
df = df.dropna(subset=["passenger_count"])


VendorID = {
    1: "Creative Mobile Technologies, LLC",
    2: "Curb Mobility, LLC",
    6: "Myle Technologies Inc",
    7: "Helix"
}
df["VendorID"] = df["VendorID"].map(VendorID)

df = df[(df["trip_distance"] > 0) & (df["trip_distance"] <= 100)]

Payment_type = {
    0: "Tarifa Flexivel",
    1: "Cartão de Credito",
    2: "Dinheiro",
    3: "Sem Custo",
    4: "Contestação",
    5: "Desconhecido",
    6: "Viagem Anulada"
}
df["payment_type"] = df["payment_type"].map(Payment_type)



# print(df['total taxes'])
print(df)