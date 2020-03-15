# Hostname Monitor Service
This project showing how to provision, deploy and run script as service on both Linux and Windows.
##
## File Details
* _.gitignore_ - Git ignore file.
* _ansible.cfg_ - Ansible configuration to configure the inventory details
* _host-monitor.service_ - Linux based service file for configuring the service
* _hosts_ - Inventory file for Ansible to have the server details where the service will be deployed
* _Jenkinsfile_ - Jenkins pipeline file to create the service on both windows and linux
* _playbook.yml_ - Ansible playbook to deploy copy the files and to create the service on both windows and linux
* _process.py_ - Simple python script to print hostname and date stamp
* _README.md_ - This file

##
## CI/CD Pipeline Flow

``` 
Github -> Jenkins with Ansible (on linux) -> Target (Windows/Linux Server)
```

Ansible can be installed on a different server like below but for this project the above flow is used by having Jenkins and Anisble on same linux server.

``` 
Github -> Jenkins (on linux) -> Ansible (linux) -> Target (Windows/Linux Server)
```

##

## Prerequisites

#### Github
* Nothing required

#### Jenkins
* Install Git for checkout repo during build.
* Install python `sudo yum install python3 -y` as it required for Ansible.
* Install Ansible `sudo yum install python3 -y` and add ansible bin directory `/usr/local/bin` to Environment variable `PATH` 
* Make sure the SSH keys used to connect linux target servers is under `/var/lib/jenkins/.ssh/` with owner as jenkins for user and group with required permission.
* Create pipeline to use _Jenkinsfile_ file from Github repo.
* Add credentials to Jenkins if the repo is private and configure it in pipeline. 
* Configure the pipeline to have listed parameters to be passed on each build.
* Install WinRM which is used by Ansible for connecting to Windows. You can use `sudo pip3 install pywinrm` for linux host.
``` 
Parameter Name: host, Paramater Value: windows/linux; // This is deciding which target the pipeline should be executed. It can be either windows or linux, but not both.

Common parameters:
*****************
Parameter type: Credentials parameter, Parameter Name: git_credential, Paramater Value: <User name and password of git repo>;
Parameter type: Choice/String parameter, Parameter Name: git_branch, Paramater Value: <Branch of git repo>; // master
Parameter type: Choice/String parameter, Parameter Name: git_repo_url, Paramater Value: <Clone URL of git repo>;

```
#### Ansible
* No seperate configuration for Ansible as we covered it in above section.

#### Linux Targets
*  No seperate configs but esnure the SSH connectivity from Jenkins
 
#### Windows Targets
* Create new user name and password with Admin rights which will be used to connect by ansible to connect and run playbook.
* Configure WinRM if not already done. Details on how to configure is available in https://docs.ansible.com/ansible/latest/user_guide/windows_setup.html#winrm-setup.

##

## Implementation
* Implementation is simple. Change the target server details on hosts file. For Linux server add hostname below [linux] and windows server below [windows].
Once done push it to repo and configure it to consumed by Jenkins pipeline to read the file `Jenkinsfile`.
Ensure the other parameter values are also given if default value are not set for those.

## Assumption/Key Details
* User/SSH details for bot linux and windows hosts are already configured.
* Linux user used here is `ec2-user`
* Windows user used here is `Test`
* Script and log will be available in `/app/` for Linux targets
* Script and log will be available in `C:\Process\` for Linux targets
* Linux service name `host-monitor.service`
* Windows service name `Hostname Monitor`