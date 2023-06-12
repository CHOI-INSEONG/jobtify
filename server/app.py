from flask import Flask, request, make_response, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from flask_cors import CORS

# Use a service account.
cred = credentials.Certificate('./env/jobtify-jcl-firebase-adminsdk-486oy-8b1b68b8bd.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)
CORS(app)

@app.route('/register_user', methods=['POST'])
def register_user():
    data = request.json
    uid = data.get('uid')
    keywords = data.get('keywords')
    country = data.get('country')
    sites = data.get('sites')
    response = make_response(jsonify({'status':'good'}))
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"
    print(data)
    doc_ref = db.collection(u'users').document(uid)
    doc_ref.set({
        u'keywords': keywords,
        u'country': country,
        u'sites': sites
    })
    print(response)
    return response

@app.route('/get_jds', methods=['POST'])
def get_jds():
    jds=[]
    data = request.json
    print(data)
    uid = data.get('uid')
    doc_ref = db.collection(u'users').document(uid).collection(u'jds')
    docs = doc_ref.stream()
    for doc in docs:
        jds.append(doc.to_dict())
    response = make_response(jsonify(jds))
    print(response)
    return response

@app.route('/set_jds', methods=['POST'])
def set_jds():
    data = request.json
    print(data)
    response = make_response(jsonify({'status': 'good'}))
    print(response)
    return response

@app.route('/get_jd', methods=['POST'])
def get_jd():
    data = request.json
    print(data)
    uid = data.get('uid')
    doc_ref = db.collection(u'users').document(uid).collection(u'jds')
    jds = doc_ref.where(u'link', u'==', data.get('link')).stream()
    info_ref = db.collection(u'users').document(uid)
    info = info_ref.get()
    site_arr = []
    for jd in jds:
        if jd.to_dict()['link'] == data.get('link'):
            site_arr.append(jd.to_dict()['site'])
            response = make_response(
                jsonify(
                    {
                        'bookmark':jd.to_dict()['bookmark'],
                        'company':jd.to_dict()['company'],
                        'link':jd.to_dict()['link'],
                        'title':jd.to_dict()['title'],
                        'site':site_arr,
                        'keywords':info.to_dict()['keywords'],
                        'country':info.to_dict()['country']
                    }
                )
            )
    print(response)
    return response

@app.route('/set_bookmark', methods=['POST'])
def set_bookmark():
    data = request.json
    print(data)
    uid = data.get('uid')
    doc_ref = db.collection(u'users').document(uid).collection(u'jds')
    docs = doc_ref.where(u'link', u'==', data.get('link')).stream()
    for doc in docs:
        doc_ref.document(doc.id).set({
            u'bookmark':data.get('bookmark'),
            u'company':doc.to_dict()['company'],
            u'link':doc.to_dict()['link'],
            u'title':doc.to_dict()['title'],
            u'site':doc.to_dict()['site']
        })
    response = make_response(jsonify({'status': 'good'}))
    print(response)
    return response

@app.route('/get_crawl_info', methods=['POST'])
def get_crawl_info():
    data = request.json
    print(data)
    json_arr = []
    uids_stream = db.collection(u'users').stream()
    for uid in uids_stream:
        json_uid = {
            'uid': uid.id,
            'country': uid.to_dict()['country'],
            'keywords': uid.to_dict()['keywords'],
            'sites': uid.to_dict()['sites']
        }
        json_arr.append(json_uid)
    response = make_response(jsonify(json_arr))
    print(response)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)