import boto3
import requests
import os
import sys

credentials_provider_url = ""

class AWSS3Service:
    """
    AWS S3 class with functionality
    upload , list folder and read files in a given S3 Bucket
    """

    s3_session = None 
    s3_client = None 
    s3_region = None 
    s3_bucket = None 

    def __init__(self):
       print("Initialized an instance - AWSS3Service")

    def initlialize_credentials_from_url(self, url):
        print("Getting AWS credentials...")
        response_json = requests.get(url).json()
        self.s3_region = response_json["AWS_REGION"]
        self.create_connection(response_json["AWS_ACCESS_KEY_ID"], response_json["AWS_SECRET_ACCESS_KEY"], response_json["AWS_BUCKET_NAME"])

    def initlialize_credentials_from_static_values(self, aws_region, aws_access_key_id, aws_secret_access_key, aws_bucket_name):
        print("Loading provided credentials...")
        self.s3_region = aws_region
        self.create_connection(aws_access_key_id, aws_secret_access_key, aws_bucket_name)

    def create_connection(self, aws_access_key_id, aws_secret_access_key, aws_bucket_name):
        print("Establishing S3 connection...")
        boto_s3 = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
        self.s3_resource = boto_s3.resource("s3")
        self.s3_client = boto_s3.client("s3")
        self.s3_bucket = aws_bucket_name
        self.s3_session = self.s3_resource.Bucket(aws_bucket_name)
    
    def upload_large_file(self, local_filepath, s3_filepath):
        print("Uploading upload_large_file " + local_filepath + " to s3path=" + s3_filepath)
        bucket = self.s3_bucket
        key = s3_filepath

        tc = boto3.s3.transfer.TransferConfig()
        t = boto3.s3.transfer.S3Transfer(client=self.s3_client, config=tc)
        t.upload_file(local_filepath, self.s3_bucket, s3_filepath)

    def get_filename_from_key(self, s3_filepath):
        return s3_filepath.split("/")[-1]
    
    def list_bucket_contents(self, s3_folderpath):
        print("Listing bucket contents...")
        contents = []
        for each_object in self.s3_session.objects.filter(Prefix=s3_folderpath):
            contents.append(each_object.key)
        return contents
    
    def upload_file(self, local_filepath, s3_filepath):
        print("Uploading file " + local_filepath + " to s3path=" + s3_filepath)
        self.s3_session.upload_file(local_filepath, s3_filepath)

    def download_file(self, s3_filepath):
        local_filepath = self.get_filename_from_key(s3_filepath)
        self.s3_session.download_file(s3_filepath, local_filepath)
    
    def download_file_to_directory(self, s3_filepath, local_filepath):
        print("Downloading file " + s3_filepath + " to " + local_filepath)
        if not os.path.exists(os.path.dirname(local_filepath)):
            os.makedirs(os.path.dirname(local_filepath))
        self.s3_session.download_file(s3_filepath, local_filepath)

    def download_folder(self, s3_folderpath):
        s3_folders_list = self.list_bucket_contents(s3_folderpath)
        for s3_each_file in s3_folders_list:
            self.download_file(s3_each_file)
    """
    Historical log analysis specific functions
    """
    def create_file(self, filename, filecontent):
        text_file = open(filename, "w")
        text_file.write(filecontent)
        text_file.close()

    def read_file(self, filename):
        text_file = open(filename, "r")
        content = text_file.read()
        text_file.close()
        return content
        
    def save_mappings_to_s3(self, dictionary_to_upload, s3_upload_directory):
        s3_files_list = self.list_bucket_contents(s3_upload_directory)
        filesnames_list = [ (self.get_filename_from_key(each)) for each in s3_files_list]
        for key in dictionary_to_upload:
            if key not in filesnames_list:
                self.create_file(key, dictionary_to_upload[key])
                self.upload_file(key, s3_upload_directory + "/" + key)
    
    def read_mappings_from_s3(self, mapping_key, s3_upload_directory):
        s3_files_list = self.list_bucket_contents(s3_upload_directory)
        filesnames_list = [ (self.get_filename_from_key(each)) for each in s3_files_list]
        if mapping_key in filesnames_list:
            self.download_file(s3_upload_directory + "/" + mapping_key)
            return self.read_file(mapping_key)
        else:
            return "NOT_FOUND"

def show_console_separator():
    print("-------------------------")


def main():
    show_console_separator()
    print("Initializing script...")
    show_console_separator()
    print("help -- version1 - Args - filename s3filepath AWS_REGION AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_BUCKET_NAME")
    print("help -- version2 - Args - filename s3filepath CREDENTIALS_URL")
    show_console_separator()
    
    service = AWSS3Service()
    
    argv_length = len(sys.argv)
    
    if argv_length == 7:
        print("Detected args required - filename s3filepath AWS_REGION AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_BUCKET_NAME")
        service.initlialize_credentials_from_static_values(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif argv_length == 4:
        print("Detected args required - filename s3filepath CREDENTIALS_URL")
        service.initlialize_credentials_from_url(sys.argv[3])
    else:
        raise ValueError('Proper arguments are required.') 

    # service.upload_file("meta.json", "historyarchives/clean/meta12441.json")
    # print(service.list_bucket_contents("historyarchives"))
    # service.read_file("historyarchives/meta1244.json")
    # service.download_folder("historyarchives/clean/")

    # service.save_mappings_to_s3(dict, "testmappings")
    service.upload_large_file(sys.argv[1], sys.argv[2])
    #print(service.read_mappings_from_s3("1234", "testmappings"))

if __name__ == '__main__':
    main()
