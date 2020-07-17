## upload.py

def upload_maven():
    """Upload artifact to Maven 2 repository"""
    params = (('repository', repository),)
   
    finalpath = path + '/' + artifact_name
    
    if ('tar.gz' in artifact_name):
        pass
    
    artname_lst = artifact_name.split("-", 10)
    versionnumber, exten = os.path.splitext(artname_lst[-1])
    
    extension = exten
    
    actual_artifact_name = '-'.join(artname_lst[:-1])

    files = {
        'maven2.groupId': (None, directory),
        'maven2.artifactId': (None, actual_artifact_name),
        'maven2.version': (None, versionnumber),
        'maven2.asset1': (artifact_name, open(finalpath, 'rb')),
        'maven2.asset1.extension': (None, extension),
        'maven2.generate-pom': (None, True)  ## dont know if this will work
    }

    response = requests.post(url, params=params, files=files, auth=auth, proxies=proxies, verify=False)
    if response.status_code == 204:
        print("Nexus Upload successful")
        return sys.exit(0)
    elif response.status_code == 400 and ("release" in repository or "staging" in repository):
        print("Nexus Upload failed. Please modify version number")
        return sys.exit(1)
    else:
        print("Nexus Upload failed")
        return sys.exit(1)
    print("Status code: ",response.status_code)



def upload_npm():
    """Upload artifact to NPM type repository"""
    params = (('repository', repository),)
    finalpath = path + '/' + artifact_name
    files = {
	  'npm.asset' : (None, finalpath),
    }
    response = requests.post(url, params=params, files=files, auth=auth)
    if response.status_code == 204:
        print("Nexus Upload successful")
        return sys.exit(0)
    else:
        print("Nexus Upload failed")
        return sys.exit(1)
    print("Status code: ",response.status_code)



def upload_raw():
    """Upload artifact to RAW type repository"""
    params = (('repository', repository),)
	
    finalpath = path + '/' + artifact_name
    print("Uploading to Nexus Repository: "+repository)
    files = {

	  'raw.directory' : (None, directory),
	  'raw.asset1' : (None, finalpath),
	  'raw.asset1.filename': (None, artifact_name)
    }
	#raw.assetN : (None, 
	#raw.assetN.filename
    #response = requests.post("http://localhost:8081/service/rest/v1/components",params=params, files=files, auth=auth)
    response = requests.post(url, params=params, files=files, auth=auth)
    if response.status_code == 204:
        print("Nexus Upload successful")
        return sys.exit(0)
    elif response.status_code == 400 and ("release" in repository or "staging" in repository):
        print("Nexus Upload failed. Please modify version number")
        return sys.exit(1)
    else:
        print("Nexus Upload failed")
        return sys.exit(1)
    print("Status code: ",response.status_code)

