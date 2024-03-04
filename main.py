import Inheritance as i
import ReadingFiles as r
import WritingFiles as w
# check push

tv = i.Product("TV", 1000, True)
dog = i.Dog()
print(dog.speak())

things = [i.Dog(), i.Cat(), i.Animal()]

for animal in things:
    print(animal.speak())

x = r.example()
y = w.example()




