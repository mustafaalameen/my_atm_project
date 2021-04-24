
database={} #to store users info with the 'acct_no' as the key for each user

import random

print('•••••••••••••••• Welcome to OUR BANK •••••••••••••••••')
def init( ):

	get_user=int(input('Do you have an Account with us? 1. Yes 2. No\n'))
	if get_user==1:
		login()
			
	elif get_user==2:
		register()
	else:
		print('Loading........')
		init()
	
def login():
	"""This is the login function both the registered and new users"""
	print ('*****°°°°°LOGIN°°°°°*****')
	acct_number=int(input('Enter your Account number:\n'))
	
	for acct_number_for_each_user, user_details in database.items():
		balance=user_details[5]
		if acct_number==acct_number_for_each_user:
				password=input('password\n:')
				if user_details[4] ==password:
					print('You logged in successfully!!!\n')
					
					bank_operations(balance)
				else:
					pass
		else:
			print('Invalid Account Number! Try again!!!')
			init()
def register():
	"""For new users only"""
	first_name=input('Enter Your first name:\n')
	last_name=input('Your last name:\n')
	e_mail=input('e-mail:\n')
	phone_no=input('Phone No.:\n')
	password=input('Password:\n')
	acct_balance=0
	print ('You\'ve successsfully created an account')
	acct_no=generate_acct_number()
	print (f"Your Account Number: {acct_no}")

	database[acct_no]= [ first_name, last_name, e_mail, phone_no, password,acct_balance]
	login()
	return database
	
	
def generate_acct_number():
	"""the account number generator"""
	acct_gen=random.randrange(1111111111,9999999999)
#	print (f"Your Account Number: {acct_gen}")
	return acct_gen
def deposit(balance):
	deposit_amount=int(input('How much do you want to deposit?\n'))
	balance+=deposit_amount
	print(f'You\'ve just deposited: NGN {balance}')
	return balance

def withdraw (balance):
	amount=int(input('How much do you want to withdraw:\n'))
	print(f'You just withdraw: NGN {amount}')
	balance-=amount
	
	return balance

def check_balance(balance):
	print(f'Your balance: NGN {balance}')
	
	
def bank_operations(balance):
	"""this is for the banking operations"""
	print('•••••••TRANSACTION•••••••\n')
	transaction=int(input("Select one of the following:\t 1. Deposit\t 2. Withdraw\t 3. Check Balance\t 4. Complaint\n"))
	
	if transaction==1:
		deposit(balance)
		continue_statements=input('Do you want to continue transaction? Press Y for Yes N for No\n')
		continue_statements= continue_statements.lower()
		if continue_statements=='y':
		
			bank_operations(balance)
		else:
				print('Thanks for banking with us!')
				exit()
		# continue_transaction(balance)
		
	elif transaction==2:
		withdraw(balance)
		continue_statements=input('Do you want to continue transaction? Press Y for Yes N for No\n')
		continue_statements= continue_statements.lower()
		if continue_statements=='y':
		
			bank_operations(balance)
		else:
				print('Thanks for banking with us!')
				exit()
		# continue_transaction(balance)
		
	elif transaction==3:
		check_balance(balance)
		continue_statements=input('Do you want to continue transaction? Press Y for Yes N for No\n')
		continue_statements= continue_statements.lower()
		if continue_statements=='y':
		
			bank_operations(balance)
		else:
				print('Thanks for banking with us!')
				exit()
		# continue_transaction(balance)

	elif transaction==4:
		complaint=input('What\'s your complain?\n')
		print('Thanks for informing us! Your complaint will be treated as urgent\n\n')
		continue_statements=input('Do you want to continue transaction? Press Y for Yes N for No\n')
		continue_statements= continue_statements.lower()
		if continue_statements=='y':
		
			bank_operations(balance)
		else:
				print('Thanks for banking with us!')
				exit()
		# continue_transaction(balance)
	
		return balance
	else:
			login()

			
init()
