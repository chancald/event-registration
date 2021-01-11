
class Contacts():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Leads():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


ContactsList = [
    Contacts('Alice Brown', None, '1231112223'),
    Contacts('Bob Crown', 'bob@crowns.com', None),
    Contacts('Carlos Drew', 'carl@drewess.com', '3453334445'),
    Contacts('Doug Emerty', None, '4564445556'),
    Contacts('Egan Fair', 'eg@fairness.com', '5675556667'),
]

LeadsList = [
    Leads(None, 'kevin@keith.com', None ),
    Leads('Lucy', 'lucy@liu.com', '3210001112'),
    Leads('Mary Middle', 'mary@middle.com', '3331112223'),
    Leads(None, None, '4442223334'),
    Leads(None, 'ole@olson.com', None),
]

json = {
  "registrant": 
     { 
        "name": "Tom Jones", 
        "email": "tom@jones.com",
        "phone": '3211234567',
     }
}

def store_registrant(json):
    ''' stores registrant to contacts or updates existant contact following filtering rules '''

    name = json['registrant']['name']
    email = json['registrant']['email']
    phone = json['registrant']['phone']

    for contact in ContactsList:
        if contact.email == email:
            if contact.name == None:
                contact.name = name
            if contact.email == None:
                contact.email = email
            if contact.name == None:
                contact.phone = phone
            return False
        elif contact.phone == phone:
            if contact.name == None:
                contact.name = name
            if contact.email == None:
                contact.email = email
            if contact.name == None:
                contact.phone = phone
            return False
    
    for lead in LeadsList:
        if lead.email == email:
            LeadsList.remove(lead)
            ContactsList.append(Contacts(name, email, phone))
            return False
        elif lead.phone == phone:
            LeadsList.remove(lead)
            ContactsList.append(Contacts(name, email, phone))
            return False
    
    # if there isn't a matching contact or lead, create contact
    ContactsList.append(Contacts(name, email, phone))
    return False
