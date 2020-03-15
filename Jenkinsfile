pipeline {
   agent any
   parameters {
        choice(name: 'host', description: 'Host type to choose from Linux/Windows', choices: ['linux','windows'])
        credentials(name: 'git_credential', description: 'Git credential ID configured in Jenkins credential', defaultValue: 'git_credential')
        string(name: 'git_branch', description: 'Git branch', defaultValue: 'master')
        string(name: 'git_repo_url', description: 'Git Repo URL', defaultValue: '')
        text(name: 'host_details', defaultValue: '[linux]\nlinux1.com\nlinux2.com \nOR\n [windows]\nwin1.com\nwin2.com', description: 'Should be in the format \n[linux]\nlinux1.com\nlinux2.com \nOR\n [windows]\nwin1.com\nwin2.com')
   }
   environment {
        PATH = "/usr/local/bin:$PATH"
        linux_service_name = 'host-monitor.service'
        linux_user = 'ec2-user'
        win_service_name = 'Hostname Monitor'
        windows_credential  = credentials('ansible_password')
   }
   stages {
      stage('Git Checkout') {
         steps {
            git credentialsId: "${git_credential}", url: "${git_repo_url}"
         }
      }
      stage('Host File update') {
         steps {
             script {
                  if(params.host == "windows"){
                    sh 'echo -e "$host_details\n\n$(cat hosts)" > hosts'
                  }
                  if(params.host == "linux"){
                    sh 'echo "$host_details\n" > hosts'
                  }
             }
         }
      }
      stage("Deploy app"){
          steps {
              script {
                  if(params.host == "windows"){
                    sh 'ansible-playbook playbook.yml -i hosts -l "$host" -e ansible_password="$windows_credential" -e win_service_name="$win_service_name"'
                  }
                  if(params.host == "linux"){
                    sh 'ansible-playbook playbook.yml -i hosts -l "$host" -e linux_user="$linux_user" -e linux_service_name="$linux_service_name"'
                  }
              }
          }
      }
   }
}
