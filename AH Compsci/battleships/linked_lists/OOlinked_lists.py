class Ticket:
    def __init__(self, user, issue):
        self.user = user
        self.issue = issue
        self.next = None
    

class HelpDesk:
    def __init__(self):
        self.head = None
    
    def log_ticket(self, user, issue):
        new_ticket = Ticket(user, issue)
        new_ticket.next = self.head
        self.head = new_ticket
    
    def show_tickets(self):
        current = self.head
        while current is not None:
            print(f"{current.user} reported: {current.issue}")
            current = current.next
    
    def resolve_ticket(self):
        self.head = self.head.next
        



help_desk = HelpDesk()
help_desk.log_ticket("user1", "Robbery")
help_desk.log_ticket("user2", "Speeding")
help_desk.log_ticket("user3" ,"Theft")
help_desk.resolve_ticket()
help_desk.resolve_ticket()
help_desk.resolve_ticket()

help_desk.show_tickets()