import numpy as np
import matplotlib.pyplot as plt

def to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

def from_polar(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.array([x, y])

def get_vector_input(name):
    x = float(input(f"Enter x for vector {name}: "))
    y = float(input(f"Enter y for vector {name}: "))
    return np.array([x, y])

# Step 1: Input vectors
v1 = get_vector_input("A")
v2 = get_vector_input("B")

# Step 2: Convert to polar coordinates
r1, theta1 = to_polar(v1[0], v1[1])
r2, theta2 = to_polar(v2[0], v2[1])

print("\n--- Polar Coordinates ---")
print(f"Vector A: magnitude = {r1:.2f}, angle = {np.degrees(theta1):.2f}°")
print(f"Vector B: magnitude = {r2:.2f}, angle = {np.degrees(theta2):.2f}°")

# Step 3: Vector operations
add = v1 + v2
sub = v1 - v2
mul = v1 * v2  # element-wise multiplication
div = np.divide(v1, v2, out=np.zeros_like(v1), where=v2!=0)  # avoid divide-by-zero
power = np.power(v1, v2, where=v1 >= 0)  # limit domain to avoid complex results

# Step 4: Print results
print("\n--- Vector Operations ---")
print(f"Addition (A + B): {add}")
print(f"Subtraction (A - B): {sub}")
print(f"Element-wise Multiplication (A * B): {mul}")
print(f"Element-wise Division (A / B): {div}")
print(f"Element-wise Power (A ** B): {power}")

# Step 5: Plotting
vectors = {
    "Vector A": v1,
    "Vector B": v2,
    "Addition": add,
    "Subtraction": sub,
    "Multiplication": mul,
    "Division": div,
    "Power": power
}

colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown', 'cyan']


plt.figure(figsize=(10, 8))
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)

for i, (label, vec) in enumerate(vectors.items()):
    plt.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1,
               color=colors[i % len(colors)], label=label)

plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.grid(True)
plt.legend()
plt.title("Vector Operations Visualization")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
