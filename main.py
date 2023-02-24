import matplotlib.pyplot as plt
from countryinfo import CountryInfo


c1 = input("Please enter a country's name: ")
c2 = input("Please enter another country's name: ")

country1 = CountryInfo(c1)
country2 = CountryInfo(c2)

try:
    data1 = country1.population()
except:
    print("First country name doesn't exist or contains a typo.")

try:
    data2 = country2.population()
except:
    print("Second country name doesn't exist or contains a typo.")

# print(c1 + ": " + str(data1))
# print(c2 + ": " + str(data2))

# Create a bar chart
fig, ax = plt.subplots()
ax.bar([c1, c2], [data1, data2])

# Add labels and title
ax.set_xlabel('Country')
ax.set_ylabel('Population')
ax.set_title("Current population of " + c1+" and " + c2)

# Display the chart
plt.show()