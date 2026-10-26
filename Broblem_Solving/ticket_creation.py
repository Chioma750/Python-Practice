def get_ticket_details():

    while True:
        title = input("Enter Ticket title: ").strip()
        if title == "":
            print("Invalid title.")
            continue
            
        description = input("Enter Ticket description: ").strip()

        return title, description

ticket_title, ticket_description = get_ticket_details()

print("Ticket_title:", ticket_title)
print("Ticket_description:",ticket_description)