
class Car:
    #brand='MyBrand'
    #model='MyModel'
    #price_normal=50
    price_offert=None

    def __init__(self, brand, model, price_normal) -> None:
        self.brand = brand
        self.model = model
        self.price_normal = price_normal

    
    def getCompleteDescription(self):
        return f'{self.brand} - {self.model}'

    def getPrice(self):
        if self.price_normal is None:
            return { 'price':self.price_offert, 'type':'offert' }
        
        return { 'price':self.price_normal, 'type':'normal' }

car = Car('Tesla', 'V1', 50)
car.brand='Tesla-2'

car.getCompleteDescription()

print(car.getCompleteDescription())

print(car.brand)
