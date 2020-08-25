import requests
import pyfiglet as fig
import termcolor
from random import choice





def dad_jokes():

    welcome_ascii = fig.figlet_format("DAD JOKE 3000")
    color_welcome = termcolor.colored(welcome_ascii, color="red", attrs=["blink"])

    print(color_welcome)

    print("We haz jokes")

    look_up_sub = input("What kind of joke do you want me to look up? ")

    #how_many = input("How many do you want? Please type your answer in numeric values: ")

    #num = int(how_many)
    sub_low = look_up_sub.lower()

    url = "https://icanhazdadjoke.com/search?"

    res = requests.get(
        url,
        headers={"Accept":"application/json"},
        params={"term":sub_low}
        ).json()


    num_jokes = res["total_jokes"]
    results = res["results"]
    if num_jokes > 1:
        print(f"I found {num_jokes} jokes about {look_up_sub} here is one: ")
        print(choice(results)["joke"])
    elif num_jokes == 1:
        print(f"I found only one joke about {look_up_sub} here it is: ")
        print(results[0]["joke"])
    else:
        print(f"Sorry i could not find a joke with your search term {look_up_sub}")
 
dad_jokes()
