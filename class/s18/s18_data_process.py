FILENAME = "children-per-woman-UN.csv"
file = open(FILENAME)
entire_file = file.read()
lines = entire.splitlines()
def get_country_max_birth_rate(country,lines):
max_rate = 0
may_year_rate = 0
for line in lines:
    if line.lower().find("iran") != -1 :
        tokens = line.split("")
        rate = float(tokens[3])
        year = int(tokens[2])
        if rate > max_rate:
            max_rate = rate
            max_rate_year = year

