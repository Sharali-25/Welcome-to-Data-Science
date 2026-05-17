import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="ticks")
weather = pd.read_csv("Test.csv")
print(weather.head(10))
print(weather.info())

sns.barplot(x=weather["humidity"],y=weather["temperature"])
plt.show()

sns.displot(weather["humidity"],kde=False, rug=True)
plt.show()

sns.jointplot(x=weather["humidity"],y=weather["temperature"], kind="hist")
plt.show()

sns.pairplot(weather[["humidity","temperature","air_pollution_index"]])
plt.show()

sns.stripplot(x=weather["weather_type"],y=weather["temperature"],jitter=True)
plt.show()

sns.swarmplot(x=weather["humidity"],y=weather["temperature"])
plt.show()