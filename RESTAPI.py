import requests
import json

#Headers 
payload = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE2OTk4NzU3NDksIm5iZiI6MTY5OTg3NTc0OSwiZXhwIjoxNjk5ODgwOTk4LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBOG9BQ0x6WnRvc2FJd2FUcGtWb2RtQmtHVGJ2R1BGRXgwNklpN1pYT0VES2xtZkhpK09NMU5hUjZaNXV2Wmo4d2cvNkdySjg3NjV3RW9td0JieXo5empJdEdUT2dEYW1uVEVyMjRYTUtjNlk9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTGVrYSIsImdpdmVuX25hbWUiOiJXaWxsaWFtIiwiZ3JvdXBzIjpbIjgxMDhjNTAzLWQ2NTYtNDJjZi04ZWU0LTg5NDRhZWYwZmFkZSIsIjk3YWY4MTJkLTk2ZTktNGYwMS04YTExLTc1ODAzMzc2MjE3YSIsIjg3ZjYwMDNkLTk0NzAtNDM4Zi1iZmVmLTgxM2IzN2ZjMmI2OCIsIjNlODQ4MDk4LWI0YTEtNDE3ZC1hMWJhLWM5Y2YzZmNlOWY1MSIsIjgzOGEyODlhLTg0YTQtNGNhOC1hZWVjLWIzMWVjMWQ3MWQ0YSIsIjRkYzAzYjlmLTFiNmMtNDQxNS1hYzA1LTgyNDI3MTNjNzUyMCIsIjVhZDdkNmI0LWFkYWYtNGI5ZC05NTdmLTBmM2I2MTRiZWU2MCIsIjhhYzE1NGRkLWQ0NWYtNGM0Ni05NGU1LWJiNzhmZWZhM2FlZiIsIjhjODE4NmVhLTQyYTQtNDRhZi04YTc4LWFlOTE0MDExZTZiNCIsImQyYTZhOGVmLTRkMjYtNGQ5NS1iZDExLWFhMWVjNjE5ZjgxOCJdLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxNzYuNjEuNC4xNDciLCJuYW1lIjoiQzIxNDIzMjQ0IFdpbGxpYW0gTGVrYSIsIm9pZCI6IjQ3YzM4ZTZhLTk1NTctNGZkMy1hYjNlLTEwMWJiY2FiNWYyOCIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQ0MzU3IiwicHVpZCI6IjEwMDMyMDAxNkJDQkFCRUIiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QUFJLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IllSUDlJZndfSjYtd1JNejVYOXZVSzA1T3lqcFNHSDJPMnZCS1dPU2JyVEkiLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTQyMzI0NEBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxNDIzMjQ0QG15dHVkdWJsaW4uaWUiLCJ1dGkiOiJ3Sy11bDJvLXBrS01FQUFHcHR4Q0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.sktD24UiaZZvSEv_SO6fRnVz6lT-dXots1wSAAHhnE2ive8cFXtwnf9Dry1QkuV2p6U9Lmbx9AGUKg63j6VWcRQkhMqbA5keFEVHFx3Qnwrc_LlN9x4lnFWtY59O97w2GGKjZs5b7doIP2IXqzVQwGAMHj0d9xw0cnNvvXfxwunScbUfP4UucMxknR89O8HaR7vfyH460u_Zqi5b09wK7qGAXQweYZkh6MheIK9J5lwdcEtn_3yERcMx9JMTaJjVHmhmHUCtAq0czYTn1WcbdKqC7pAeHsBGFaDQ9R6mkS_2k3p1FN9oWwyYdfEspufavFV_VpTm8q4iX-oVKjoKCw',
    'Content-type': 'application/json'
}

#Resource Groups 
responseResourceGroups = requests.get('https://management.azure.com/subscriptions/6c01e812-bb10-4007-afea-43097d9ed75a/resourcegroups/lab4?api-version=2021-04-01', headers=payload)
print("\n---Resource Groups---\n",responseResourceGroups.json(),"\n---Resource Groups---\n")


#Virtual Networks 
responseVirtualNetworks =  requests.get('https://management.azure.com/subscriptions/6c01e812-bb10-4007-afea-43097d9ed75a/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/net4?api-version=2023-05-01', headers=payload)
print("\n---Virtual Network---\n",responseVirtualNetworks.json(),"\n---Virtual Network---\n")


#Sub Net 
responseSubNet = requests.get('https://management.azure.com/subscriptions/6c01e812-bb10-4007-afea-43097d9ed75a/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/net4/subnets/snet4?api-version=2023-05-01', headers=payload)
print("\n---Sub Net---\n",responseResourceGroups.json(),"\n---Sub Net---\n")


#Public IP Address
responsePublicIPAddress = requests.get('https://management.azure.com/subscriptions/6c01e812-bb10-4007-afea-43097d9ed75a/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/nic4?api-version=2023-05-01', headers=payload)
print("\n---Public IP Address---\n",responseResourceGroups.json(),"\n---Public IP Address---\n")


##Network Interface
responseNetworkInterface = requests.get('https://management.azure.com/subscriptions/6c01e812-bb10-4007-afea-43097d9ed75a/resourceGroups/lab4/providers/Microsoft.Compute/virtualMachines/vm4?api-version=2023-07-01', headers=payload)
print("\n---Network Interface---\n",responseResourceGroups.json(),"\n---Network Interface---\n")


##Virtual Machine
responseVirtualMachine = requests.get('https://management.azure.com/subscriptions/6c01e812-bb10-4007-afea-43097d9ed75a/resourcegroups/lab4?api-version=2021-04-01', headers=payload)
print("\n---Virtual Machine---\n",responseResourceGroups.json(),"\n---Virtual Machine---\n")


