# login_guardian.py - Simple Login Guard

def check_login(username, password, location):
    # Rule 1: Correct password check
    if password != "1234":
        return "DENY - Wrong Password"
    
    # Rule 2: Unknown location check
    if location != "Patna":
        return "FLAG - Unknown Location, needs OTP"
    
    return "ALLOW - Login Successful"

# Test 1 - Normal user
print("Test 1:", check_login("student", "1234", "Patna"))
# Test 2 - Hacker from different city
print("Test 2:", check_login("student", "1234", "Delhi"))
# Test 3 - Wrong password
print("Test 3:", check_login("student", "wrong", "Patna"))