# Looking at insurance information and basic analysis

# importing of modules

from pprint import pprint  # Used mainly for evaluating in the console
import csv
import statistics


class InsuranceData:  # instead of making individual functions for each process I tried object-orientation to practice using classes and methods

    def __init__(self, csv_file='insurance.csv'):  # Starting with our constructor, this will create the various calls and empty lists to populate
        self.data = []
        self.ages = []
        self.sexes = []
        self.bmis = []
        self.num_children = []
        self.smoker_statuses = []
        self.regions = []
        self.insurance_charges = []
        self.patient_dictionary = {}

        with open(csv_file, newline='') as csvinsurance:   # reading in our insurance file to parse out the data
            csv_reader = csv.DictReader(csvinsurance)
            for row in csv_reader:  # iterating over all rows of the data
                row['bmi'] = float(row['bmi'])  # Converts the bmi string to a float
                row['age'] = int(row['age'])  # Converts the age string to an integer
                row['children'] = int(row['children'])  # Converts the children string to an integer
                row['smoker'] = row['smoker'].lower() == 'yes'  # Converts the smoker string from 'yes' and 'no' to Booleans
                row['charges'] = float(row['charges'])  # Converts the charges string to a float
                self.data.append(row)  # populating individual lists
                self.ages.append(row['age'])  # populating individual lists
                self.sexes.append(row['sex'])  # populating individual lists
                self.bmis.append(row['bmi'])  # populating individual lists
                self.num_children.append(row['children'])  # populating individual lists
                self.smoker_statuses.append(row['smoker'])  # populating individual lists
                self.regions.append(row['region'])  # populating individual lists
                self.insurance_charges.append(row['charges'])  # populating individual lists
                self.patient_dictionary["age"] = [int(age) for age in self.ages]  # creating a dictionary with the list values
                self.patient_dictionary["sex"] = self.sexes  # creating a dictionary with the list values
                self.patient_dictionary["bmi"] = self.bmis  # creating a dictionary with the list values
                self.patient_dictionary["children"] = self.num_children  # creating a dictionary with the list values
                self.patient_dictionary["smoker"] = self.smoker_statuses  # creating a dictionary with the list values
                self.patient_dictionary["regions"] = self.regions  # creating a dictionary with the list values
                self.patient_dictionary["charges"] = self.insurance_charges  # creating a dictionary with the list values

    def get_data(self, value, params):  # should return a list of values from a header with a specified dictionary argument
        return [float(row[value]) for row in filter(lambda row: all(row[k] == v for k, v in params.items()), self.data)]

    def get_average(self, value, params=None):  # returns the average value of a data header set
        params = params or dict()
        if value == 'smoker':
            raise Exception("Boolean value is not valid entry")
        elif value == 'sex' or value == 'region':
            raise Exception("String value is not valid entry")

        return round(
                statistics.fmean(
                    self.get_data(value, params)), 2
        )

    def get_median(self, value, params=None):  # returns the mean value of a data header set
        params = params or dict()
        if value == 'smoker':
            raise Exception("Boolean value is not valid entry")
        elif value == 'sex' or value == 'region':
            raise Exception("String value is not valid entry")

        return statistics.median(
            self.get_data(value, params)
        )

    def get_standard_deviation(self, value, params=None):  # returns the standard deviation value of a data header set
        params = params or dict()
        if value == 'smoker':
            raise Exception("Boolean value is not valid entry")
        elif value == 'sex' or value == 'region':
            raise Exception("String value is not valid entry")

        return round(
                statistics.stdev(
                    self.get_data(value, params)), 2
        )

# Variable to call Insurance Data from. Makes it easier to call different parts

insurance_data = InsuranceData()

# Average Age
average_age = insurance_data.get_average('age')

age_standard_deviation = insurance_data.get_standard_deviation('age')

# Count of different sexes in data

number_of_females = insurance_data.sexes.count('female')

number_of_males = insurance_data.sexes.count('male')

# BMI information

# BMI average across all fields
average_bmi = insurance_data.get_average('bmi')

# BMI average of sex

# BMI average across all female data points
average_bmi_female = insurance_data.get_average('bmi', {'sex': 'female'})
# BMI average across all male data points
average_bmi_male = insurance_data.get_average('bmi', {'sex': 'male'})

# BMI average of smokers

# BMI average across all smoker
average_bmi_smoker = insurance_data.get_average('bmi', {'smoker': True})
# BMI average across all non-smokers
average_bmi_non_smoker = insurance_data.get_average('bmi', {'smoker': False})

# BMI average of sex and if smoking

# BMI average across all females who smoke data points
average_bmi_female_smoker = insurance_data.get_average('bmi', {'smoker': True, 'sex': 'female'})
# BMI average across all females who do not smoke data points
average_bmi_female_non_smoker = insurance_data.get_average('bmi', {'smoker': False, 'sex': 'female'})
# BMI average across all males who smoke data points
average_bmi_male_smoker = insurance_data.get_average('bmi', {'smoker': True, 'sex': 'male'})
# BMI average across all males who do not smoke data points
average_bmi_male_non_smoker = insurance_data.get_average('bmi', {'smoker': False, 'sex': 'male'})

# Charges information

# Charges average across all fields
average_charges = insurance_data.get_average('charges')

# Charges average of sex

# Charges average across all female data points
average_charges_female = insurance_data.get_average('charges', {'sex': 'female'})
# Charges average across all male data points
average_charges_male = insurance_data.get_average('charges', {'sex': 'male'})

# Charges average of smokers

# Charges average across all smoker
average_charges_smoker = insurance_data.get_average('charges', {'smoker': True})
# Charges average across all non-smokers
average_charges_non_smoker = insurance_data.get_average('charges', {'smoker': False})

# Charges average of sex and if smoking

# Charges average across all females who smoke data points
average_charges_female_smoker = insurance_data.get_average('charges', {'smoker': True, 'sex': 'female'})
# Charges average across all females who do not smoke data points
average_charges_female_non_smoker = insurance_data.get_average('charges', {'smoker': False, 'sex': 'female'})
# Charges average across all males who smoke data points
average_charges_male_smoker = insurance_data.get_average('charges', {'smoker': True, 'sex': 'male'})
# Charges average across all males who do not smoke data points
average_charges_male_non_smoker = insurance_data.get_average('charges', {'smoker': False, 'sex': 'male'})
