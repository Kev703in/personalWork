# Car brand sales data
#Description: Project to get the data of the car company with the year and the sales for that year from a site carsalesbase.com.


#importing beautifulsoup and requests to scrap the data
from bs4 import BeautifulSoup
import requests
import lxml
#importing matplotlib to show th ecomparison using the graphical representation
import matplotlib.pyplot as plt
import numpy as np
#importing pandas to show the data required in a tabular format
import pandas as pd

#Created a class fro vehicelsale
class VehicleSales():
    
#intitializing variables brandnames and sales and text which is getting scarpped from web
    def __init__(self):
        self.userName = input('\nEnter Your Name:')
        print('\nThis Prgram gives the car sales data of American and Chinese brands')
        print('The data is collected from "carsalesbase.com" and has records till 2021')
        input('\nPress Enter to Continue!!')
        self.usa_carBrands={}
        self.brand_sales = {}
        self.html_text = ''
        
#function to get all the brandlinks from the brand names
    def scrape_brands(self):
        try:
            # going into the website by requesting the UR:
            html_text = requests.get(self.html_text).content
            #scraping the data with tag div and classname as shown below
            soup = BeautifulSoup(html_text, 'lxml')
            cars_html=soup.find_all('div', class_="block-html-content clearfix link-color-wrap")
            #inside the div tag, finding all the a tag which are all the names of the brands in the page
            car_brands=cars_html[1].find_all('a')
            #for all the brandnames which was found getting the links of it by using th for loop
            for car_brand in car_brands:
                self.usa_carBrands.update({car_brand.text:car_brand['href']})
            print(self.usa_carBrands)
            flag = 1
        except IndexError:
            print(f"\nLink has Expired?\nLink:{self.html_text}")
            flag = 0
        return flag

#function to scrap the sales number and year for the brank from the link which was retrieved from above function
    def scrape_brand_Sales(self):
        #calling the above function to get the links
        flag = self.scrape_brands()
        if flag ==0:
            return 0
        #for all the brands scrapped retrieving the sales for it using for loop
        for brand in self.usa_carBrands:
            year_sales=[]
            #getting the data using beautifulsoup
            try:
                html_brand = requests.get(self.usa_carBrands.get(brand)).content
                soup2 = BeautifulSoup(html_brand, 'lxml')
                #parsing column and row of the table in that page and getting all the data
                table_rows=soup2.find_all('table')
                for table in table_rows:
                    if 'Sales' in (str(table)):
                        table_data = table               
                table_rows=table_data.find('tbody').find_all('tr')
                #for each row finding the required column and getting the data
                for table_row in table_rows:
                    year_sales.append([table_row.find_all('td')[0].text,int(table_row.find_all('td')[1].text.replace(',',''))])
                self.brand_sales.update({brand:year_sales})
                print(f'{brand} : Scrapping Successfull')
            except:
                #if scrapping was not successful then showing the error by printing the below
                print(f'Server issues with : {brand}')
        
                
#function to show the top 10 sales of the data
    def top_10_sales(self):
        #initializing the data and getting the brand name, year and sales
        sales_2021=[]
        sales_2020=[]
        #for the brand names getting the sales value
        for brand in self.brand_sales:
            sales_values_2021=self.brand_sales.get(brand)
            #if the sales value is 2021 it will sgo to this loop and append all the sales of that year
            if sales_values_2021[-1][0] == '2021':
                sales_2021.append([brand,sales_values_2021[-1][1]])
        sales_2021.sort(key = lambda x:int(x[1]))
        sales_2021.reverse()
        for brand_list in sales_2021:
            sales_values_2020=self.brand_sales.get(brand_list[0])
            #f it is in 2020 then it goes into this loop
            if sales_values_2020[-2][0] == '2020':
                sales_2020.append([brand_list[0],sales_values_2020[-2][1]])
            else:
                sales_2020.append([brand_list[0],0]) 
        #checks the sales which ae the top 10 by limiting the value to 10 and only returns those values    
        if len(sales_2021)>10:
            return sales_2021[:10],sales_2020[:10]
        return sales_2021,sales_2020

#function to show the top 10 in a grpahical representation
    def top_10_sales_graph(self):
        #intitializing the variables and gettung the data which was deducted which is required for graph
        sales_2021,sales_2020=self.top_10_sales()
        brand = []
        sale20 = []
        sale21 = []
        #for the 10 top appedning the values
        for i in range(len(sales_2020)):
            brand.append(sales_2020[i][0])
            sale20.append(sales_2020[i][1]/100000)
            sale21.append(sales_2021[i][1]/100000)  
        #using np and plt to plot the graph with the data required with x axis represeing brands and y axis representing sales 
        x = np.array(brand)
        x_axis = np.arange(len(brand))
        plt.bar(x_axis - 0.2, sale20, 0.4, label = '2020')
        plt.bar(x_axis + 0.2, sale21, 0.4, label = '2021')
        plt.xticks(x_axis, x)
        plt.xlabel("Brands")
        plt.ylabel("Sales number X 100000")
        plt.title("Sales of top 10 car brands in the US")
        plt.legend()
        plt.show()
    
    #function to show the brand options for the user to select
    def brandOptions(self):
        count = 1
        brands = {}
        #show all the brands with index getting updated by 1 
        for brand in self.brand_sales:
            brands.update({count:brand})
            count = count+1
        print('Choose the required brand')
        space_count = 0
        # fr all the brands which is selected show this was selected and go to that option
        for option in brands:
            space_count = space_count + 1
            print(f'{option} : {brands.get(option)}',end="\n" if space_count==3 else "\t\t")
            if space_count ==3:
                space_count = 0
        return(count,brands)

    #function to compare the two brands           
    def compareBrandsGraph(self):
        while(True):
            #it will get the index and the brand from the above function and display
            count,brands = self.brandOptions()
            print(f'\n{count} : Back to Menu')
            #to select the two brands
            while(True):
                selectedbrands = input(f'Enter two Brand options for Comparison (or) {count} for main menu\n  (example input:"52,11")\n:')
                if selectedbrands == str(count):
                    return
                x = np.array(selectedbrands.split(','))
                x = np.unique(x)
                # getting the details for the two brands after they select two brands
                if len(x) ==2:
                    brandName1=brands.get(int(x[0]))
                    brandName2=brands.get(int(x[1]))
                    sales_data1=self.brand_sales.get(brands.get(int(x[0])))
                    sales_data2=self.brand_sales.get(brands.get(int(x[1])))
                    break
                else:
                #exception to select exactly two brankds
                    print('Enter exactly Two Values seperated by comma ","')
            #intitializing the variables
            years = []
            sales1 = []
            sales2 = []
            #getting the data for first option selected and storing the sales data
            for i1 in sales_data1:
                years.append(i1[0])
            #gettng the data for the second option selected and storing the sales data
            for i2 in sales_data2:
                years.append(i2[0])
            #group into the year and then sorting 
            years = np.unique(years)
            years.sort()   
            # for the same year appending the sales number for first brand selected        
            for year in years:
                flag = True
                for i3 in sales_data1:
                    if year == i3[0]:
                        sales1.append(i3[1]/100000)
                        flag =False
                        break
                if flag == True:
                    sales1.append(0)
            # for the same year appending the sales number for the second brand selected
            for year in years:
                flag = True
                for i4 in sales_data2:
                    if year == i4[0]:
                        sales2.append(i4[1]/100000)
                        flag = False
                        break
                if flag ==True:
                    sales2.append(0) 
            #plotting the data with x-axis mentioning the years and y axis mentioning the sales               
            x = np.array(years)
            x_axis = np.arange(len(years))
            plt.plot(x_axis, sales1, label = f'{brandName1}', marker='o', linewidth=2, color='blue')
            plt.plot(x_axis, sales2, label = f'{brandName2}', marker='o', linewidth=2, color='orange')
            plt.xticks(x_axis, x)
            plt.xlabel('Years')
            plt.ylabel("Sales number X 100000")
            plt.title(f"Sales of {brandName1} & {brandName2}")
            plt.locator_params(axis='x', nbins=12)
            #of it is max,min for two brands eespectively showing it in differing colors as shown below
            plt.axhline(max(sales1), color ='red', label=f'Max Sales:{max(sales1)*100000}', linestyle='dashed' )
            plt.axhline(min(sales1), color = 'yellow', label=f'Min Sales:{min(sales1)*100000}',linestyle='dashed')
            plt.axhline(max(sales2), color ='green', label=f'Max Sales:{max(sales2)*100000}',linestyle='dashed' )
            plt.axhline(min(sales2), color = 'cyan', label=f'Min Sales:{min(sales2)*100000}',linestyle='dashed')
            plt.legend()
            plt.show()
        
    #plotting graph for the brands 
    def plotgraphbrands(self):
        # getting the list of brand names with index
        while(True):
            count,brands = self.brandOptions()
            print(f'\n{count} : Back to Menu')
            while(True):
                #selecting the brand
                brandSelection = int(input('Enter the desired option:'))
                if brandSelection == count:
                    return
                #getting the sales data for the brand selected
                elif brandSelection in range(1,count):
                    brand_name=brands.get(brandSelection)
                    sales_data=self.brand_sales.get(brands.get(brandSelection))
                    break
            #initializing the variable and then getting the sales year and seles number for the brand selected
            year = []
            sales = []
            for i in range(len(sales_data)):
                year.append(sales_data[i][0])
                sales.append(sales_data[i][1]/100000)
            # pring the data retrieved in a table format and showing in data.csv file
            data = pd.DataFrame(sales_data,columns = ['year','sales'])
            print(data)
            data.to_csv('data.csv', sep = ",", mode = "w", index = False)
            #plotting the graph with x axis as brand name and y axis as the sales
            x = np.array(year)
            x_axis = np.arange(len(year))
            plt.stem(x_axis, sales, label = f'{brand_name}')
            plt.xticks(x_axis, x)
            plt.xlabel(brand_name)
            plt.ylabel("Sales number X 100000")
            plt.title(f"Sales of {brand_name}")
            plt.locator_params(axis='x', nbins=12)
            # showing the maximum sales in green and minimum sales in red
            plt.axhline(max(sales), color ='green', label=f'Max Sales:{max(sales)*100000}',linestyle='dashed' )
            plt.axhline(min(sales), color = 'red', label=f'Min Sales:{min(sales)*100000}',linestyle='dashed')
            plt.legend()
            plt.show()   
            input('\nPress Enter to continue')

# creating a subclass menu for the class vehiclesales
class Menu(VehicleSales):
    
    def mainMenu(self):
        #scarping the data in the function called from the website
        flag = self.scrape_brand_Sales()
        if flag == 0:
            return
        while(True): 
            try:   # Menu loop valid until user selects the Exit option and exitFlag=True.
                selectedOperation= int(input("\nSelect operation to pracitice:-\n1 - Sales graph of Top 10 in 2021\n2 - Sales per Brand\n3 - Compare two Brands\n4 - Back\n5 - Exit Program\n:"))
                if selectedOperation not in [1,2,3,4,5]:
                    print("Choose from the given option")
                # request user option.    
                if selectedOperation in [1]:
                    #if option 1 get the top 10 sales for the brand
                    self.top_10_sales_graph()
                #show the graph for the brand selectd
                elif selectedOperation in [2]:
                    self.plotgraphbrands()
                # comapare two brands and show the data
                elif selectedOperation in [3]:
                    self.compareBrandsGraph()
                #go back
                elif(selectedOperation==4):
                    return
                    #exit from the program
                elif(selectedOperation==5):   # Call function to save Report
                    print('')
                    exit()
            except ValueError:
                print("\nThe server is not responding")
            continue


    #chose which webiste you need to scarp US company website or china one or go back
    def countrySelect(self):
        while(True):
            try:
                selectedCountry = int(input('Kindly select the country :-\n1 - United States of America\n2 - China\n3 - Exit Program\n:'))
                if selectedCountry not in [1,2,3]:
                    print("Please select from the given option")
                if selectedCountry == 1:
                    self.html_text='https://carsalesbase.com/car-sales-us-home-main/car-sales-by-brand-us/'
                    # self.html_text='https://www.goodcarbadcar.net/automotive-sales-by-brand/'
                elif selectedCountry == 2:
                    self.html_text='https://carsalesbase.com/car-sales-china-home-main/car-sales-by-brand-china/'
                    #self.html_text='https://www.goodcarbadcar.net/china-automotive-brand-sales-hub/'
                elif selectedCountry == 3:
                    return  
                self.mainMenu()
            except ValueError:
                print("\nThe server is not responding")
  #main function which goes to menu to slect the country          
def main():
    user = Menu()
    user.countrySelect()

#main function is called
if __name__=='__main__':
    main()    

        

