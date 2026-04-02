
# import libraries and load dataset
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
customer_satisfaction_dataset = pd.read_csv("user_satisfaction_150.csv") # copy file path here or file name if dataset is in project folder
print(customer_satisfaction_dataset)

#
satisfied_user_count = customer_satisfaction_dataset["satisfaction"].value_counts()
print(satisfied_user_count)


# Visualizing customer satisfaction data through bar plot
sns.barplot(x =satisfied_user_count.index,  y= satisfied_user_count.values) # .index gives us the names/labels & .values gives us the actual values/data
plt.title("Customer Satisfaction Distribution")
plt.xlabel("Satisfaction Level")
plt.ylabel("Number of users")
plt.xticks(rotation = 30) # To avoid smudging of x-axis data labels


# Age-wise customer satisfaction data 
customer_by_age =customer_satisfaction_dataset["age"].value_counts()
print(customer_by_age)

# group by customers with same satisfaction level
age_satisfaction = customer_satisfaction_dataset.groupby(["age", "satisfaction"]).size()
print(age_satisfaction)

# convert a row index into column index an filling missing or NaN values with 0
age_satisfaction = customer_satisfaction_dataset.groupby(["age", "satisfaction"]).size().unstack(fill_value=0)
print(age_satisfaction)

# plot stacked bar graph for bivariate analysis:
age_satisfaction.plot(kind="bar", stacked=True, figsize=(8,8)) # Bar for vertical bars & barh for horizontal bars. 
# we want stacked graph, we write true. If we write false, bars are placed side by side.                                                
plt.title("Age vs Satisfaction Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.legend(title="Satisfaction")

plt.show() # show both plot hers

# Digging through other parameters for deep insights
# Analyzing data distribution by gender (male and female count)
user_count_by_gender = customer_satisfaction_dataset["gender"].value_counts()
print(user_count_by_gender)

# Analyzing data distribution by category count
product_category_count = customer_satisfaction_dataset["product_category"].value_counts()
print(product_category_count)

