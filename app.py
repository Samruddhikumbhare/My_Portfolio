from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Samruddhi Nikhare"
    projects = [
        {
            "title": "CI/CD pipeline with GitHub webhook", 
        },
        {
            "title": "Infrastructure as Code (IaC) with Terraform",
        },
        {
            "title": "Automated Configuration Management with Ansible",
        },
        {
            "title": "Containerized Application Deployment with Docker Compose",
        }
    ]
    return render_template('index.html', name=name, projects=projects)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

