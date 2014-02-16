from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/test')
def test():
    return render_template('index.html')



# @app.route('/')
# def search_job():
#     # content = request.json
#     return 'search_job'

@app.route('/foo')
def foo():
    return "hi"


@app.route('/all_jobs')
def all_jobs():
    jobs = None
    with open('data/pc.json') as f:
        jobs = json.load(f)
    return jsonify({'data':jobs})


# @app.route('/get_jobs')
# def get_jobs():
#     filters = request.json
#     locations = filters.get('country', None)    
#     start_date = filters.get('start_date')
#     all_jobs = None
#     with open('data/pc.json') as f:
#         all_jobs = json.load(f)

#     jobs = []
#     for j in all_jobs:
#         if j['location'] in locations:
#             jobs.append()
        
#     return jsonify({'data':jobs})

if __name__ == '__main__':
    app.run(debug=True)