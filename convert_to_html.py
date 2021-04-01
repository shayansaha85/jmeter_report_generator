import pandas as pd
import os

def convert_to_html(csv_filename):
    df = pd.read_csv(f"./aggregate_report/{csv_filename}")
    df.to_html("./html_report/raw_html.html")

    file = open("./html_report/raw_html.html","r")
    table = file.read()
    file.close()
    
    css = '''<style>
    body {
        font-family : Arial
    }
    table {
    border-collapse: collapse;
    width: 100%;
    }

    th, td {
    text-align: left;
    padding: 8px;
    }

    tr:nth-child(even){background-color: #f2f2f2}

    th {
    background-color: #4285F4;
    color: white;
    }
    </style>
    '''
    html_meta = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        {css}
    </head>
    <body>
        {table}
    </body>
    </html>'''

    html_file = open(f"./html_report/{csv_filename.split('.')[0]}.html", "w")
    html_file.write(html_meta)
    html_file.close()
    os.remove("./html_report/raw_html.html")
