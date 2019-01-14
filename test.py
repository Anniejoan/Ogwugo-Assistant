import  requests
import json
def test():
    print("============loading======")
    url = "https://ogwugo.net/api/v2/machine/resources/product/search/by/name"

    querystring = {"q": "rice"}

    payload = ""
    headers = {
        'Authorization': "Basic b2d3dWdvX3NlcnZpY2U6ZzU3ODI3NmRzZmZkYmE"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.text)


def run( ):
    # Sample Basic Auth Url with login values as username and password
    user = "ogwugo_service"
    passwd = "g578276dsffdba"
    user_name = "Tessy"

    # Make a request to the endpoint using the correct auth values
    auth_values = (user, passwd)
    url = "https://ogwugo.net/api/v2/machine/resources/users/buyers?user_name="+user_name
    response = requests.get(url, auth=auth_values)

    #user_name = tracker.get_slot('Username')

    user_dict = json.loads(response.content.decode())
    User = user_dict['data']
    Telephone = User["phone"]
    location = User["addresses"][0]['address']

    print("Please confirm that ", Telephone, " is your phone number and ", location, " is your delivery address." )


def action( ):
    user = "ogwugo_service"
    passwd = "g578276dsffdba"
    product_name = 'pancakes', 'bread'
    url = "https://ogwugo.net/api/v2/machine/resources/product/search/by/name?q={product_name}"

    # Make a request to the endpoint using the correct auth values
    auth_values = (user, passwd)
    response = requests.get(url, auth=auth_values)

    # Convert JSON to dict and print

    product_dict = json.loads(response.content.decode())
    Products = product_dict['data']
    name_value = Products[0]['name']
    stock_status = Products[0]["in_stock"]
    store_value = Products[0]["store_name"]
    prodct_type = Products[0]["product_type"]

    if stock_status == 1:
        # reply = """" {} sold by {} is currently available for delivery.""".format(name_value, store_value)
        print("""" {} sold by {} is currently available for delivery.""".format(name_value, store_value))
    else:
        # reply =  "" {name_value} sold by {store_value} is currently unavailable for delivery."
        print(" {name_value} sold by {store_value} is currently available for delivery.")





action()