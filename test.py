import ecommerce #(option 1, import package)
#from ecommerce import shipping #(option 2 import module)
#from ecommerce.shipping import calc_shipping #(option 2 import function)

ecommerce.calc_shipping() # (option 1, only works if you put "from .shipping import calc_shipping" in the __init__ of the package)
#shipping.calc_shipping() #(option 2)
#calc_shipping() #(option 3)