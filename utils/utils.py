import inspect

URL         =   "https://opensource-demo.orangehrmlive.com/"
USERNAME    =   "Admin"
PASSWORD    =   "admin123"

# functions
def whoami():
    return inspect.stack()[1][3]
