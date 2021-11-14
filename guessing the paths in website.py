import requests
from http import HTTPStatus
check_path_website = ['/admin.php','/adminLogin/','/logout', '/administrator/', '/login/']
check_url = str(input("URL:"))
for i in check_path_website:
    double_check_url = check_url+i
    Admin = requests.get(double_check_url)
    if double_check_url == Admin.url:
        print(double_check_url,Admin.status_code)
    if double_check_url != Admin.url :
        print(double_check_url,"200") 
        pass
