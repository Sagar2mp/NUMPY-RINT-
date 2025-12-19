import numpy as np
data = np.array([0.5, 1.5, 2.5, 3.5, 4.1, 10.9])
rounded_data = np.rint(data)
print(f"Original array: {data}")
print(f"Rounded values: {rounded_data}")
