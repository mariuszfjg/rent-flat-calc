node{
    stage('VirtualEnv') {
        sh "virtualenv venv"
        sh "source venv/bin/activate"
        sh "pip3 install requests"
    }
    stage('Run App') {
        sh 'python3 main.py'
    }

}