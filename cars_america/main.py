from cars import Cars
filename = 'cars.csv'  
c = Cars(filename)
desc = 'descending'
asc = 'ascending'
new_car = [30, "6300", "toyota", "cruiser",2008, "clean vehicle", 274117, \
 "black", "jtezu11f88k007763", "159348797", "new jersey", "usa", "10 days left"]

#All database specifications:
print("This database contains 11 columns:")
for i in range(0, 11):
    print(c.columnNames(i), end='')
    if i != 10:
        print(end=', ')
print()

print('======================================')
print('TASK 2. CRUD operations')
print('======================================')
#creates new row
c.createRow(new_car)
#reads particular car data from file
c.readRow(1)
print(c[2])
#updates row, also supports item reassignment
c.updateRow(3, new_car)
c[4] = c[30]
#deletes particular car data from file
c.deleteRow(5)

print('======================================')
print('TASK 3. Text file handling methods')
print('======================================')
#commonly used to update the file
#reads and prints all data from file
# c.readFile()
#outputs only particular car data in initial file
# c.outputFile()
# c.outputFileRow(7)
print('======================================')
print('TASK 4. Basic algorithms from lectures')
print('======================================')
#makes a copy of a car and outputs in file
c.copyRow(6)
#uses Merge sort to sort by a key
#  and outputs in the file
c.outputSortedFile(c.sortCars(0, desc))
#Sums up the price of everycar 
# and prints in the terminal
c.priceSummarization()
#Counts cars depending on the searching key
#  on a particular column
c.countCarByIndex(9, 'new jersey')
#Uses binary search in order to find 
# particular car data and print in terminal
c.searchByMileage(34861)

print('======================================')
print('TASK 5. Business calculations')
print('======================================')
#counts number of branded cars from 
# the file and prints the results
c.ModelonSale("ford")
#calculates the average price for
#particular branded car
c.avg_price_for_brand("ford")
#Counts branded cars on sale on a particular year 
# and stores them in a dictionary
c.distribution_of_brand(2017)
#Calls avg_price_for_brand_in_year() and avg_price_for_brand() 
#to calculate the change in percents 
c.change_in_price('chevrolet', 2018)