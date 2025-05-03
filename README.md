
Project: Python Gmail Service
markdown

# Python Gmail Service

A Python-based service that interacts with Gmail, allowing users to perform various operations, including generating a list of unique senders, deleting emails based on queries, and fetching email statistics. The service is designed for managing Gmail accounts efficiently through the terminal.

## Features

- **Generate Unique Senders**: Creates a JSON file containing a list of unique senders from your Gmail account.
- **Delete Emails Based on Query**: Delete emails from your Gmail account based on specific search queries.
- **Fetch Total Mails Based on Query**: Get the total number of emails matching a specific query.
- **Delete All Emails**: Delete all emails from your Gmail account.
- **Show First 10 Mails**: Display the first 10 emails in your inbox.
- **Terminal-based Interface**: Interact with the service through the terminal using simple commands.

## Prerequisites

Before running this project, make sure you have the following installed:

- **Python** (>= 3.6)
- **Google API Client**: Install the required Google API client library to interact with Gmail API.
- **OAuth 2.0** credentials to authenticate your Gmail account.

### Installing Dependencies

1. **Install the required libraries** using `pip`:

    ```bash
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```

2. **Get OAuth credentials**:
   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project and enable the **Gmail API**.
   - Download the OAuth credentials as `cridentials1.json` and place it in your project directory.

## Getting Started

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Akshay3237/python-gmail-service.git
cd python-gmail-service
2. Authenticate with Gmail
When you run the program, it will prompt you to authenticate using your Google account. The credentials will be saved locally for future access.

Note: Make sure you have a credentials.json file (from Google Cloud) in the project directory for the Gmail authentication.

3. Run the Service
Execute the Python script to interact with Gmail and perform actions:


python -m gmail_handler
The service will prompt you to enter commands as follows:

Enter 's': Generate the unique_senders.json file containing unique senders.

Enter 'd': Delete emails based on a query.

Enter 'l': Show the total number of emails matching a specific query.

Enter 'a': Delete all emails from your account.

Enter 'p': Show the first 10 emails in your inbox.

Example Commands:

Enter base on follow:
- Enter 's' for generate unique_senders.json
- Enter 'd' for delete mails based on query
- Enter 'l' for total mails based on query
- Enter 'a' for delete all mails
- Enter 'p' for show first 10 mails
The system will ask for confirmation and proceed based on your input.

Code Overview
input_handler.py: Handles user input and command processing.

gmail_service.py: Contains logic to interact with the Gmail API for email operations.

main.py: The main entry point to run the service, where the user interacts with the terminal interface.

License
This project is licensed under the GNU General Public License Version 3 - see the LICENSE file for details.

Contact
Name: Akshay

GitHub: https://github.com/Akshay3237

Email: akshaygohel364@gmail.com

Contributing
Feel free to fork the repository, contribute via pull requests, or report any issues. Contributions are always welcome to improve the service!
