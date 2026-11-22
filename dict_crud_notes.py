## Read
## example of dict.get()
print ('----------------- Read ------------------')
item_list = {'name': 'Monitor', 'stock': 4, 'price': 200}
if item_list.get('stock1', 0) > 0: 
  item_list['price'] = item['price'] * 0.9
print(item_list)
print(item_list.get('stock1', "not found"))
# not stock1, so "not found" rather than standard 'None' output

## 2nd method
print(item_list['name'])
# Throws 'KeyError' when unknown key is used.
# print(item['name1'])
# KeyError: 'name1'

## Update
print ('----------------- Update ------------------')
## example of dict.setdefault()
store = {'apples': 10, 'orange': 5} 
val = store.setdefault('apples', 25) 
# doesn't change value of already existing key
val2 = store.setdefault('pineapples', 25) 
# create new key value pair
print(store['apples'])
print(val)
print(val2)
store.setdefault('coconut', 35) 
# no need of variable assignment, it update directly to the dictionary 'store'

## 2nd methood --> using assignment operator/ square brackets
store['orange'] = 10
store['kiwi'] = 5
print(store)

## 3rd method --> using update() method
store.update({'banana':6, 'cranberry':150})
print(store)

print ('----------------- Delete ------------------')
store.pop("coconut")
print(store)
status = store.pop("mango", "not found")
print(status)

print ('----------------- Key and Values check ------------------')
# list the keys
item_list.keys()
print(store.keys())

keys_used = item_list.keys()
print(type(keys_used))
print(type(store))

#list the values
print(item_list.values())
print(store.values())

print('--------------------- unpacking -------------------')
#list key value pair 
# Usecase: for unpacking
data = item_list.items()
print(store.items())
print(type(data))
print(data)
for var in data:
  detail, value = var
  print(f"detail: {detail}, value: {value}")

print('---------------- duplicate keys ------------------')

fruits = {'apple': 10, 'kiwi': 10, 'apple': 25, 'coconut': 35, 'kiwi': 5}
print(fruits)
# Duplicate keys are replaced with the latest values

print('--------------------- Others -------------------')
# key type other than string 
dict2 = { 1: "name", 2.2: "type", 1: "james"}
print(dict2)
print(type(dict2))
print(dict2.get(1))
print(dict2.get(2.2))
print(dict2[1])


 