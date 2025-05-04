from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Spreadsheet id
SPREADSHEET_ID = "1-VoXk8xitqkQ7LMHnpwj6svmdt60qrh0z31irXhvPwQ"

# Sheet Name and Range to Read
READ_RANGE = "Sheet1!B2:E10"
WRITE_RANGE = "Write!B1:Y1"
BBB_link = "Sheet1!B1:B10"
TrustPlot_link = "Sheet1!C2:C10"
Google_link = "Sheet1!E2:E10"

# The boundary of script
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Configuration for python to sheet link
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json', scopes=SCOPES)
spreadsheet_service = build('sheets', 'v4', credentials=credentials)
drive_service = build('drive', 'v3', credentials=credentials)


def extract_hyperlinks(sheet_data):
    hyperlinks = []
    for row in sheet_data:
        for cell in row['values']:
            if 'hyperlink' in cell:
                hyperlinks.append(cell['hyperlink'])
    return hyperlinks


def read_range(READ_RANGE):
    range_name = READ_RANGE
    spreadsheet_id = SPREADSHEET_ID
    result = spreadsheet_service.spreadsheets().get(
        spreadsheetId=spreadsheet_id, ranges=range_name, fields="sheets(data(rowData(values(hyperlink,userEnteredValue))))"
    ).execute()
    sheet_data = result['sheets'][0]['data'][0]['rowData']
    hyperlinks = extract_hyperlinks(sheet_data)
    print('--- Reading from Google Sheets------')
    print('------------------------------------')
    print('\t{0} cells retrieved.'.format(len(hyperlinks)))
    print('------------------------------------')
    print('{0} rows retrieved.'.format(hyperlinks))
    return [hyperlinks]


def write_range():
    spreadsheet_id = SPREADSHEET_ID
    range_name = WRITE_RANGE
    values = read_range(BBB_link)
    print(values, len(values[0]))
    value_input_option = 'USER_ENTERED'
    body = {
        'values': values
    }
    print(body)
    result = spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('--- Writing from Google Sheets------')
    print('------------------------------------')
    print('\t{0} cells updated.'.format(result.get('updatedCells')))
    print('------------------------------------')


read_range(TrustPlot_link)
# read_range(Google_link)
# read_range(BBB_link)

write_range()
