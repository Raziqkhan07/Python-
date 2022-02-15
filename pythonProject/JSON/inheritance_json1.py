import json
class Person:

    with open("arraySample.json", "w") as p:
            json.dump(var, p)
            print(repr(p))
            print(type(p))
 var = {
            "Subjects": {
                "Maths": 85,
                "English": 90
            }
        }
