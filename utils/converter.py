# class PhoneDetail:
#
#     def __init__(self, area_code, country, country_code,):
#         self.area_code = area_code
#         self.country = country
#         self.country_code = country_code
#
#     def __str__(self):
#         return "{'country'}"

fx = open("codex.py", mode="w")
i = 0
result = []
with open("countrycode.csv", mode="r") as f:

    while True:
        if i == 1:
            details = f.readline().split('",')

            if len(details) == 1:
                break           # end of task

            data = {"country": details[0].strip('"'),
                    "country_repr": details[1].strip('"'),
                    "area_code": [c.strip('" ') for c in details[8].split(',')]
                    }
            result.append(data)
        else:
            f.readline()
            print("Header info")
            i = 1


print(result)
fx.writelines(str(result))
fx.close()