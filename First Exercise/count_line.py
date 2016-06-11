
# coding: utf-8

# In[ ]:

def count_line(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(count_line("C:\\Users\\c.dottorelli\\Airport-Test\\Data\\bookings.csv"))
print(count_line("C:\\Users\\c.dottorelli\\Airport-Test\\Data\\searches.csv"))


# In[ ]:



