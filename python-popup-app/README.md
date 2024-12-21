# Python Popup Application

This project is a Python application that provides a graphical user interface (GUI) for selecting and running Python files. It ensures that any previously running Python file is stopped before a new one is executed.

## Project Structure

```
python-popup-app
├── src
│   ├── application.py   # Main entry point of the application
│   ├── popup.py         # Defines the Popup class for file selection
│   └── utils.py         # Utility functions for running Python files
├── requirements.txt      # Lists project dependencies
└── README.md             # Project documentation
```

## Requirements

To run this application, you need to install the required dependencies listed in `requirements.txt`. You can do this using pip:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory.
2. Run the main application file:

```
python src/application.py
```

3. A popup will appear allowing you to select a Python file to run. If a file is already running, it will be stopped before the new file is executed.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.