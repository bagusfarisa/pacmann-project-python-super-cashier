class Transaction:
    '''
    Attributes
    ----------
    transaction = {}
        Dictionary containing the items ordered for the transaction.
    
    Methods
    --------
    show_order_table(order_items): 
        Show the list of items ordered as a table.
        
    add_item(item_name, item_qty, item_price):
        Add an item to the transaction.

    update_item_name(item_name, new_item_name): 
        Update the name of an item.

    update_item_qty(item_name, new_item_qty): 
        Update the quantity of an item.
        
    update_item_price(item_name, new_item_price): 
        Update the price of an item.
    
    delete_item(item_name): 
        Delete an item by its name.
        
    reset_transaction(): 
        Delete all the items in the transaction.

    check_order(): 
        Check whether the values inputted to the transaction are correct or not.
    
    total_price(): 
        Check the total price of all items ordered for the transaction.
    
    is_discounted(total_price): 
        Check whether a transaction will be dicounted or not.
    '''
    
    transaction = {}
    
    # Method to iniate the class object containing an "order" dictionary
    def __init__(self):
        self.order_items = self.transaction
        
    
    # Method to display the shopping items and price as a table
    def show_order_table(self):
        '''
        Show the list of the items ordered for the transaction as a table.
        '''
        
        self.column_spacing = "|{:<4}|{:<12}|{:>12}|{:>12}|{:>12}|"
    
        # Print the table header
        print(self.column_spacing.format('No','Nama Item','Jumlah Item','Harga/Item','Harga Total'))
        
        n = 1
        
        for key, value in self.order_items.items():
            no = n 
            item_name = key
            item_qty = value[0]
            item_price = value[1]
            amount = item_qty * item_price
            # Print the defined variables
            print(self.column_spacing.format(no, item_name, item_qty, item_price, amount))
            n += 1
        
    
    # Method to add a new key and values to the transaction Dictionary
    def add_item(self, item_name, item_qty, item_price):
        '''
        Add an item to the transaction.
        
        Parameters
        ----------
            item_name : str
                name of the item
                
            item_qty : int
                quantity of the item
                
            item_price : int
                unit price of the item
        '''
        self.item_name = str(item_name)
        try:
            self.item_qty = int(item_qty)
            self.item_price = int(item_price)
            self.order_items[self.item_name] = [self.item_qty, self.item_price]
        except:
            print("Tidak dapat menambahkan item. \nJumlah dan harga item harus berupa angka.\n")
        
        
    # Method to change the key name of an order item
    def update_item_name(self, item_name, new_item_name):
        '''
        Update the name of an item.
        
        Parameters
        ----------
            item_name : str
                name of the item to be replaced
                
            new_item_name : str
                new name of the item
        '''
        self.item_name = str(item_name)
        self.new_item_name = str(new_item_name)
        
        try:
            self.order_items[self.new_item_name] = self.order_items[self.item_name] # Duplicate the values of the old key to the new one
            del self.order_items[self.item_name] # Delete the old key
        except:
            print("Gagal mengubah nama item. \nNama item tidak ditemukan\n")
        
    
    # Method to change the quantity of an order item
    def update_item_qty(self, item_name, new_item_qty):
        '''
        Update the quantity of an item.
        
        Parameters
        ----------
            item_name : str
                name of the item which the quantity to be changed
                
            new_item_qty : int
                the new quantity assigned to the item.
        '''
        self.item_name = str(item_name)
        
        try:
            self.new_item_qty = int(new_item_qty)
            try:
                self.order_items[self.item_name][0] = self.new_item_qty
                
            except:
                print("Gagal mengubah jumlah item. \nNama item tidak ditemukan.\n")
        except:
            print("Jumlah item harus berupa angka.\n")
        
    
    # Method to change the price of an order item
    def update_item_price(self, item_name, new_item_price):
        '''
        Update the price of an order item.
        
        Parameters
        ----------
            item_name : str
                name of the item which the quantity to be changed
                
            new_item_qty : int
                the new quantity assigned to the item.
        '''
        self.item_name = str(item_name)
        
        try:
            self.new_item_price = int(new_item_price)
            try:
                self.order_items[self.item_name][1] = self.new_item_price
            except:
                print("Gagal mengubah harga. \nNama item tidak ditemukan.\n")
        except:
            print("Harga item harus berupa angka.\n")
        
        
    
    # Method to delete an order item (its key and values)
    def delete_item(self, item_name):
        '''
        Delete an item by its name.
        
        Parameters
        ----------
            item_name : str
                Item name you want to delete.
        '''
        self.item_name = str(item_name)
        try:
            del self.order_items[self.item_name]
        except:
            print("Gagal menghapus item. \nNama item tidak ditemukan.\n")
        
        
    
    # Method to delete all order items
    def reset_transaction(self):
        '''
        Delete all the items in the transaction.
        '''
        transaction = {}
        self.order_items = transaction
        print("Semua item berhasil dihapus.\n")
    
    
    def check_order(self):
        '''
        Check whether the values inputted to the order items are correct or not.
        '''
        for key, value in self.order_items.items():
            item_name = key
            item_qty = value[0]
            item_price = value[1]
            
            if type(item_name) == str and type(item_qty) == int and type(item_price) == int:
                print(f"[v] {item_name :<12}: data sudah sesuai.")           
            else:
                if type(item_name) != str:
                    print(f"[x] {item_name :<12}: nama barang harus berupa teks.")
                else:
                    pass   
                
                if type(item_qty) != int:
                    print(f"[x] {item_name :<12}: jumlah item harus berupa angka.")
                else:
                    pass

                if type(item_price) != int:
                    print(f"[x] {item_name :<12}: harga item harus berupa angka.")
                else:
                    pass
            
    
    
    # Method to calculate the total price of the order items
    def total_price(self):
        '''
        Check the total price of all order items of the transaction.
        '''
        self.total_price = 0
        for value in self.order_items.values():
            item_qty = value[0]
            item_price = value[1]
            self.total_price += (item_qty * item_price)
            
        self.is_discounted(self.total_price)
        
    
    # Method to check whether a transaction gets a discount or not
    def is_discounted(self, total_price):
        '''
        Check whether a transaction will be dicounted or not.
        
        Parameters
        ----------
            total_price : int
                The total price of the transaction.
        '''
        self.total_price = total_price
        if self.total_price > 500000:
            is_discounted = True
            discount = "10%"
            discounted_price = total_price * (1 - 0.1)
        elif total_price > 300000:
            is_discounted = True
            discount = "8%"
            discounted_price = total_price * (1 - 0.08)
        elif total_price > 200000:
            is_discounted = True
            discount = "5%"
            discounted_price = total_price * (1 - 0.05)
        else:
            is_discounted = False
        
        if is_discounted == True:
            print(f"Total belanja Anda: Rp{total_price}.")
            print(f"Anda mendapat diskon {discount}.")
            print(f"Anda hanya perlu membayar: Rp{discounted_price}.")
        else:
            print(f"Total belanja Anda: Rp{total_price}.")
            print("Belanja di atas Rp200.000 untuk mendapat diskon.")