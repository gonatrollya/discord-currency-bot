import discord
from discord.ext import commands
import sqlite3
client = commands.Bot(command_prefix = '!')
@client.command(pass_context=True)
@client.event
async def on_ready():
    print('bot is ready')


@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)



@client.command(pass_context=True)
async def balance(ctx, *arg):
    currencyamount = arg[-1]
    arg = arg[:-1]
    membername = ''
    currentbalance= ''
    for argument in arg:
        membername += str(argument) + ' '
    print(membername)
    membername = "'" + membername
    membername = membername + "'"
    print(membername)
    conn = sqlite3.connect('currency_store.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS currency(user STR, balance INT)")
    c.execute("SELECT balance FROM currency WHERE user = ?", (membername,))
    currentbalance = c.fetchall()
    currentbalance = str(currentbalance)
    currentbalance = currentbalance[2:-3]
    if currentbalance == '':
        await client.say('that person isnt in the database')
    else:
        await client.say('that persons balance is')
        await client.say(currentbalance)


@client.command(pass_context=True)
@commands.has_role('currency')
async def insert(ctx, *arg):
    arg = arg[:-1]
    membername = ''
    currentbalance= ''
    for argument in arg:
        membername += str(argument) + ' '
    membername = "'" + membername
    membername = membername + "'"
    print(membername)
    conn = sqlite3.connect('currency_store.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS currency(user STR, balance INT)")
    if membername == "''":
        await client.say("incorrect formatting, you have to @ the person twice")
        await client.say()
    if currentbalance == '':
        await client.say('checking databse')
        c.execute("SELECT balance FROM currency WHERE user = ?", (membername,))
        currentbalance = c.fetchall()
        currentbalance = str(currentbalance)
        currentbalance = currentbalance[2:-3]
        if currentbalance == '':
            await client.say("adding user to database")
            c.execute("INSERT INTO currency VALUES(?,0)",(membername,))
            conn.commit()
            await client.say("added user to database")
        else:
            await client.say("user is already in the database")
    else:
        await client.say("oopsy, that person is in the database")




@client.command(pass_context=True)
@commands.has_role('currency')
async def give(ctx, *arg):
    currencyamount = arg[-1]
    arg = arg[:-1]
    membername = ''
    currentbalance= ''
    for argument in arg:
        membername += str(argument) + ' '
    print(membername)
    membername = "'" + membername
    membername = membername + "'"
    print(membername)
    conn = sqlite3.connect('currency_store.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS currency(user STR, balance INT)")
    c.execute("SELECT balance FROM currency WHERE user = ?", (membername,))
    currentbalance = c.fetchall()
    currentbalance = str(currentbalance)
    currentbalance = currentbalance[2:-3]
    if currentbalance == '':
        await client.say('uhhh, that person isnt in the database')
    currentbalance = int(currentbalance)
    currencyamount = int(currencyamount)
    currentbalance = currentbalance + currencyamount
    await client.say('new balance')
    await client.say(currentbalance)
    c.execute("UPDATE currency SET balance = ? WHERE user =?",(currentbalance,membername,))
    conn.commit()
    await client.say("balance successfully updated")


@client.command()
async def broken():
    await client.say('im sorry, im trying my best')
    await client.say(person)
client.run('TOKEN')
