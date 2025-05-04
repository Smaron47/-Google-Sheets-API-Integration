# -Google-Sheets-API-Integration
# Google Sheets API Integration – Python Script Documentation

**Developed by:** Smaron Biswas  
**License:** MIT  
**Year:** 2024

---

## Overview

This project demonstrates how to use the Google Sheets API with Python to read and write data from a Google Spreadsheet. The script uses the Google API Client and a service account (with credentials provided in `credentials.json`) to authenticate and interact with Google Sheets and Drive. The code includes functions to extract hyperlinks from specified sheet ranges and update values in a given range.

**Key Outputs:**
- **Read Data:** Reads hyperlinks from a specified cell range of a Google Spreadsheet.
- **Write Data:** Updates a designated range in the same spreadsheet with data read from another range.

**SEO Keywords:**  
Google Sheets API, Python Google Sheets, Google API Client, Service Account, Spreadsheet Automation, Google Drive API, Python Automation, Data Extraction, Hyperlink Extraction, Google Sheets Integration

---

## Features

- **Automated Spreadsheet Access:**  
  Uses a service account to authenticate and access Google Sheets without manual intervention.
  
- **Hyperlink Extraction:**  
  Extracts hyperlinks embedded in cell values from a specified range.
  
- **Data Read/Write Operations:**  
  Reads a specified range from a Google Sheet and writes the extracted data to another range.
  
- **Modular Functions:**  
  Organized into functions for reading and writing data, making the code easy to maintain and extend.
  
- **Google Sheets and Drive Integration:**  
  Seamlessly integrates both the Sheets and Drive APIs for enhanced functionality.

---

## Project Structure

```plaintext
/your-project-directory/
│
├── credentials.json             # Service account credentials for Google API
├── README.md                    # This documentation file
└── google_sheets_script.py      # Python script file containing the code
Installation & Setup
Prerequisites:
Python 3.x must be installed on your system.

Google API Python Client: Install via pip:


pip install google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib

```
Service Account Credentials:

Create a service account in the Google Cloud Console.

Enable the Google Sheets and Drive APIs.

Download the credentials.json file and place it in your project directory.

Google Spreadsheet:

Create or use an existing Google Spreadsheet.

Share the spreadsheet with the service account email.

Running the Script:
Clone your repository and navigate to the project directory:

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Run the Python script:


python google_sheets_script.py
SEO Keywords: Installation, Python Setup, Google Sheets API, Service Account, Google API Client, Python Script Execution

Code Walkthrough & Analysis
Code Overview
The code (commented out in the provided snippet) is divided into the following key sections:

Imports and API Setup:

Imports necessary modules from googleapiclient and google.oauth2 for API interaction.

Sets API scopes for both Google Sheets and Drive.

Initializes the service account credentials and builds service objects for Sheets and Drive.

Constants Definition:

SPREADSHEET_ID: Identifies the target spreadsheet.

Range Constants:
READ_RANGE, WRITE_RANGE, and additional ranges such as BBB_link, TrustPlot_link, and Google_link specify where data is read from and written to.

Hyperlink Extraction Function:

extract_hyperlinks(sheet_data) iterates over the sheet data and extracts hyperlinks from each cell that contains the property 'hyperlink'.

Read Operation:

read_range(READ_RANGE) accesses a specific range in the spreadsheet, retrieving cell data (including hyperlinks) using the get method with specific field filters.

It prints the number of retrieved cells and rows, then returns the extracted hyperlinks in a list.

Write Operation:

write_range() calls the read function (using the BBB_link range in this example) and writes the values to the range specified in WRITE_RANGE using the update method with 'USER_ENTERED' input option.

Prints the number of cells updated.

Script Execution Flow:

The script calls read_range() (with TrustPlot_link in the provided snippet) and then executes write_range() to update the designated range.

SEO Keywords: Code Analysis, Google Sheets Read, Google Sheets Write, Hyperlink Extraction, Python Google API

Detailed Code Analysis
Initialization & API Setup
Description:
The script imports required modules and sets API scopes (https://www.googleapis.com/auth/spreadsheets and https://www.googleapis.com/auth/drive).

Implementation:
Uses service_account.Credentials.from_service_account_file to load the credentials and builds service objects with build().

SEO Keywords: API Authentication, Service Account, Google Sheets API, Google Drive API, Python Authentication

Hyperlink Extraction
Description:
The extract_hyperlinks() function iterates over the rows and cell values from the sheet data, collects those cells with a 'hyperlink' property, and returns a list of hyperlinks.

Implementation:
Nested loops check each cell in the row data and append found hyperlinks.

SEO Keywords: Hyperlink Extraction, Data Parsing, Spreadsheet Data Processing

Reading Data from the Spreadsheet
Description:
The read_range(READ_RANGE) function fetches a specified cell range using spreadsheets().get() with fields limiting the response to rows containing hyperlink and userEnteredValue.

Implementation:
Uses execute() to obtain the data, calls extract_hyperlinks() for processing, and prints logging details.

SEO Keywords: Data Retrieval, Spreadsheet Reading, Google Sheets Data, Python Data Extraction

Writing Data to the Spreadsheet
Description:
The write_range() function writes data (read from a range like BBB_link) to another defined range (WRITE_RANGE) using the update() method.

Implementation:
Prepares a body with values and updates the spreadsheet using 'USER_ENTERED' mode, printing the updated cell count.

SEO Keywords: Data Update, Spreadsheet Writing, Google Sheets API Update, CSV-like Data Export

Troubleshooting & Customization
Troubleshooting:
Authentication Errors:
Ensure your credentials.json file is valid and that the service account has access to the target spreadsheet.

API Scopes:
Confirm that both Sheets and Drive APIs are enabled in your Google Cloud project.

Incorrect Ranges:
Verify that the ranges (e.g., READ_RANGE, WRITE_RANGE) match the actual spreadsheet layout.

Customization:
Range Adjustments:
Modify the range constants to suit your spreadsheet structure.

Field Filtering:
Adjust the fields in the get method to extract additional cell properties if needed.

Logging:
Enhance logging or error handling for production-level monitoring.

SEO Keywords: Troubleshooting, Customization, API Errors, Data Range Adjustment, Python Debugging, Google Sheets Issues

Conclusion
This Python script provides a streamlined way to interact with Google Sheets using the Google API Client. It reads hyperlink data from a specified range and writes data back to the spreadsheet, demonstrating core functionalities needed for spreadsheet automation. The modular structure and clear separation of concerns make it easy to extend or modify for various applications.

SEO Keywords Recap:
Google Sheets API, Python Automation, Service Account, Hyperlink Extraction, Data Read/Write, API Client, Spreadsheet Integration, Google Drive API
