from discord.ext import commands
from discord import app_commands
import discord
import random
from database import Score

db = Score() #initialising the class Score 

class quizCommands(commands.GroupCog, name="quiz"):
 def __init__(self, bot):
        self.bot = bot


   # Creating a slash command which provides a random quote 
 @app_commands.command(name="filmquote", description = "provides a film quote")
 async def filmquote(self, interaction: discord.Interaction):
    with open("filmQuotes.txt", "r") as file:
        quotes = file.readlines()
        quotes_length = (int(len(quotes))-1)
        random_number = random.randint(0,quotes_length)
        random_line = quotes[random_number]
    await interaction.response.send_message(f" Hey {interaction.user.mention}! here is a a film quote:\n {random_line}")

    # Creating a quiz game slash command 
 @app_commands.command(name="game", description="Film quiz, asks user question and checks if it's correct")
 async def game(self, interaction: discord.Interaction):
    def check(m):
        return m.author == interaction.user and m.channel == interaction.channel

    with open("triviaQuestions.txt", "r") as file:
        data = file.readlines()
        random_question = random.choice(data)

    await interaction.response.send_message(f"Hey {interaction.user.mention}! Here is a question: {random_question}")
    userGuess = await self.bot.wait_for('message', check=check)

    with open("triviaAnswers.txt", "r") as file:
        answers = file.readlines()
        random_answer = answers[data.index(random_question)].strip()  # Ensures matching question-answer pair

    if userGuess.content.lower() == random_answer.lower():
        await interaction.followup.send("You got the right answer!")
        db.add_table(interaction.user.mention)
    else:
        await interaction.followup.send("Your answer is wrong.")


    # Creating a slash command which shows all scores 
 @app_commands.command(name="showscores", description="Shows all scores")
 async def showscores(self, interaction: discord.Interaction):
     await interaction.response.send_message(f"Hey {interaction.user.mention}! Here are the scores:\n **USER**\t\t\t\t\t\t\t**SCORE** \n {db.show_all_scores()}")
     

   #creating a slash command which deletes all scores
 @app_commands.command(name="clearscores", description="Delete all scores")
 async def clearscores(self, interaction: discord.Interaction):
     def check(m):
        return m.author == interaction.user and m.channel == interaction.channel
     await interaction.response.send_message(f"Hey {interaction.user.mention}! Are you sure you want to clear all scores? (yes/no)")
     userResponse = await self.bot.wait_for('message', check=check)
     if userResponse.content.lower() == "yes":
         db.delete_all_scores()
         await interaction.followup.send("The scores have been cleared!")
     elif userResponse.lower() == "no":
         await interaction.followup.send("The scores have not been cleared!")
     else:
         await interaction.followup.send("If you want to delete all scores please reselect the command and enter yes,\n if not resume playing.")
         
         

    
     

    
