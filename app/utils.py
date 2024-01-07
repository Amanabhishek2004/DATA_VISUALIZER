import pandas as pd
import requests
import seaborn as sns 
import matplotlib.pyplot as plt
import os



def replace_null(x):
    try:
        return int(x)
    except (ValueError, TypeError):
        return 0  # Replace non-convertible values with 0



def dataframe_creator(data):
    dict = {
        "end_year": [],
        "intensity": [],
        "sector": [],
        "topic": [],
        "insight": [],
        "url": [],
        "region": [],
        "start_year": [],
        "impact": [],
        "added": [],
        "published": [],
        "country": [],
        "relevance": [],
        "pestle": [],
        "source": [],
        "title": [],
        "likelihood": []
    }

    for entry in data:
        entry.pop("update_data")
        for key, value in entry.items():
            dict.get(key).append(value)


   

    df = pd.DataFrame(dict)
    for i in ["relevance" ,"intensity", "start_year" , "end_year" , "likelihood"]:
        df[i] = df[i].apply(replace_null)

    df["region"]=df["region"].str.replace(" " , "-")  
    return df



def imgage_renderer(file_path):
    path = file_path
    files = os.listdir(path)
    files = [file for file in files if str(file).endswith(".png")]   
    images = [os.path.join(file_path , image) for image in files]
    
    return images


def plot_pie_chart(df, query = ""):


    if query: 
      filtered_df = df.query(query)
    else:
        filtered_df = df


    if len(filtered_df["region"].unique())<10:
       threshold = 0
    else:
        threshold = 50  
    region_counts = filtered_df['region'].value_counts()
    filtered_regions = region_counts[region_counts > threshold]
    return filtered_regions

def plot_pie_pestles(df , query = ""):

    if query: 
      filtered_df = df.query(query)
    else:
        filtered_df = df
    if len(df["pestle"].unique())<10:
       threshold = 0
    else:
        threshold = 50  
    pestle_counts = filtered_df['pestle'].value_counts()
    filtered_pestles = pestle_counts[pestle_counts > threshold]
    
    return filtered_pestles

def plot_pie_sector(df , query = ""):
    if query: 
      filtered_df = df.query(query)
    else:
        filtered_df = df

    if len(df["sector"].unique())<10:
       threshold = 0
    else:
        threshold = 50  
    sector_counts = filtered_df['sector'].value_counts()
    filtered_sectors = sector_counts[sector_counts > threshold]
    
    return filtered_sectors

def plot_pie_topic(df , query = ""):

    if query: 
      filtered_df = df.query(query)
    else:
        filtered_df = df
    if len(df["topic"].unique())<10:
       threshold = 0
    else:
        threshold = 50   
    topic_counts = filtered_df['topic'].value_counts()
    filtered_topics = topic_counts[topic_counts > threshold]
    
    return filtered_topics






def count_plots_relevance(df , query = ""):
    if query: 
      filtered_df = df.query(query)
    else:
        filtered_df = df
    
    return filtered_df["relevance"].value_counts()


def count_plots_intensity(df , query = ""):
    if query: 
      filtered_df = df.query(query)
    else:
        filtered_df = df
    
    return filtered_df["intensity"].value_counts()


def count_plots_likelihood(df , query = ""):
    if query: 
      filtered_df = df.query(query)
    else:
        filtered_df = df
    
    return filtered_df["likelihood"].value_counts()
    

def count_plots_end_year(df , query = ""):
    if query: 
      filtered_df = df.query(query)
    else:
        filtered_df = df
    
    return filtered_df["end_year"].value_counts()




