#!/bin/bash

<< task
Deploy the Django event manager project and handle the code for errors.

#replace this for requirements.txt > cd django-event-manager-project >> vim requirements.txt
asgiref==3.4.1
brotli==1.1.0
django==3.2.25
django-jazzmin==2.6.1
django-quill-editor==0.1.40
gunicorn==21.2.0
packaging==21.3
sqlparse==0.4.4
tzdata==2024.1
whitenoise==5.3.0

#and alwaye runing the project befor manage.py file activect for virtual environment
python3 -m venv venv
source venv/bin/activate

task

code_clone() {
    echo "Cloning the Django app..."
    if [ ! -d "django-event-manager-project" ]; then
        git clone https://github.com/biisal/django-event-manager-project.git
        if [ $? -ne 0 ]; then
            echo "Failed to clone the repository."
            return 1
        fi
    else
        echo "*** The code directory already exists ***"
        cd django-event-manager-project || return 1
    fi
}

#fix_requirements() {
#    echo "Checking and fixing requirements.txt..."
#    if ! pip3 install "asgiref==3.8.1"; then
#        echo "asgiref==3.8.1 is not available, replacing with available version..."
#        sed -i 's/asgiref==3.8.1/asgiref==3.7.2/' requirements.txt
#    fi
#}


install_requirements() {
    echo "Installing dependencies..."

    # Update package lists
    sudo apt-get update

    # Install pip3 if not installed
    sudo apt-get install -y python3-pip

    # Skip fixing permissions if the directory doesn't exist
#    if [ -d "/home/vagrant/.cache/pip" ]; then
#        sudo chown -R vagrant:vagrant /home/vagrant/.cache/pip
#    fi

    # Install Python dependencies from requirements.txt
    sudo -H pip3 install -r requirements.txt

    if [ $? -ne 0 ]; then
        echo "Dependency installation failed."
        return 1
    fi
}



required_restarts() {
    echo "Applying migrations..."
    sudo python manage.py migrate
    if [ $? -ne 0 ]; then
        echo "Migrations failed."
        return 1
    fi
    # Uncomment these if needed for your environment
    # sudo chown $USER /var/run/docker.sock
    # sudo systemctl enable docker
    # sudo systemctl enable nginx
    # sudo systemctl restart docker
}

deploy() {
    echo "Starting Django development server..."
    #python manage.py runserver localhost:8000
    #python manage.py runserver 0.0.0.0:8000
    #python manage.py runserver 127.0.0.1:8000 &
    nohup python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &
    if [ $? -ne 0 ]; then
        echo "Failed to start the server."
        return 1
    fi
    # Uncomment these if deploying via Docker
    # docker build -t notes-app .
    # docker run -d -p 8000:8000 notes-app:latest
    # docker-compose up -d
     	echo "Django development server is running on http://127.0.0.1:8000/"
}

echo "*********** DEPLOYMENT STARTED ************"

code_clone || exit 1
install_requirements || exit 1
required_restarts || exit 1
deploy || {
    echo "Deployment failed, mailing the Admin and Stakeholders"
    # sendmail admin@example.com
    exit 1
}

echo "*********** DEPLOYMENT DONE ************"

