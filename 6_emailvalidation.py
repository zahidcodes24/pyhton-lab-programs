def is_valid_simple(email):
    
    if email.count("@") != 1:
        return False
    
    
    user_part, domain_part = email.split("@")
    
   
    if not user_part or not domain_part:
        return False
        
   
    if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith("."):
        return False
        
    return True


test_email = input("Enter email: ")
if is_valid_simple(test_email):
    print(" Valid format")
else:
    print(" Invalid format")