import os

# Create 'tables' folder if it doesn't exist
os.makedirs("tables", exist_ok=True)

def generate_tables(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"
    
    # Save each table in a separate file
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables from 1 to 24
for i in range(1, 25):
    generate_tables(i)
