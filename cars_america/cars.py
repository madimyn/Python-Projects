ID = 0 
class Cars():
  def __init__(self, filename):
    self._filename = filename
    self._cars = self.inputFile()


  def columnNames(self, num):
    names = {0:'id', 1:'price', 2:'brand', 3:'model', 4:'year', 5:'title_status', 6:'mileage', \
             7:'color', 8:'vin', 9:'state', 10:'condition'}
    return names[num]
  
    # CRUD Funcitons 
  def createRow(self, car_new = []):
    with open("cars.csv", "a") as f:
      f.write(','.join(map(str, car_new)) + '\n')
    print("Create row finished")
  def readRow(self, id):
    initial_id = ID
    g = 0
    for i, car in enumerate(self._cars):
      if car[initial_id] == str(id):
        print(self._cars[i])
        g = g  + 1
        break
    if g == 0:
      print(f"Car with ID:{id} not found")
    
  def updateRow(self, id, car_update = []):
    initial_id = ID
    for i, car in enumerate(self._cars):
      if int(car[initial_id]) == id:
        self._cars[i] = car_update
        self.outputFile()
        break
    print("Update row finished")

  def deleteRow(self, id):
    with open('cars.csv', 'w') as f:  
      f.write("id,price,brand,model,year,title_status,mileage,color,vin,state,condition\n")
      for i, car in enumerate(self._cars):
        if int(car[0]) != id:
          f.write(','.join(map(str, self._cars[i])) + '\n')
    print("Delete row Finished")

  # File handling
  def inputFile(self):
    with open(self._filename, 'r') as f:
      text = f.readlines()
      return [row.strip().split(',') for row in text[1:]]
  
  def readFile(self):
    for car in self._cars:
      print(car)
    print("Read file finished")

  def __getitem__(self, index):
    if 0 <= index < len(self._cars):
      return self._cars[index]
    
  def __setitem__(self, id, car_update):
    if 0 <= id < len(self._cars):
      self.updateRow(id, car_update)
    
  def outputFile(self):
    with open(self._filename, 'w') as f:
      f.write("id,price,brand,model,year,title_status,mileage,color,vin,state,condition\n")
      if self._cars:
        for car in self._cars:
          f.write(','.join(map(str, car)) + '\n')

  def outputSortedFile(self, cars = None):
    with open(self._filename, 'w') as f:
      f.write("id,price,brand,model,year,title_status,mileage,color,vin,state,condition\n")
      if cars:
        for car in cars:
          f.write(','.join(map(str, car)) + '\n')

  def outputFileRow(self, id):
    initial_id = ID
    with open('cars.csv', 'w') as f:
      # f.write("id,price,brand,model,year,title_status,mileage,color,vin,state,condition\n")
      for i, car in enumerate(self._cars):
        if int(car[initial_id]) == id:
          f.write(','.join(map(str, self._cars[i])) + '\n')
    print("Output file row finished.")
    
  #Basic algorithms (next 4)
  def copyRow(self, id):
    if id in [int(self._cars[id][0])]:
      with open('cars.csv', 'a') as f:
        f.write(','.join(map(str, self._cars[id])) + '\n')
    print("Copy row finished")

  def priceSummarization(self):
    sum = 0
    length = len(self._cars)
    for i in range(1, length):
      sum = sum + int(self._cars[i][1])
    print(f"The total price for all cars from data set is {sum} $")
    return sum

  def countCarByIndex(self, index, key):
    length = len(self._cars)
    occurencies = 0
    where = []
    for i in range(length):
      if self._cars[i][index] == str(key):
        where.append(self._cars[i][0])
        occurencies += 1   
    print(f"Cars with {self.columnNames(index)} \"{key}\" occured {occurencies} times, where id = {where}")
  
  def mergeSort(self, cars, key):
    if len(cars) > 1:
        mid = len(cars) // 2
        left_half = cars[:mid]
        right_half = cars[mid:]
        self.mergeSort(left_half, key)
        self.mergeSort(right_half, key)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if int(left_half[i][key]) < int(right_half[j][key]):
                cars[k] = left_half[i]
                i += 1
            else:
                cars[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            cars[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            cars[k] = right_half[j]
            j += 1
            k += 1
        return cars
    
  def mergeSortForStr(self, cars, key):
    if len(cars) > 1:
        mid = len(cars) // 2
        left_half = cars[:mid]
        right_half = cars[mid:]
        self.mergeSortForStr(left_half, key)
        self.mergeSortForStr(right_half, key)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                cars[k] = left_half[i]
                i += 1
            else:
                cars[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            cars[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            cars[k] = right_half[j]
            j += 1
            k += 1
        return cars
    
  def searchByMileage(self, num):
        num = int(num)
        cars = self.sortCars(6, 'ascending')
        low, high = 0, len(cars) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_num = int(cars[mid][6])  # Convert mileage to integer for comparison

            if mid_num == num:
                print(f"Car with mileage equal to {num} was found:")
                print(cars[mid])
                return cars[mid]  # Found the car with the given mileage
            elif mid_num < num:
                low = mid + 1
            else:
                high = mid - 1
        print(f"Car with {num} miles was not found")
        return None  # Mileage not found
  #Mathematical, Statistical, Business (next 4)
  def avg_price_for_brand(self, name):
        sum = 0
        count = 0
        for car in self._cars:
            if car[2] == name:
                sum = sum + int(car[1])
                count +=1
                avg = sum/count
        print(f"The average price for \"{name}\" cars is {round(avg,2)} $")
        return round(avg, 2)
    #print(avg_price_for_brand('ford'))

  def distribution_of_brand(self, year):
      brand = []
      for car in self._cars:
          if car[4] == str(year):
              brand.append(car[2])
      brand_unique = []
      count = []
      #create a list of brand
      for car in brand:
          if car not in brand_unique:
              brand_unique.append(car)
      #create a number of a specific brand was made in a specific year
      for car in brand_unique:
          a = brand.count(car)
          count.append(a)
      dic = dict(zip(brand_unique, count))
      print(f"{year} contains {len(dic)} car brands on sale:")
      print(dic)
      return dic
    
  def avg_price_for_brand_in_year(self, name, year):
        sum = 0
        count = 0
        for car in self._cars:
            if car[2] == name and int(car[4]) == year:
                sum = sum + int(car[1])
                count +=1
        avg = sum/count
        print(f'The average price of {name} in {year} is: {avg:.2f} $')
        return round(avg, 2)

  def change_in_price(self, name, year):
    year_price = self.avg_price_for_brand_in_year(name,year)
    avg = self.avg_price_for_brand(name)
    change = float(year_price)/float(avg) * 100
    print(f"The \"{name}\" cars changed in price by {round(change, 2)} % by {year}")
    return round(change, 2)
  
  def ModelonSale(self, model):
    counter = 0
    if self._cars:  
      for car in self._cars:
        if car[2] == model:
          counter += 1
    print(f"\"{model}\" {counter} cars on sale found")
    return counter
  
  
  def sortCars(self, key, order):
    if key in [0, 1, 4, 6]:
      if order == 'ascending':
        print(f"Sorted by {c.columnNames(key)}, {order}")
        return self.mergeSort(self._cars, key)
      else:
        print(f"Sorted by {c.columnNames(key)}, {order}")
        return self.mergeSort(self._cars, key)[::-1]
    if key in [2, 3]:
      if order == 'ascending':
        print(f"Sorted by {c.columnNames(key)}, {order}")
        return self.mergeSortForStr(self._cars, key)
      else:
        print(f"Sorted by {c.columnNames(key)}, {order}")
        return self.mergeSortForStr(self._cars, key)[::-1]
    
    
filename = "cars.csv" 
c = Cars(filename)

# c.createRow(new_car)
# c.outputFileRow(id)
# c.readRow(id)
# c.deleteRow(id)
# c.readFile(id)
# c.updateRow(20, new_car)
# c[20] = new_car
# c[20] = c[30]
# print(c[15])
# c.copyRow(id)
# c.outputSortedFile(c.sortCars(key, asc))
# print(c.priceSummarization(), "$")
# c.countCarByIndex(9, 'new jersey')
# print(c.ModelonSale("ford"),"$")
# print(c.avg_price_for_brand("ford"), "$")
# print(c.distribution_of_brand(2017))
# print(c.avg_price_for_brand_in_year('chevrolet', 2018), "$")
# print(c.change_in_price('chevrolet', 2018), "%")
# print(c.binary_search_by_year(1998))
# print(c.avg_price_for_brand_in_year('chevrolet', 2017), "$")


c.searchByMileage("9643")