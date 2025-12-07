# Найдите количество книг, которое можно разместить на дискете

diskette_size_mb = 1.44
diskette_size_bytes = diskette_size_mb * 1024 * 1024

pages_per_book = 100
lines_per_page = 50
symbols_per_line = 25
bytes_per_symbol = 4

symbols_per_book = pages_per_book * lines_per_page * symbols_per_line
bytes_per_book = symbols_per_book * bytes_per_symbol

books_count = int(diskette_size_bytes // bytes_per_book)

print("Количество книг, помещающихся на дискету:", books_count)
