from slicer import Slicer

#My list data
data = [
    200, 1230, 15, 2200, 5550
]
#2 is amount to split
data_slice = Slicer.cut(data, 2)
print(data_slice)


data = [
    {
        "foodname": "Ayam Bakar",
        "price": 12000
    }, 
    {
        "foodname": "Jus Mangga",
        "price": 7000
    },
    {
        "foodname": "Mie Goreng",
        "price": 9000
    },
    {
        "foodname": "Chicken Katsu",
        "price": 15000
    },
]
print(Slicer.cut(data, 2))