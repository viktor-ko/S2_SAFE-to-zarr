import re
import os
from google.cloud import storage


def extract_sensing_time(filename):
    match = re.search(r'_(\d{8}T\d{6})_', filename)  #Match YYYYMMDDTHHMMSS between underscores
    if match:
        timestamp = match.group(1)
        return f"{timestamp[:4]}-{timestamp[4:6]}-{timestamp[6:8]} {timestamp[9:11]}:{timestamp[11:13]}:{timestamp[13:]}"
    return None


def create_gcs_bucket(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name) #Create a bucket object with the desired name
    new_bucket = storage_client.create_bucket(bucket, location="EU") #Create the bucket located on servers in the EU region
    print(f"Bucket {new_bucket.name} created in {new_bucket.location}.")
    return new_bucket


def upload_folder_to_gcs(bucket_name, source, destination_blob):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"  #Free tier

    for root, _, files in os.walk(source): #Scan the folder for all files
        for file in files:
            local_file_path = os.path.join(root, file)

            #Preserve folder structure in GCS
            relative_path = os.path.relpath(local_file_path, source)
            destination_blob_name = os.path.join(destination_blob, relative_path)

            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(local_file_path)

            print(f"Uploaded {local_file_path} to gs://{bucket_name}/{destination_blob_name}")