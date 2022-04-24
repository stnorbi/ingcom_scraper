# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json 
import boto3
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()


class IngatlancomScraperPipeline:
        
    def process_item(self, item, spider):
        # calling dumps to create json data.
        line = json.dumps(dict(item)) + "\n"
        # converting item to dict above, since dumps only intakes dict.
        self.file.write(line)                    # writing content in output file.
        return item
 
    def open_spider(self, spider):
        self.file = open('result.json', 'w')
 
    def close_spider(self, spider):
        self.file.close()
        s3 = boto3.client('s3', aws_access_key_id = os.environ['ACCESS_KEY'], aws_secret_access_key = os.environ['SECRET_ACCESS_KEY'])
        bucket_name=os.environ['S3_BUCKET']
        data_bin = open('result.json','r')
        data = data_bin.read()


        try:
            s3.create_bucket(ACL='authenticated-read',Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": "eu-central-1"}
                )

            response_public = s3.put_public_access_block(
                                                        Bucket=bucket_name,
                                                        PublicAccessBlockConfiguration={
                                                                                        'BlockPublicAcls': True,
                                                                                        'IgnorePublicAcls': True,
                                                                                        'BlockPublicPolicy': True,
                                                                                        'RestrictPublicBuckets': True
                                                                                        },
                                                        )
        except:
            pass


        s3.upload_file(Filename='result.json', Bucket=bucket_name, Key=os.environ['PROPERTY_TYPE']+'_' + os.environ['CITY'] + '_'
                                + datetime.now().strftime("%Y%m%d_%H%M%S")+'.json') #“propertytype_county_city_timestamp.csv”
        





        
