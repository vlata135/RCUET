# # from time import sleep

# # print("This is my file to demonstrate best practices.")

# # def process_data(data):
# #     print("Beginning data processing...")
# #     modified_data = data + " that has been modified"
# #     sleep(3)
# #     print("Data processing finished.")
# #     return modified_data

# # def main():
# #     data = "My data read from the Web"
# #     print(data)
# #     modified_data = process_data(data)
# #     print(modified_data)

# # if __name__ == "__main__":
# #     main()




# for i in range(3):
#     print(i)
import imp


import numpy as np
A = np.array([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
print(np.linalg.inv(A))