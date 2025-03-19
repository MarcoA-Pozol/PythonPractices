# Dependencies


# Common root URL components
host = 'localhost'
port = '8000'
root_path = '/techstore'
URL_common_root = f'{host}:{port}{root_path}' 

# URLs
URL_revenues = f'{URL_common_root}/products'
URL_employees = f'{URL_common_root}/employees'
URL_customers = f'{URL_common_root}/customers'

URLS_List = (URL_revenues, URL_employees, URL_customers)
