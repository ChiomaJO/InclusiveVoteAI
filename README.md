InclusiveVote AI
An AI-Powered Accessible Electoral Information Assistant for Inclusive Civic Participation in Nigeria

About the Project
InclusiveVote AI is an early-stage functional prototype designed to explore how technology can make verified electoral information easier to find, access and understand, particularly for persons with disabilities.

The project focuses on improving access to electoral information through a simple question-and-answer interface.

The Problem
Some voters with disabilities may experience difficulties accessing, finding and understanding official electoral information in formats that meet their different accessibility and communication needs.

InclusiveVote AI is being developed to explore how an accessible digital information assistant could help address some of these barriers.

This problem hypothesis is still being investigated and requires further validation with intended users.

Current Prototype Features
The current version can:

Accept electoral questions through a web form.
Search a small collection of stored electoral information.
Match some questions with different wording.
Display answers alongside their source information and links.
Provide a fallback response when no sufficiently strong match is found.
Technology Stack
Python
Flask
HTML
CSS
JSON
Git and GitHub
Current Development Status
This is an early functional prototype. It currently uses basic keyword matching to retrieve information from a small, manually prepared knowledge collection.

It does not yet use a trained AI model or a large language model.

Accessibility Direction
The project aims to support more inclusive access through:

Clear and readable content.
Simple navigation.
Keyboard accessibility.
Screen-reader-friendly page structure.
Further exploration of text-to-speech and other assistive features.
Accessibility testing with intended users is still required. Full WCAG compliance has not yet been established.

Current Limitations
The information collection is small and requires further expansion and verification.
Question matching is limited and may return incorrect or incomplete matches.
The prototype does not currently connect to INEC systems.
Screen-reader and assistive technology testing is still pending.
It is not a substitute for official electoral guidance.
Running the Project Locally
Clone or download this repository.
Create and activate a Python virtual environment.
Install Flask.
Run the application.
Example commands for Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install flask
python app.py
Open http://127.0.0.1:5000 in your browser.

Project Vision
The long-term goal is to develop an accessible, reliable and inclusive electoral information assistant that helps people with different disabilities access and understand verified civic and electoral information.

Project: InclusiveVote AI
Developer: Chioma Joan Okeke
Focus: Inclusive and accessible civic technology
Status: Early functional prototype – under development