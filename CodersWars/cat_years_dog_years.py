# I have a cat and a dog.
#
# I got them at the same time as kitten/puppy. That was humanYears years ago.
#
# Return their respective ages now as [humanYears,catYears,dogYears]
#
# NOTES:
#
# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

def human_years_cat_years_dog_years(human_years):

    cat = 0
    dog = 0
    year = 1
    while year <= human_years:
        if year == 1:
            cat += 15
            dog += 15
        elif year == 2:
            cat += 9
            dog += 9
        else:
            cat += 4
            dog += 5
        year += 1
    return [human_years, cat, dog]


print(human_years_cat_years_dog_years(10))