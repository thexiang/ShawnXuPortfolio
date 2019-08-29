Title: Ansible
Date: 2019-08-21
Category: IAC
Tags: Ansible

create virtual environment:

    python -m venv introansible
    source introansible/bin/activate

install ansible:

    pip install ansible
    ansible localhost -a "echo 'hi'"

generate keys, and visit them,
put public key on the 

    ssh-keygen -t rsa -b 4096 -o -C xiangxu1105@gmail.com
    /User/shawn/.ssh/introAnsible
    ls ~/.ssh/ | grep introAnsible

Core Concepts:

![](Untitled-6ef287d1-d882-4e4a-8086-37374d6cb121.png)

1. Modules
2. Tasks
3. Roles
4. Playbooks
5. Inventory
6. YAML

- What are Ansible Modules?

    Code, typically in Python, provided by Ansible to perform an action.

    Ex:

    - clone a git repo
    - enable the OS' firewall
    - send a notification about a depolymnet
- What are Ansible tasks?

    YAML instructions that invoke Ansible modules to execution an action

    Ex:

        - name: ensure Git is installed
        	apt: name=git-core state=present update_cache=yes
        	become: true

    ad-hoc

        ansible localhost -m setup
        
        ansible localhost -m apt -a "name=git-core state=present update_cache=yes" -b -K -e ansible_python_interpreter=/user/bin/python3

- What's an Ansible role?

    Roles are a required file naming and directory convention for grouping tasks and variables

- Why use roles?

    Roles make groups of Ansible tasks reusable, both for different environments and for usage between projects.

- What are playbooks?

    Playbooks are the top-level collection that contain one or more roles, many tasks, variable and all other information necessary for execution

        mkdir roles
        cd roles
        mkdir common
        cd common
        mkdir tasks
        cd tasks
        

        ansible-playbook -i ./hosts --private-key=./first_playbook playbook.yml

        ssh -i ./first_playbook deployer@174.138.43.168


