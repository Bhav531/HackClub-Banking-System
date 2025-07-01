print ('Welcome to HACKCLUB Banking online')
name= input('Enter your name: ')
print ('Your current balance is 0.')
print ('Enter 1 to deposit money')
print ('Enter 2 to withdraw money')
print ('Enter 3 to view balance')
print ('Enter 4 to exit')
question = 'Yes'
balance = 0
while question == 'Yes' or question =='Y':
  choice= input('Enter your choice: ')
  if choice == '1':
    def deposit (money):
      global balance
      if money!=0:
        balance = balance + int(money)
        return 'Amount Deposited successfully.'
      else:
        return 'Amount not valid to be deposited.'
    deposit1= input('Enter the amount you would like to deposit: ')
    m = deposit(deposit1)
    print (m)
    question= input('Would you like to continue: ')

  elif choice == '2':
      def withdraw (cash):
        global balance
        if cash<deposit1:
          balance= balance - int(cash)
          return 'Amount withdrawn successfully.'
        else:
          return 'Transaction can not be possible, you do not have sufficient balance in your account.'
      withdraw1= input('Enter the amount you would like to withdraw: ')
      c= withdraw(withdraw1)
      print(c)
      question= input('Would you like to continue: ')


    
  elif choice == '3':
        print ('The current balance of your account is',balance)
        question= input('Woud you like to continue: ')

  elif choice == '4':
        print ('Thank you for using HACKCLUB Banking online')
        break


else:
  print ('We do not have that command.')