'''Albert Kabore
Week 1 - P1: Create a New Python Module (Company Byline)
This module provides a reusable byline for the author's services. 
'''

import math
import statistics

def main():

    #Define Variables
    company_name: str = 'GlobBISTECH ( Global Business Intelligence, Security and Technology) LLC'
    company_description: str = 'Artificial Intelligence, Data Science & Analytics, Cybersecurity and innovative technologies consulting company'
    company_founding_year: int = 2023
    company_city: str = 'Yonkers'
    company_state: str = 'New York'
    company_number_employees: int = 1
    has_international_presence: bool = True
    employee_benefits: list = ['Insurance', 'Flexible Schedule']
    services_offered: list = ['Artificial Intelligence', 'Data Science & Analysis', 'Machine Learning engineering']
    customer_satisfaction: float = 9.9
    service_pricing: list = [300, 900, 200]

# Multiline string with byline using f-string formatting
    byline: str = f"""
    Information:
    Name: {company_name}
    Description: {company_description}
    Founded: {company_founding_year}
    City: {company_city}
    State: {company_state}
    Number of Employees: {company_number_employees}
    International: {has_international_presence}
    Employee Benefits: list = ['Insurance', 'Flexible Schedule']
    Services Offered: list = ['Artificial Intelligence', 'Data Science & Analysis', 'Machine Learning engineering']
    Customer Satisfaction: {customer_satisfaction} Out of 10!
    """

#Prices for services offered
    stats_string: str = f"""
    Services with Pricing:
    Services Offered: {services_offered}
    Service Prices: {service_pricing}
    Maximum Service Price: {max(service_pricing)}
    Minimum Service Price: {min(service_pricing)}
    Mean Service Price: {statistics.mean(service_pricing)}
    Median Service Price: {statistics.median(service_pricing)}
    Standard Deviation of Service Price: {statistics.stdev(service_pricing)}
    """

    print(byline)
    
# Call the main function to execute the code
if __name__ == '__main__':
        main()
    
