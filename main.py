import cashier as c

trnsct_123 = c.Transaction()

# Test Case 1
print("TEST CASE 1")
print("Customer ingin menambahkan 2 item, yaitu:")
print("1. 'Ayam Goreng', Qty: 2, Harga: 20000")
print("2. 'Pasta Gigi', Qty: 3, Harga: 15000\n")

trnsct_123.add_item("Ayam Goreng", 2, 20000)
trnsct_123.add_item("Pasta Gigi", 3, 15000)


# Test Case 2
print("TEST CASE 2")
print("Ternyata customer salah menambahkan item dan ingin menghapus item 'Pasta Gigi' dari belanjaan.\n")

trnsct_123.delete_item("Pasta Gigi")

# Test Case 3
print("TEST CASE 3")
print("Ternyata customer salah memasukkan item yang lain juga.")
print("Daripada menghapus satu persatu, dia ingin me-reset seluruh daftar belanjaan.\n")

trnsct_123.reset_transaction()

# Test Case 4
print("TEST CASE 4")
print("Ternyata customer salah memasukkan item yang lain juga.")

trnsct_123.add_item("Ayam Goreng", 2, 20000)
trnsct_123.add_item("Pasta Gigi", 3, 15000)
trnsct_123.add_item("Mainan Mobil", 1, 200000)
trnsct_123.add_item("Mie Instant", 5, 3000)

trnsct_123.total_price()

# Apakah show_order_table() sebaiknya tidak disatukan dengan method_method yang lain, ya?
