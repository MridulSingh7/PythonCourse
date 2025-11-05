chai_type = "ginger"

def update_order():
    # Local variable 'chai_type' within update_order
    chai_type = "Elaichi"
    
    def kitchen():
        # 'nonlocal' refers to the nearest enclosing scope variable (update_order's chai_type)
        nonlocal chai_type
        chai_type = "Kesar"  # updates the 'chai_type' in update_order, not global
        
    kitchen()
    print("After kitchen update", chai_type)  # prints "Kesar" because nonlocal updated it

update_order()


chai_type = "Plain"  # global variable

def front_desk():
    def kitchen():
        # 'global' keyword refers to the top-level variable 'chai_type'
        global chai_type
        chai_type = "Irnai"  # updates the global chai_type
        
    kitchen()

front_desk()
print("Final global chai: ", chai_type)  # prints "Irnai" because global variable was updated
