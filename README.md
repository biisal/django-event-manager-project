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
- **Register for Events**: As a logged-in user, register for events posted by others.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

**Note**: This project was started on 7th Jun and almost completed on 18th Jun.
