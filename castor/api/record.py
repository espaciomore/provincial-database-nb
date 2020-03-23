import requests
import oauth

def get_study_records(studyID, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  RECORDS = '/api/study/' + studyID + '/record'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + RECORDS, headers = headers)

  records = response.json()

  return records

def get_study_record(Id, studyID, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  RECORDS = '/api/study/' + studyID + '/record/'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + RECORDS + Id, headers = headers)

  record = response.json()

  return record
  
def get_study_record_data_point(Id, studyID, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  RECORDS = '/api/study/' + studyID + '/record/' + Id + '/data-point/study'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + RECORDS, headers = headers)

  data = response.json()

  return data  
