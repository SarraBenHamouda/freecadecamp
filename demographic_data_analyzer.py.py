import pandas as pd

def calculate_demographic_data(print_data=True):
    
    df = pd.read_csv('adult.data.csv')

   
    race_counts = df['race'].value_counts()


    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

   
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

 
    min_work_hours = df['hours-per-week'].min()

   
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = round(
        (len(rich_min_workers) / len(num_min_workers)) * 100, 1
    )

    
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts();

    highest_earning_country_percentage = round(
        (rich_country_counts / country_counts * 100).max(), 1
    )
    highest_earning_country = (rich_country_counts / country_counts * 100).idxmax()

   
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

    # Return results
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
