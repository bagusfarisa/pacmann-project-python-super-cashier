import cashier

trnsct_123 = cashier.Transaction()

# Test Case 1
print("\n>> TEST CASE 1")
print("Customer ingin menambahkan 2 item, yaitu:")
print("1. 'Ayam Goreng', Qty: 2, Harga: 20000")
print("2. 'Pasta Gigi', Qty: 3, Harga: 15000\n")

trnsct_123.add_item("Ayam Goreng", 2, 20000)
trnsct_123.add_item("Pasta Gigi", 3, 15000)
print(trnsct_123.order_items)
print()
trnsct_123.show_order_table()


# Test Case 2
print("\n\n>> TEST CASE 2")
print("Ternyata customer salah menambahkan item dan ingin menghapus item 'Pasta Gigi' dari belanjaan.\n")

trnsct_123.delete_item("Pasta Gigi")
print(trnsct_123.order_items)
print()
trnsct_123.show_order_table()

# Test Case 3
print("\n\n>> TEST CASE 3")
print("Ternyata customer salah memasukkan item yang lain juga.")
print("Daripada menghapus satu persatu, dia ingin me-reset seluruh daftar belanjaan.\n")

trnsct_123.reset_transaction()
trnsct_123.show_order_table()

# Test Case 4
print("\n\n>> TEST CASE 4")
print("Customer akhirnya memutuskan untuk membeli 4 barang berikut ini:")
print("1. 'Ayam Goreng', Qty: 2, Harga: 20000")
print("2. 'Pasta Gigi', Qty: 3, Harga: 15000")
print("1. 'Mobil Mainan', Qty: 1, Harga: 200000")
print("2. 'Mie Instant', Qty: 5, Harga: 3000\n")

trnsct_123.add_item("Ayam Goreng", 2, 20000)
trnsct_123.add_item("Pasta Gigi", 3, 15000)
trnsct_123.add_item("Mainan Mobil", 1, 200000)
trnsct_123.add_item("Mie Instant", 5, 3000)
print(trnsct_123.order_items)
print()
trnsct_123.show_order_table()
print()
trnsct_123.total_price()
