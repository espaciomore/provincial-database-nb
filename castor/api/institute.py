import requests
import oauth

def get_study_institutes(studyID, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  PATH = '/api/study/' + studyID + '/institute'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + PATH, headers = headers)

  institutes = response.json()

  return institutes

def get_study_institute(Id, studyID, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  PATH = '/api/study/' + studyID + '/institute/'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + PATH + Id, headers = headers)

  institute = response.json()

  return institute  
