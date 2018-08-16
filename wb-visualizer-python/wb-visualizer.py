# Python script for fetching and plotting data from the World Bank. By: Daniel Sonne Lehnberg

import wbdata
import pandas
import matplotlib.pyplot as plt

#Setting up the country selections
countries = ["SE","DK","FI"]

#Setting up the indicators
indicators = {'NY.GNP.PCAP.CD':'GNI per Capita'}

#Using the indicators above for the countries above to put the data into a #DataFrame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)

#The DataFrame is pivoted, so we'll use the unstack function to make it plottable
dfu = df.unstack(level=0)

# Plotting the unstacked dataframe with a legend, title and axis-labels
dfu.plot();
plt.legend(loc='best');
plt.title("GNI Per Capita ($USD, Atlas Method)");
plt.xlabel('Date'); plt.ylabel('GNI Per Capita ($USD, Atlas Method');

# Saving the figure
#plt.savefig('some/path/of/yours/gniplot.png')

# Showing the figure
plt.show()