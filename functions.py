import requests

def get_tickets(url, user, token):
    while url is not None:
        response = requests.get(url, auth=(user, token))
        data = response.json()
        tickets = data['tickets']
        zendesk_new_tickets = 0

        for ticket in tickets:
            if ticket['status'] == 'new':
                zendesk_new_tickets = zendesk_new_tickets + 1
        url = data['next_page']

    return zendesk_new_tickets
