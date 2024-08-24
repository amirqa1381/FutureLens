import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Plotter:
    def __init__(self, file):
        self.data = file
        print("Successfully read CSV file.")

    def data_head(self):
        """Get the first 5 rows of the CSV file."""

        dfhead = self.data.head()
        return dfhead

    def plot(self, x, y):
        plt.plot(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'Plot of {x} vs {y}')
        plt.show()

    def hist(self, column):
        plt.hist(self.data[column], bins=10)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {column}')
        plt.show()

    def scatter(self, x, y):
        plt.scatter(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'Scatter Plot of {x} vs {y}')
        plt.show()

    def bar(self, x, y):
        plt.bar(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'Bar Chart of {x} vs {y}')
        plt.show()

    def boxplot(self):
        plt.boxplot(self.data.values)
        plt.title('Box Plot')
        plt.show()

    def heatmap(self, data):
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm', square=True)
        plt.title('Heatmap')
        plt.show()

    def pairplot(self):
        sns.pairplot(self.data)
        plt.title('Pair Plot')
        plt.show()

    def countplot(self, column):
        sns.countplot(x=column, data=self.data)
        plt.title(f'Count Plot of {column}')
        plt.show()

    def distplot(self, column):
        sns.distplot(self.data[column])
        plt.title(f'Distribution Plot of {column}')
        plt.show()

    def violinplot(self, x, y):
        sns.violinplot(x=x, y=y, data=self.data)
        plt.title(f'Violin Plot of {x} vs {y}')
        plt.show()

