import update_data as ud
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

y = ud.load_the_data()
x = y.update_housing()

end_line = "\n" + "-" * x.shape[1] + "\n"
# print(x.head(), end=end_line
print("We are now displaying the x.info() now on the line below", end=end_line)
print(x.info(), end=end_line)
print(
    "Below this we will be displaying the value_counts of x['ocean_proximity']",
    end=end_line,
)
print(x["ocean_proximity"].value_counts(), end=end_line)
print("Next we are describing the values within x through the use of x.describe()", end=end_line)
print(x.describe(), end=end_line)
print(y.__str__())
x.hist(bins=50, figsize=(12, 8))
plt.show()
train_set, test_set = train_test_split(x, test_size=0.2, random_state=42)
print(len(train_set))
print(len(test_set))
