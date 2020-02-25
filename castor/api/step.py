import requests
import oauth

def get_study_steps(study_id, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  PATH = '/api/study/' + study_id + '/step'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + PATH, headers = headers)

  steps = response.json()

  return steps

def get_study_step(study_id, step_id, domain='us'):
  ACCESS_TOKEN = oauth.get_token(domain)['access_token']
  BASE_URL = 'https://' + ('data' if domain == 'us' else domain) + '.castoredc.com'
  PATH = '/api/study/' + study_id + '/step/'

  headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
  }

  response = requests.get(url = BASE_URL + PATH + step_id, headers = headers)

  step = response.json()

  return step
