# Function to create a mirrored right-angled triangle
def mirrored_triangle(n):
    for i in range(1, n + 1):
        # Print spaces for alignment
        print(' ' * (n - i), end='')
        # Print stars for the triangle
        print('*' * i)

# Example usage
rows = 5  # You can change the number of rows
mirrored_triangle(rows)
