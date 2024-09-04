# Django Event Management System

This is a simple event management system where users can create, register, and manage events. The application is built with Django and includes features such as user authentication, event registration, and image uploads.

## Features

- **User Authentication**:

  - Registered users can log in using Django's built-in authentication.
  - Non-logged-in users can view all events.
  - Logged-in users can view, register, and modify their own events.

- **Event Management**:

  - Users can create, edit, and delete their events.
  - Other logged-in users can register for these events.

- **Image Uploads**:

  - Users can upload images when creating or editing events.

- **Rich Text Editing**:

  - Integrated with Django Quill for markdown inputs, allowing users to format event descriptions easily.

- **Responsive Design**:
  - Styled using Tailwind UI for a modern and responsive user interface.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/event-management.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd event-management
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

- **Create an Account**: Register a new user or log in with existing credentials.
- **View Events**: Browse all available events, even without logging in.
- **Manage Events**: Create new events, edit or delete your existing ones.
- **Register for Events**: As a logged-in user, register for events posted by others.z



# Option 2: For VM and Vagrant Users

#### Prerequisites

- **Python 3.6+**
- **Vagrant**
- **VirtualBox**
- **Git**

#### Project Setup

1. **Clone the Repository**:  
   The repository is cloned as part of the deployment script. No additional action is needed.

2. **Configure Port Forwarding**:  
   Ensure your `Vagrantfile` includes the following configuration to forward port 8000 from the VM to the host:
   
   ```ruby
   config.vm.network "forwarded_port", guest: 8000, host: 8000
   ```

3. **Start the Vagrant VM**:  
   In your project directory, start the Vagrant VM:
   
   ```bash
   vagrant up
   ```

4. **SSH into the Vagrant VM**:  
   Once the VM is up, SSH into it using:
   
   ```bash
   vagrant ssh
   ```

5. **Navigate to the Project Directory**:  
   Change to the directory where the project files are located:
   
   ```bash
   cd /vagrant/event-management
   ```

6. **Set Up the Virtual Environment**:  
   Set up and activate the virtual environment:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

7. **Install Project Dependencies**:  
   Install the dependencies listed in `requirements.txt`:
   
   ```bash
   pip install -r requirements.txt
   ```

8. **Apply Migrations**:  
   Apply the necessary migrations to set up the database:
   
   ```bash
   python manage.py migrate
   ```

9. **Run the Django Development Server**:  
   Start the Django development server on all available network interfaces:
   
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

10. **Access the Application**:  
    Open your browser and go to `http://localhost:8000` to access the application.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Notes

This project was started on 7th Jun and almost completed on 18th Jun.

---
