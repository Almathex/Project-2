pipeline{
    agent any
    stages{
        stage('Ansible'){
	    steps{
                sh './scripts/ansible.sh'
	    }
        }
	stage('Test'){
	    steps{
		sh './scripts/test.sh'
	    }
	}
        stage('Build'){
            steps{
               sh './scripts/build.sh'
            }
        }
        stage('Deploy'){
            steps{
                sh './scripts/deploy.sh'
            }
        }
    }
}
