
[![CI](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject5/actions/workflows/cicd.yml)

IDS706_DataEngineering_BarbaraFlores_Miniproject5
## 📂 Python Script interacting with SQL Database

The goal of this task is to create a Python script that effectively interacts with a SQL database.

In this miniproject, the following activities were undertaken:

### 1. Connect to a SQL database. 

Connect to a SQL database. In particular, the [world-small.csv](https://raw.githubusercontent.com/sejdemyr/sejdemyr.github.io/master/r-tutorials/basics/data/world-small.csv) database was used, which was employed in the `"Practical Data Science"` class taught by Nick Eubank. This database contains information about some countries, their regions, and their values for `Polity IV` and `gdppcap08`.

- The **polityIV** variable in this dataset is an expert score for a country's authoritarianism. Traditionally, values of -10 represent extreme autocracies, while values of 10 denote consolidated liberal democracies. However, in this dataset, they have been rescaled to range from 0 to 20, where 0 represents an extreme autocracy, and 20 represents a consolidated liberal democracy.

- The variable **gdppcap08** represents the GDP per Capita values for countries in the year 2008.

With [extract.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject5/blob/main/mylib/extract.py) scrypt, we extract a CSV file from [an extrenal url](https://raw.githubusercontent.com/sejdemyr/sejdemyr.github.io/master/r-tutorials/basics/data/world-small.csv) and save its content to [a local path](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject5/blob/main/data/WorldSmall.csv). The extract function utilizes the requests library to make an HTTP request, and then it saves the response content.


