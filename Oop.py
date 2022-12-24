# Oop = objet oriented programs 

# class is like a template blueprint out of which we can create multiple objects
# blueprint contains structure 
# from a temp we can create diff values and behaviours
class laptop:

    def config(self):
        print("Asus","i7","1tb")

laptop1=laptop()
laptop2=laptop()
print(id(laptop1))
print(id(laptop2))
laptop1.config()


