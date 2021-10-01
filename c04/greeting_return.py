def greet(lang="en"):
    if lang == "es":
        return("Hola")
    elif lang == "fr":
        return("Bonjour")
    else:
        return("Hello")

print(greet("en"), "Glenn")
print(greet("fr"), "Michael")
print(greet("es"), "Sally")
print(greet(), "Dr.Chuck")
