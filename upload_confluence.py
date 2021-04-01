from atlassian import Confluence

def upload_to_confluence(html_body):
    conf_site = 'https://confluence.*****.com'
    conf_user = 'shayan.saha'
    conf_pass = '*******'

    page_title = 'TEST' 
    page_space = 'TST'
    page_id = "123456"

    connection = Confluence(url=conf_site, username=conf_user, password=conf_pass)

    page_id = connection.get_page_id(space_key, page_title)

    page = connection.get_page_by_id(page_id=page_id, expand='body.storage')
    page_content = page['body']['storage']['value']
    page_content =  html_body

    connection.update_page(page_id, page_title, page_content)
    print("Successfully updated")