def hello(to):
    print("hello,", to)


    print("===Welcome to calculator!===")

# Ask user to user for hello 
name = input( "What's your name?" ).strip().title().capitalize().title().strip()

hello (name)

# Split last name user 
first, last = name.split(" ")


# Say hello to first name user 
print(f" halo, {first}!")


# Small calculator

x = float (input("whats x ? "))
y = float (input("whats y ? "))

z = round(x * y)

print(f"{z:,}" )

print("Thanks for run the program!")
