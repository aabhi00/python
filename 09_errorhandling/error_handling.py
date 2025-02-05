file = open('yuotube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()
# same can be done as
with open('youtube.txt' , 'w') as file:
    file.write('chai aur python')