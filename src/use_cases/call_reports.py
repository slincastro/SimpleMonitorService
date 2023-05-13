import pandas as pd

def get_intermittence_time(file_path):
    data = pd.read_csv(file_path, names= ["Flow_Name", "Service_Name", "Date", "trace_id", "Service_Response", "Service_Response_Time", "Message"])
    data['Date'] = pd.to_datetime(data['Date'])

    filtered_data = data[['Service_Response', 'Date']]

    filtered_df = filtered_data.loc[filtered_data['Service_Response']==500]
    first_row = filtered_df.iloc[0]

    filtered_df['matches_first'] = filtered_df.apply(lambda row: (row['Date'] - first_row['Date']).total_seconds() , axis=1)

    non_consecutive_indexes = filtered_df.loc[filtered_df.index.isin(range(len(filtered_df)))]
    print(non_consecutive_indexes)

def get_interm(file_path):
    data = pd.read_csv(file_path, names=["Flow_Name", "Service_Name", "Date", "trace_id", "Service_Response",
                                         "Service_Response_Time", "Message"])
    data['Date'] = pd.to_datetime(data['Date'])
    filtered_data = data[['Service_Response', 'Date']]

    filtered_df = filtered_data.loc[filtered_data['Service_Response'] == 500]

    diffs = filtered_df.index.to_series().diff().fillna(1)
    groups = diffs.ne(1).cumsum()
    grouped = filtered_df.groupby(groups)

    unavailable_time =pd.DataFrame(columns=['Start_Date','End_Date','Time'])

    for name, group in grouped:
        dif_time = group['Date'].iloc[-1] - group['Date'].iloc[0]
        unavailable_time.loc[len(unavailable_time)] = [group['Date'].iloc[0], group['Date'].iloc[-1], dif_time.total_seconds()/60]

    print(unavailable_time)

get_interm("test/service_data_test.csv")