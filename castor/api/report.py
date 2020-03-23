import requests
import oauth

def get_report_data_point_collection(studyID, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  PATH = '/api/study/' + studyID + '/data-point-collection/report-instance'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + PATH, headers = headers)

  collection = response.json()

  return collection  