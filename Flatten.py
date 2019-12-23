import pprint


def flatten(dictionary):
    flatDictionary = {}
    Helper("", dictionary, flatDictionary)
    return flatDictionary


def Helper(initialKey, dictionary, flatDictionary):
    for key in dictionary:
        if not isinstance(dictionary[key], dict):
            if (initialKey == None or initialKey == ""):
                flatDictionary[key] = dictionary[key]
            else:
                flatDictionary[initialKey + "." + key] = dictionary[key]
        else:
            if (initialKey == None or initialKey == ""):
                Helper(initialKey + key, dictionary[key], flatDictionary)
            else:
                Helper(initialKey + "." + key, dictionary[key], flatDictionary)

    # import collections
    # obj = collections.OrderedDict()
    # join = "."

    # def checkProperties(mapper, parent=""):
    #     if isinstance(mapper, dict):
    #         for key, value in mapper.items():
    #             checkProperties(value, parent + join + key if parent else key)
    #     else:
    #         obj[parent] = mapper

    # checkProperties(dictionary)

    # return dict(obj)


dictionary = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

pprint.pprint(flatten(dictionary))


# def flatten_dictionary(dictionary):
#     import collections

#     if dictionary == {}:
#         return {}

#     output = {}

#     for akey in dictionary:
#         if isinstance(dictionary[akey], dict) == False:
#             output[akey] = dictionary[akey]
#         else:
#             output = helper(akey, dictionary[akey], output)

#     return output

#     pass  # your code goes here

# # expand key that has dictionary as value


# def helper(akey, toExpand, output):
#     '''
#       originalKey = akey = 'Key2'
#       newkey = 'a'
#     '''
#     originalKey = akey  # might not need this ---

#     for newkey in toExpand:
#         # NOT a dictionary
#         if isinstance(toExpand[newkey], dict) == False:
#             # check if newkey is empty
#             if newkey == '':
#                 output[originalKey] = toExpand[newkey]
#             else:
#                 output[originalKey + '.' + newkey] = toExpand[newkey]
#             # print(output)
#         # IS a dictionary
#         else:
#             output = helper(akey + '.' + newkey, toExpand[newkey], output)

#     return output


# test = {
#     "Key1": "1",
#     "Key2": {
#         "a": "2",
#         "b": "3",
#         "c": {
#             "d": "3",
#             "e": {
#                 "": "1"
#             }
#         }
#     }
# }

# print(flatten_dictionary(test))

# '''
# for key, value in flatten_dictionary(test).items():
#     print(key, value)

# '''


# def flatten_dictionary(dictionary):

#     if dictionary == {}:
#         return {}

#     output = {}

#     for akey in dictionary:
#         if isinstance(dictionary[akey], dict) == False:
#             output[akey] = dictionary[akey]
#         else:
#             output = helper(akey, dictionary[akey], output)

#     return output

#     pass  # your code goes here

# # expand key that has dictionary as value


# def helper(akey, toExpand, output):
#     '''
#       originalKey = akey = 'Key2'
#       newkey = 'a'
#     '''
#     originalKey = akey  # might not need this ---

#     for newkey in toExpand:
#         # NOT a dictionary
#         if isinstance(toExpand[newkey], dict) == False:
#             # check if newkey is empty
#             if newkey == '':
#                 output[originalKey] = toExpand[newkey]
#             else:
#                 output[originalKey + '.' + newkey] = toExpand[newkey]
#             # print(output)
#         # IS a dictionary
#         else:
#             output = helper(akey + '.' + newkey, toExpand[newkey], output)

#     return output


# test = {
#     "Key1": "1",
#     "Key2": {
#         "a": "2",
#         "b": "3",
#         "c": {
#             "d": "3",
#             "e": {
#                 "": "1"
#             }
#         }
#     }
# }
# print(flatten_dictionary(test))
