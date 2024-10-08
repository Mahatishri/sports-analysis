import pandas as pd

# Create the data of the DataFrame as a dictionary
data_df = {
    'Name': ['Asha', 'Harsh', 'Sourav', 'Riya', 'Hritik',
             'Shivansh', 'Rohan', 'Akash', 'Soumya', 'Kartik'],
    'Department': ['Administration', 'Marketing', 'Technical', 'Technical', 'Marketing',
                   'Administration', 'Technical', 'Marketing', 'Technical', 'Administration'],
    'Employment Type': ['Full-time Employee', 'Intern', 'Intern', 'Part-time Employee',
                        'Part-time Employee', 'Full-time Employee', 'Full-time Employee', 
                        'Intern', 'Intern', 'Full-time Employee'],
    'Salary': [120000, 50000, 70000, 70000, 55000,
               120000, 125000, 60000, 50000, 120000],
    'Years of Experience': [5, 1, 2, 3, 4,
                            7, 6, 2, 1, 6]
}

# Create the DataFrame
df = pd.DataFrame(data_df)

# Display the DataFrame
print(df)

df_grouped = df.groupby('Department')
print("Grouped by Department")
print(df_grouped)
print(df_grouped.get_group('Technical'))

groups = df.groupby(by='Department')
print()
print(groups.groups)

groups1 = df.groupby(['Employment Type', 'Department'])
print("Mean")
print(groups1.aggregate('mean'))