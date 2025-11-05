'''
Imagine you’re building a backend feature for an ATM. Customers can request multiple withdrawals during one session. Your task is to simulate how the system should handle each request based on the account balance.
Tasks:
Use a while loop to iterate through the list named withdrawals.
For every withdrawal:
✅ If the current balance is enough:
Subtract the amount.
Append a success message: "Withdrawn: {amount}"
❌ If not enough:
Append a message: "Insufficient funds for requested amount: {amount}"
After all withdrawals:
Append the final balance as: "Remaining Balance: balance"
Return a list containing all the messages.
'''

def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> None:
    for amount in withdrawals:
        if balance >= amount:
            balance -= amount
            print(f"Withdrawal Successful,amount deduted = {amount}")
        else:
            print("Insufficient Funds")
            break
    print(f"Remaining balance : {balance}")

simulate_atm_withdrawals(100,[2,3,4,5,6,7,8,8,8,8,8,8])

