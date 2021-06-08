n = 10
for i in range(n):
    print("  "*i + "오" + "  "*2*(n-1-i) + "직")
for i in range(n):
    print("  "*(n-1-i) + "직" + "  "*2*i + "진")
