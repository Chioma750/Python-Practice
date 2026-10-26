def get_ticket_details():

    title = input("Enter Ticket title: ").strip()
    description = input("Enter Ticket description: ").strip()

    return title, description

ticket_title, ticket_description = get_ticket_details()

print("Ticket_title:", ticket_title)
print("Ticket_description:",ticket_description)