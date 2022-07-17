import pandas as pd

d={
    "hotel" : {
"topics" : [
  {"topic1":  '1', "topic2" : "2", "topic3" :  "3","topic4":'12'},
    {"topic1":  '2', "topic2" : "3", "topic3" :  "4","topic4":'23'},
    {"topic1":  '3', "topic2" : "4", "topic3" :  "5","topic4":'13'},
    {"topic1":  '4', "topic2" : "5", "topic3" :  "6","topic4":'141'},
    {"topic1":  '5', "topic2" : "6", "topic3" :  "7","topic4":'4'}
],
  "timesal": "12h",  "hotel_name" : "hotel1" }
}

def parsing(df):
    list_of_data=[]
    for topic in df["hotel"]['topics']:
        di={"topic1": int(topic['topic1']),"topic2":int(topic['topic2']),
        "topic3": int(topic['topic3']),"topic4": int(topic['topic4']), 
        'timesal':df["hotel"]['timesal'], 'hotel_name':df["hotel"]['hotel_name']}
        list_of_data.append(di)
    return list_of_data

df=pd.DataFrame( parsing(d))

print([df.columns()])

# df_columns=


