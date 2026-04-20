# DevOps CI/CD Sample Project

A simple Flask REST API with automated CI/CD pipeline using Jenkins and Docker.

## Project Structure

```
my-cicd-project/
├── app.py              # Flask application
├── test_app.py         # Unit tests
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker container definition
├── Jenkinsfile         # Jenkins pipeline configuration
└── README.md           # This file
```

## Application Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check endpoint |
| `/hello` | GET | Hello World endpoint |
| `/api/info` | GET | Application info endpoint |

## Running Locally

### Using Python
```bash
pip install -r requirements.txt
python app.py
```

### Using Docker
```bash
docker build -t my-cicd-project .
docker run -p 5000:5000 my-cicd-project
```

### Running Tests
```bash
pytest test_app.py -v
```

---

## Jenkins Setup

### 1. Configure Jenkins Credentials for DockerHub

1. Login to Jenkins dashboard
2. Go to **Manage Jenkins** → **Manage Credentials**
3. Click on **Add Credentials**
4. Select **Username with password** kind
5. Fill in the details:
   - **Kind**: Username with password
   - **ID**: `dockerhub-username` (for username)
   - **ID**: `dockerhub-password` (for password)
   - **Username**: Your DockerHub username
   - **Password**: Your DockerHub password or access token
6. Create TWO separate credentials:
   - One with ID: `dockerhub-username`
   - One with ID: `dockerhub-password`

### 2. Create Jenkins Job

1. Go to Jenkins dashboard
2. Click **New Item**
3. Enter job name (e.g., `my-cicd-project`)
4. Select **Pipeline** and click OK
5. In the job configuration:
   - Under **General** section, check **GitHub project**
   - Enter your GitHub repository URL (e.g., `https://github.com/yourusername/my-cicd-project/`)
   - Under **Build Triggers** section:
     - Check **GitHub hook trigger for GITScm polling**
   - Under **Pipeline** section:
     - Select **Pipeline script from SCM**
     - Choose **Git**
     - Enter your repository URL
     - Branch specifier: `*/main` (or your branch name)
     - Script path: `Jenkinsfile`
6. Click **Save**

### 3. Configure GitHub Webhook

1. Go to your GitHub repository
2. Click on **Settings** → **Webhooks**
3. Click **Add webhook**
4. Fill in the details:
   - **Payload URL**: `http://<your-jenkins-url>/github-webhook/`
     - Example: `http://jenkins-server:8080/github-webhook/`
   - **Content type**: `application/json`
   - **Which events would you like to trigger this webhook?**: 
     - Select **Just push events**
   - Check **Active**
5. Click **Add webhook**

### 4. Verify Webhook Connection

1. In GitHub webhook settings, you should see a green checkmark next to your webhook
2. Make a commit and push to trigger the pipeline
3. Check Jenkins build console output for pipeline execution

---

## Pipeline Stages

The Jenkins pipeline includes the following stages:

1. **Checkout** - Clones the repository
2. **Install Dependencies** - Installs Python packages from requirements.txt
3. **Run Tests** - Executes pytest test cases
4. **Docker Build** - Builds Docker image with tag
5. **Docker Push** - Pushes image to DockerHub

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DOCKERHUB_USERNAME` | DockerHub username (from credentials) |
| `DOCKERHUB_PASSWORD` | DockerHub password (from credentials) |
| `IMAGE_NAME` | Name of the Docker image |
| `IMAGE_TAG` | Build number used as image tag |

## Troubleshooting

### Webhook not triggering build
- Verify Jenkins URL is accessible from GitHub
- Check GitHub webhook delivery logs
- Ensure GitHub hook trigger is enabled in Jenkins job

### Docker push fails
- Verify DockerHub credentials are correct
- Ensure you have permission to push to the repository
- Check DockerHub account is not locked

### Tests failing
- Check Python version compatibility
- Ensure all dependencies are installed
- Review pytest output for specific failures