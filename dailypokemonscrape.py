
import requests
from bs4 import BeautifulSoup
from random import choice
import smtplib
from time import sleep

while True:  # Do not spam websites
  website = "https://pokemondb.net/pokedex/"
  pokemondb = requests.get("https://pokemondb.net/pokedex/national")
  main_soup = BeautifulSoup(pokemondb.content, "html.parser")
  pokemons = main_soup.findAll("a", attrs={"class":"ent-name"})
  pokemon_list = pokemons
  daily_pokemon = str(choice(pokemon_list).text)
  daily_website = website + daily_pokemon
  pokemondb_pokemon = requests.get(daily_website)
  pokemon_soup = BeautifulSoup(pokemondb_pokemon.content, "html.parser")
  information = pokemon_soup.findAll("div", attrs={"class":"grid-col span-md-6 span-lg-8"})
  pokemon_name = information[0].text.split()[0]

  news_website = requests.get("https://pokemondb.net/")
  news_soup = BeautifulSoup(news_website.content, "html.parser")
  news_title = news_soup.findAll("h2")
  news_date = news_soup.findAll("p", attrs={"class":"pull-up text-muted"})
  news = news_soup.findAll("div", attrs={"class":"grid-col span-md-8"})
  info = ""
  news_info = ""

  for n in news:
    news_info += n.text.strip().split("Continue reading")[0]
    break

  for i in information:
    info += i.text.strip()

  info = info.replace("é", "e")
  news_info = news_info.replace("é", "e")
  news_info = news_info.replace("—", "-")


  message = "**Your daily Pokemon is " + pokemon_name + "!** " + "\n\nDid you know that " + info + "\n\n\n**YOUR NEWS!**\n\n" + news_info + "\n\n Find more information here: [Pokemon Net](https://pokemondb.net/)"
  print(message)


  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login("[gmail-account-sending-emails]@gmail.com", "[google API login code to email]")
  server.sendmail("[gmail-account-sending-emails]@gmail.com", "target-email-inbox@gmail.com", message)
  server.quit()
  sleep(24 * 60 * 60)