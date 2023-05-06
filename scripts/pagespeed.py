# Import required packages 
import json
import requests
import pandas as pd
import urllib
import time
import io
import os

# Define URL  
# url = 'https://docs.google.com/document/d/1npeFQ8Xdj9YcVBiaKRkiOOOOjza3wJgVUSW7IRC7J6U/edit'
url = "https://www.twitch.tv/videos/1801584512"
# cert_file = "certs/target.cer"
# os.environ["REQUESTS_CA_BUNDLE"] = cert_file
# API request url
result = urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}/&strategy=mobile'.format(url)).read().decode('UTF-8')

# Convert to json format
result_json = json.loads(result)

# print(result_json)

with open('pagespeed/result1.json', 'w') as outfile:
  json.dump(result_json, outfile)


# Create dataframe to store responses
df_pagespeed_results = pd.DataFrame(columns=
          ['url',
          'Overall_Category',
          'Largest_Contentful_Paint',
          'First_Input_Delay',
          'Cumulative_Layout_Shift',
          'First_Contentful_Paint',
          'Time_to_Interactive',
          'Total_Blocking_Time',
          'Speed_Index'])  

print(df_pagespeed_results)


response_object = {}

urls = ['https://www.twitch.tv/videos/1801584512', 'https://www.twitch.tv/videos/1801584512']
# Iterate through the df
for url in range(0, len(urls)):

        # Make request
        pagespeed_results = urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=mobile'.format(url)).read().decode('UTF-8')

        # Convert to json format
        pagespeed_results_json = json.loads(pagespeed_results)

        # Insert returned json response into response_object
        response_object[url] = pagespeed_results_json
        time.sleep(30)
        
        print(response_object[url])

for (url, x) in zip(
    response_object.keys(),
    range(0, len(response_object))
):

        # URLs
        df_pagespeed_results.loc[x, 'url'] =\
            response_object[url]['lighthouseResult']['finalUrl']

        # Overall Category
        df_pagespeed_results.loc[x, 'Overall_Category'] =\
            response_object[url]['loadingExperience']['overall_category']   

        # Core Web Vitals     

        # Largest Contentful Paint    
        df_pagespeed_results.loc[x, 'Largest_Contentful_Paint'] =\
        response_object[url]['lighthouseResult']['audits']['largest-contentful-paint']['displayValue']

        # First Input Delay 
        fid = response_object[url]['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']
        df_pagespeed_results.loc[x, 'First_Input_Delay'] = fid['percentile']

        # Cumulative Layout Shift    
        df_pagespeed_results.loc[x, 'Cumulative_Layout_Shift'] =\
        response_object[url]['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue']

        # Additional Loading Metrics 

        # First Contentful Paint 
        df_pagespeed_results.loc[x, 'First_Contentful_Paint'] =\
        response_object[url]['lighthouseResult']['audits']['first-contentful-paint']['displayValue']

        # Additional Interactivity Metrics 

        # Time to Interactive  
        df_pagespeed_results.loc[x, 'Time_to_Interactive'] =\
        response_object[url]['lighthouseResult']['audits']['interactive']['displayValue']

        # Total Blocking Time   
        df_pagespeed_results.loc[x, 'Total_Blocking_Time'] =\
        response_object[url]['lighthouseResult']['audits']['total-blocking-time']['displayValue']

        # Speed Index
        df_pagespeed_results.loc[x, 'Speed_Index'] =\
        response_object[url]['lighthouseResult']['audits']['speed-index']['displayValue']
        
        
df_pagespeed_results.loc[x, 'Time_to_Interactive'] =\
response_object[url]['lighthouseResult']['audits']['interactive']['displayValue']

summary = df_pagespeed_results

df_pagespeed_results.head()

#Download csv file 
summary.to_csv('pagespeed_results.csv')