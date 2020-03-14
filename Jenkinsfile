pipeline {
   agent any
   parameters {
        choice(name: 'host', description: 'Host type to choose from Linux/Windows', choices: ['linux','windows'])
        string(name: 'git_credential', description: 'Git credential', defaultValue: 'git_credential')
        string(name: 'git_branch', description: 'Git branch', defaultValue: 'master')
        string(name: 'git_repo_url', description: 'Git Repo URL', defaultValue: '')
        string(name: 'linux_user', description: 'Linux user', defaultValue: 'ec2-user')
        string(name: 'linux_service_name', description: 'Name for linux service', defaultValue: 'host-monitor.service')
        string(name: 'win_service_folder', description: 'Windows directory to copy script and logs', defaultValue: 'C:\\Process')
        string(name: 'win_service_name', description: 'Name of the windows service', defaultValue: 'Hostname Monitor')
   }
   environment {
    PATH = "/usr/local/bin:$PATH"
    windows_credential  = credentials('ansible_password')
   }
   stages {
      stage('Git Checkout') {
         steps {
            git credentialsId: "${git_credential}", url: "${git_repo_url}"
         }
      }
      stage("Deploy app"){
          steps {
              script {
                  if(params.host == "windows"){
                    sh ''
                    sh 'ansible-playbook playbook.yml -i hosts -l "$host" -e ansible_password="$windows_credential" -e win_service_folder="$win_service_folder" -e win_service_name="$win_service_name"'
                  }
                  if(params.host == "linux"){
                    sh 'ansible-playbook playbook.yml -i hosts -l "$host" -e linux_user="$linux_user" -e linux_service_name="$linux_service_name"'
                  }
              }
          }
      }
   }
}
