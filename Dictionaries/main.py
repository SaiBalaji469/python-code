
# print(mobile["brand_name"])
# mobile["Wifi"] = "On"
# print(mobile)


# The items() method returns a view object. The view object contains the key-value pairs
#  of the dictionary, as tuples in a list.
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# x = mobile.items()
# print(x)







# The keys() method returns a view object. The view object contains the
# keys of the dictionary, as a list.
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# x = mobile.keys()
# print(x)





# The values() method returns a view object. The view object contains the
# values of the dictionary, as a list.
#The view object will reflect any changes done to the dictionary
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# x = mobile.values()
# print(x)



#The pop() method removes the specified item from the dictionary.
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# mobile.pop("model_num")
# print(mob
# ile)



#The popitem() method removes the item that was last inserted into the dictionary.
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# mobile.popitem()
# print(mobile)



# The clear() method removes all the elements from a dictionary.
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# mobile.clear()
# print(mobile)



# The copy() method returns a copy of the specified dictionary.
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# x = mobile.copy()
# print(x)


# The get() method returns the value of the item with the specified key.
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# x = mobile.get("price")
# print(x)




# The setdefault() method returns the value of the item with the specified key.
#  If the key does not exist, insert the key, with the specified value
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# x = mobile.setdefault("Wifi","On")
# print(mobile)




# The update() method inserts the specified items to the dictionary.
# The specified items can be a dictionary, or an iterable object with key value pairs.
# mobile = {"brand_name":"apple","model_num": 14,"price":1.1}
# mobile.update({"wifi":"On"})
# print(mobile)




# from keys - The fromkeys() method returns a dictionary with the specified keys and
#              the specified value.
x = {"key1","key2"}
y = 0
this_dict = dict.fromkeys(x,y)
print(this_dict)




