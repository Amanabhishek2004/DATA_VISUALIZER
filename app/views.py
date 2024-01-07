from django.shortcuts import render
import pandas as pd
import requests
from .utils import *

# Create your views here.

def url_testing(request):
    
    api_url = "http://127.0.0.1:8000/api"
    response = requests.get(api_url)
                         
    df  = dataframe_creator(response.json())


    city_data = request.POST.get("city" , None)
    intensity_data = request.POST.get("intensity" , None)
    relevance_data = request.POST.get("relevance" , None)
    region_data = request.POST.get("region" , None)
    topic_data = request.POST.get("topic" , None)
    likielihood_data = request.POST.get("likelihood" , None)
    end_year_data = request.POST.get("endyear" , None)
    
    

    # cities = df["city"].unique()
    topics = df["topic"].unique()
    regions = df["region"].unique()
    intensities = df["intensity"].unique()
    relevances = df["relevance"].unique()
    likielihood = df["likelihood"].unique()
    end_year = df["end_year"].unique()

    query_string = ""  
    



    
    if intensity_data:
        
         if query_string == "":
             query_string += f"intensity=={intensity_data}"
         else:
             query_string+=  f" and intensity=={intensity_data}"  
    if relevance_data:
        
         if query_string == "":
             query_string += f"relevance=={relevance_data}"
         else:
             query_string+=  f" and relevance=={relevance_data}"  

    if region_data:
         if query_string == "":
             query_string += f"region=='{region_data}'"
         else:
             query_string+=  f" and region=='{region_data}'"  
    
    if topic_data:
         if query_string == "":
             query_string += f"topic=='{topic_data}'"
         else:
             query_string+=  f" and topic=='{topic_data}'" 
    
    if likielihood_data:
         if query_string == "":
             query_string += f"likelihood=={likielihood_data}"
         else:
             query_string+=  f" and likelihood=={likielihood_data}"
    

    if end_year_data:
         if query_string == "":
             query_string += f"end_year=={end_year_data}"
         else:
             query_string+=  f" and end_year=={end_year_data}"
    
    print(query_string)
    if query_string != "":
     filtered_data = df.query(query_string)
    else:
        filtered_data  = df
    
    print(query_string)


    
    data = plot_pie_chart(filtered_data)
    data_topics = plot_pie_topic(filtered_data)
    data_pestles = plot_pie_pestles(filtered_data)
    data_sectors = plot_pie_sector(filtered_data)
    data_bar = count_plots_relevance(filtered_data)
    data_intensity  = count_plots_intensity(filtered_data)
    data_likelihood = count_plots_likelihood(filtered_data)
    end_year_plot =  count_plots_end_year(filtered_data)



    context = {

     "topics":topics ,
     "regions":regions,
     "intensities":intensities,
     "relevances":relevances,
     "likelihood":likielihood,
     "end_year":end_year,
     "data_bar":{"values":data_bar.values.tolist() , "labels": data_bar.index.tolist()},
      "data":{"values":data.values.tolist() , "labels": data.index.tolist()},
      "data_pestles":{"values":data_pestles.values.tolist() , "labels": data_pestles.index.tolist()},
      "data_sectors":{"values":data_sectors.values.tolist() , "labels": data_sectors.index.tolist()},
      "data_topics":{"values":data_topics.values.tolist() , "labels": data_topics.index.tolist()},
      "data_intensity":{"values":data_intensity.values.tolist() , "labels": data_intensity.index.tolist()},
      "data_likelihood":{"values":data_intensity.values.tolist() , "labels": data_intensity.index.tolist()},
      "data_end_year":{"values":end_year_plot.values.tolist() , "labels": end_year_plot.index.tolist()}

    }
    print(query_string)

    return render(request , "abc.html" , context)
    
    # EXTRACTING ALL THE VALUES FROM THE FILTERED DATA INTO AN ARRAY

        

            




