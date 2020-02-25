
import sys
sys.path.insert(1, './castor/api')

from user import get_users, get_user
from study import get_studies, get_study, get_study_user
from export_data import get_export_data
from record import get_records, get_record
from step import get_study_step
from flask import Flask, render_template, request
from json import dumps, loads
from datetime import datetime as dt
import os

f = open('devel.env', 'r')
env = loads(f.read())

for key in env.keys():
  os.environ[key] = env[key]

app = Flask(__name__)
#
# FILTER TEMPLATES
#
@app.template_filter('dumpjson')
def dumpjson(jsonObject):
  return dumps(jsonObject, indent=2)

@app.template_filter('date')
def date(datetimeString):
  dateTime = dt.strptime(datetimeString, '%Y-%m-%d %H:%M:%S.%f')
  return '{:%Y-%m-%d %H:%M}'.format(dateTime)

#
# ROUTES
#
@app.route('/')
@app.route('/index')
def index():
  usersData = get_users()
  studiesData = get_studies()

  return render_template('index.html', users=usersData['_embedded']['user'], studies=studiesData['_embedded']['study'])

@app.route('/study/<string:studyID>/records')
def study_records(studyID):
  domain=request.args.get('domain')

  recordsData = get_records(studyID, domain)
  
  records = recordsData['_embedded']['records']
  attributes = records[0].keys()
  attributes.remove('_embedded')
  attributes.remove('_links')
  attributes.remove('id')
  attributes.remove('record_id')
  
  return render_template('study_records.html', studyID=studyID, records=records, keys=sorted(attributes), size=len(records), domain=domain)

@app.route('/api/user/<string:userID>')
def user(userID):
  userData = get_user(userID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=userData)

@app.route('/api/study/<string:studyID>')
def study(studyID):
  studyData = get_study(studyID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=studyData)

@app.route('/api/study/<string:studyID>/user/<string:userID>')
def study_user(studyID, userID):
  studyUserData = get_study_user(studyID, userID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=studyUserData)  

@app.route('/api/study/<string:studyID>/step/<string:stepID>')
def study_step(studyID, stepID):
  studyStepData = get_study_step(studyID, stepID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=studyStepData)  

@app.route('/api/study/<string:studyID>/record/<string:recordID>')
def record(studyID, recordID):
  recordData = get_record(recordID, studyID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=recordData)

@app.route('/api/study/<string:studyID>/export/data')
def export_data(studyID):
  exportData = get_export_data(studyID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=exportData)

if __name__ == '__main__':
  app.run()