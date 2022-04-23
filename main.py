import os, json, sys
import pandas as pd
from src.searching import IngComSearch

try:
    if os.environ.get('ENV') in ['dev','local']:
        from dotenv import load_dotenv
        load_dotenv()

    # get environment variables
    county = os.environ.get('COUNTY')
    proptype = os.environ.get('PROP_TYPE')
    city = os.environ.get('SEARCH_CITY_URL')
    if city is None:
        city = os.environ.get('SEARCH_CITY')
    proptype = os.environ.get('PROP_TYPE')

    if all(v is None for v in [county, city, proptype]):
        print('Necessary environment variables missing... Run is over')
        exit(0)
except Exception as err:
    print(err)
    print("Error has been happened. Environment variables are not loaded...")
    print("Execution has been stopped... Clean exit")
    exit(0)
    

def main():
    try:
        # initialize IngComSearch class with parameters
        ingcs = IngComSearch(city=city, proptype=proptype, county=county)
        ads = []
        generated = ingcs.extract_ads() #//TODO: define function
        # restults is appending to a list
        for ad in generated:
            if ad is not None:
                ads = ad + ads
            else:
                break
        # convert to dataframe for analysis
        if(len(ads) > 0):
            df = pd.DataFrame(ads)
            proptype = ingcs.get_property_type()
            # save results to S3
            ingcs.save_results(df) #//TODO: define function and add parameters
        else:
            print("No postings found!")
    except Exception as err:
        print("Error running scraper...")
        print("Exiting scraper with exit code 0...")
        print(err)
        exit(0)


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, TypeError, NameError) as err:
        print(err)
        print('Error during execute main function')
        exit(0)