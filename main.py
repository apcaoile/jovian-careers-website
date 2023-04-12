from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'RS. 10,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'RS. 15,000'
}, {
  'id': 3,
  'title': 'Frontend Developer',
  'location': 'Remote',
  'salary': 'RS. 12,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'USA'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
