import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. How many of each race are represented in this dataset?
    race_counts = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Percentage with advanced education (>50K)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of people working minimum hours who earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = round(
        (len(rich_min_workers) / len(num_min_workers)) * 100, 1
    )

    # 7. Country with highest percentage of people earning >50K
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()

    highest_earning_country_percentage = round(
        (rich_country_counts / country_counts * 100).max(), 1
    )
    highest_earning_country = (rich_country_counts / country_counts * 100).idxmax()

    # 8. Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].mode()[0]

    if print_data:
        print("Number of each race:\n", race_counts)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education earning >50K:", higher_education_rich)
        print("Percentage without higher education earning >50K:", lower_education_rich)
        print("Minimum work hours per week:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top occupations in India for those earning >50K:", top_IN_occupation)

    # Return results in a dictionary for testing purposes
    return {
        'race_counts': race_counts,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
