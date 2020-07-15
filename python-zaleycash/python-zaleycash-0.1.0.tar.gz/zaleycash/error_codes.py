"""
1 - Invalid access token
2 - Wrong secret key
3 - Client does not exist
4 - Wrong Authorization header
5 - Access is denied for user
10 - Invalid request
20 - Registration errors
21 - User does not exist
22 - User with account does not exist
23 - Account <account_id> type is not <account_type>
24 - Account <account_name> inactive. Operations are protected
25 - Wrong account_id
26 - User inactive. Operations are protected
50 - Not enough money or your amount is less then set limit
51 - Not enough money
52 - Switch on common financial account for operation processing in account <account_name>
53 - Transaction processing error
54 - Financial operations are protected for account <account_name>
55 - Wrong operation_id
56 - Invalid transaction description in request
57 - Can not approve deposit transaction
58 - Duplicate operation_id
59 - Operation already approved
60 - Operation already declined
71 - Account creation error
72 - Email already exist
73 - {partner name} returned an error
80 - Wrong currency
81 - Agent account is disabled
"""

INVALID_ACCESS_TOKEN = 1
WRONG_SECRET_KEY = 2
CLIENT_DOES_NOT_EXIST = 3
WRONG_AUTH_HEADER = 4
ACCESS_DENIED = 5
INVALID_REQUEST = 10
REGISTRATION_ERRORS = 20
USER_DOES_NOT_EXIST = 21
USER_WITH_ACCOUNT_DOES_NOT_EXIST = 22
# I'm too lazy to type them all :)
DUPLICATED_OPERATION_ID = 58
OPERATION_ALREADY_APPROVED = 59
