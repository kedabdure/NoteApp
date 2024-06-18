# NoteApp

NoteApp is a simple and efficient web application for managing notes. It provides a user-friendly interface for creating, viewing, updating, and deleting notes. This README file provides a comprehensive guide on how to set up, use, and contribute to NoteApp.

## Features

- **User Authentication**: Secure login and sign-up functionality.
- **Create Notes**: Users can create new notes with a title and content.
- **View Notes**: Display a list of all notes with the ability to view individual note details.
- **Edit Notes**: Modify existing notes.
- **Delete Notes**: Remove notes that are no longer needed.
- **Responsive Design**: Accessible on both desktop and mobile devices.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (for simplicity)
- **Version Control**: Git

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask
- SQLite
- Git

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/kedabdure/NoteApp.git
    cd NoteApp
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application**:
    ```sh
    flask run
    ```

6. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. **Sign Up**:
    - Navigate to the sign-up page.
    - Fill in your name, email, and password.
    - Click the "Submit" button to create an account.

2. **Log In**:
    - Navigate to the login page.
    - Enter your email and password.
    - Click the "Login" button to access your account.

3. **Create a Note**:
    - Once logged in, click on the "Create Note" button.
    - Enter the title and content of the note.
    - Click "Save" to add the note to your list.

4. **View Notes**:
    - The homepage displays a list of all your notes.
    - Click on any note to view its details.

5. **Edit a Note**:
    - While viewing a note, click the "Edit" button.
    - Modify the title or content as needed.
    - Click "Save" to update the note.

6. **Delete a Note**:
    - While viewing a note, click the "Delete" button.
    - Confirm the deletion in the prompt.

## Project Structure


## Contributing

Contributions are welcome! If you would like to contribute, please follow these steps:

1. **Fork the repository**:
    ```sh
    git fork https://github.com/yourusername/noteapp.git
    ```

2. **Create a feature branch**:
    ```sh
    git checkout -b feature/your-feature-name
    ```

3. **Commit your changes**:
    ```sh
    git commit -m "Add your feature"
    ```

4. **Push to the branch**:
    ```sh
    git push origin feature/your-feature-name
    ```

5. **Open a pull request** on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- Flask documentation: [Flask Docs](https://flask.palletsprojects.com/)
- Bootstrap documentation: [Bootstrap Docs](https://getbootstrap.com/)
- All the open-source contributors and libraries.

## Contact

If you have any questions, suggestions, or issues, feel free to open an issue on GitHub or contact the repository owner.

---

Thank you for using NoteApp! Happy note-taking!
