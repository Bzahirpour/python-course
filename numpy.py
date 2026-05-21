import numpy as np

# data
#heights = [5, 6, 5, 5, 6]
#weights = [120, 151, 121, 125, 155]

#create array
np_hieghts = np.array([5, 6, 5, 5, 6])
np_wiehgts = np.array([120, 151, 121, 125, 155])

weight_per_height = np_hieghts / np_wiehgts

print(weight_per_height)


condition = weight_per_height > 0.04
index = np.where(condition)
print(index)


# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)


# Print out type of np_baseball
print(np_baseball)


twod_array = np.array([[1, 2, 3], [4, 5, 6]])
print(twod_array[:, 1:3])


baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseballs = np.array(baseball)
print(np_baseballs)