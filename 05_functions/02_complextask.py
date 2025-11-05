#you are creating a monthly report for a cafe's sales,instead of putting all logic in one place break it down
#function generate_report() that calls fetch_sales(), filter_valid_orders() and sumarrised_data()

def fetch_sales():
    print("fetching the data")

def filter_valid_orders():
    print("filtering the valid orders...")

def sumarrised_data():
    print("sumarrising the final data....")

def generate_report():
    fetch_sales()#calling a function inside a function 
    filter_valid_orders()
    sumarrised_data()


generate_report()