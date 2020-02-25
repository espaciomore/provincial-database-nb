import requests
import oauth

def get_studies(domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  PATH = '/api/study'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + PATH, headers = headers)

  studies = response.json()

  return studies

def get_study(id, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  STUDY = '/api/study/'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + STUDY + id, headers = headers)

  study = response.json()

  return study

def get_study_users(study_id, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  PATH = '/api/study/' + study_id + '/user'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + PATH, headers = headers)

  users = response.json()

  return users

def get_study_user(study_id, user_id, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  PATH = '/api/study/' + study_id + '/user/'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + PATH + user_id, headers = headers)

  user = response.json()

  return user
