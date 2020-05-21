from covid import Covid

covid = Covid()

countries = covid.list_countries() #List Countries

usa = covid.get_status_by_country_name('US') #Get Status By Country Name

usa = covid.get_status_by_country_id(18) #Get Status By Country ID

data = {
        key : usa[key]
        for key in usa.keys() and {'confirmed',
                             'active',
                             'deaths',
                             'recovered'}
        }
        
print(data)        
