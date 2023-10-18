# UML Converter Web Application

This project aims to revolutionize software development by automating the generation of Unified Modeling Language (UML) diagrams from software requirements using Natural Language Processing (NLP) and machine learning. The web application is built on the Django framework and provides a user-friendly interface for creating UML Usecase diagrams based on input requirements.

## System Requirements

- Windows 10
- Python 3.11.5

## Internet Connection Requirement

This web application requires an active internet connection to function properly. It relies on external services and APIs for certain functionalities. Please ensure that your device is connected to the internet while using this application to access all its features.

**Note:** Some features may be limited or unavailable without an internet connection.

If you encounter any issues related to internet connectivity while using the application, please check your network connection and ensure that any firewall or security settings do not block the application's access to the internet.


## Installation

Follow these steps to install and run the UML Converter web application:

1. Clone this repository to your local machine.
2. Download the classifier model from [https://drive.google.com/file/d/1t8qn8R68N1v1YAsQ90ISub_6sPe29x28/view?usp=sharing](https://drive.google.com/file/d/1t8qn8R68N1v1YAsQ90ISub_6sPe29x28/view?usp=sharing) and paste it in `uml_converter\app`.

3. Open a command prompt and navigate to the project directory.

4. Create a virtual environment using the following commands:  
   `pip install virtualenv`  
   `python -m virtualenv umlcon_env`
5. Activate the virtual environment:  
   `cd umlcon_env/scripts`  
   `./activate`
6. Install the required dependencies:  
   `cd ../..`  
   `pip install -r requirements.txt`
7. Start the server:  
   `./run.bat`
8. Open your web browser and access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

- Choose the Entity Detector. Entity detectors are pipelines to extract uml diagram entities. The current framework has two Entity Detectors  (Entity Detector 1, and Entity Detector 2). Both use different methodologies to extract UML Usecase diagram entities. 
- Enter your software requirements in the text area.
- Click the 'Make UML' button to process the requirements.
- Review and edit entity extraction results if needed in Entity correction panel (This is a table showing detected entities(actor,usecase,sentence)).
- Download the generated UML diagram.

## Project Structure

- `app`: Contains Python modules for various application components. Some important modules are mentioned below.
- `app\templates`: Contains HTML templates for rendering web pages.
- `app\views.py`: Contains logic of UML Converter API and Entity Detector 1 and 2 (ref: Project Report).
- `app\generateUmlCode.py`: Contains logic of Plant UML Script Generator(ref: Project Report).
- `app\renderDiagram.py`: Contains logic of Plant UML Render Engine (ref: Project Report).
- `db.sqlite3`: SQLite database for storing extracted entities.
- `requirements.txt`: List of Python dependencies.
- `run.bat`: Script to start the Django development server.

## Credits

This project was developed as part of a dissertation by Ashwin Mariyathu Krishnakumar. It utilizes the DaVinci-003 and Flan T5 models for sentence reformatting and entity extraction. It also use [replicate](https://replicate.com/) to run Flan T5 model. Special thanks to Dr. Hai Wang, for guidance and support during the project.

   

   
