pipeline {
    agent any  // Run on any available agent

    environment {
        NODEJS_HOME = tool 'NodeJS'  // Ensure Jenkins has Node.js installed
        PATH = "${NODEJS_HOME}/bin:${env.PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Lazzy-bug/ToDoList.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'npm test'  // Ensure test scripts are defined in package.json
            }
        }

        stage('Lint Code') {
            steps {
                sh 'npm run lint'  // Run linting (if configured)
            }
        }

        stage('Build Project') {
            steps {
                sh 'npm run build'  // Adjust if needed
            }
        }

        stage('Deploy (Optional)') {
            steps {
                echo "Deploy step (Configure as needed)"
                // Example: sh 'scp -r build/ user@server:/var/www/todolist'
            }
        }
    }

    post {
        success {
            echo "🎉 Build and tests passed!"
        }
        failure {
            echo "❌ Build failed. Check logs."
        }
    }
}
