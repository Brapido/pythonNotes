import Inheritance as i
import ReadingFiles as r
import WritingFiles as w
import CSVFiles as c
# check push

tv = i.Product("TV", 1000, True)
dog = i.Dog()
print(dog.speak())

things = [i.Dog(), i.Cat(), i.Animal()]

for animal in things:
    print(animal.speak())

x = r.example()
y = w.menu()
z = c.menu()



