import discord
from discord.ext import commands
import random

prefix = "."

token = "A"

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is online and ready to use")

#gold-FFFB00
#purple-FFFB00
#redish-FF0078
@bot.command()
async def roulette(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 36:
        predictions = ['red','red','red','purple','purple','purple','gold']
        prediction = random.choice(predictions)
        if prediction == 'red':
            embed_color = 0xFF0036
            color_text = 'Red'
            prediction = ":red_square:"
        elif prediction == 'purple':
            embed_color = 0xAE00FF
            color_text = 'Purple'
            prediction = ":purple_square:"
        elif prediction == 'purple':
            embed_color = 0xFFFB00
            color_text = 'Gold'
            prediction = ":yellow_square:"
        em = discord.Embed(color=embed_color)
        em.add_field(name="Roulette Predictor", value=color_text + "\n" + prediction)
        em.set_footer(text="Buy @ .gg/uMzgayuD")
        await ctx.send(embed=em)
    else:
        await ctx.send("Invalid round id")






@bot.command()
async def mines(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await ctx.send("Invalid round id")
    elif round_length == 36:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:'
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        if a == 1:
            mine1 = ":white_check_mark: "
        elif a == 2:
            mine2 = ":white_check_mark: "
        elif a == 3:
            mine3 = ":white_check_mark: "
        elif a == 4:
            mine4 = ":white_check_mark: "
        elif a == 5:
            mine5 = ":white_check_mark: "
        elif a == 6:
            mine6 = ":white_check_mark: "
        elif a == 7:
            mine7 = ":white_check_mark: "
        elif a == 8:
            mine8 = ":white_check_mark: "
        if b == 9:
            mine9 = ":white_check_mark: "
        elif b == 10:
            mine10 = ":white_check_mark: "
        elif b == 11:
            mine11 = ":white_check_mark: "
        elif b == 12:
            mine12 = ":white_check_mark: "
        elif b == 13:
            mine13 = ":white_check_mark: "
        if c == 14:
            mine14 = ":white_check_mark: "
        elif c == 15:
            mine15 = ":white_check_mark: "
        elif c == 16:
            mine16 = ":white_check_mark: "
        elif c == 17:
            mine17 = ":white_check_mark: "
        if d == 18:
            mine18 = ":white_check_mark: "
        elif d == 19:
            mine19 = ":white_check_mark: "
        elif d == 20:
            mine20 = ":white_check_mark: "
        elif d == 21:
            mine21 = ":white_check_mark: "
        elif d == 22:
            mine22 = ":white_check_mark: "
        elif d == 23:
            mine23 = ":white_check_mark: "
        elif d == 24:
            mine24 = ":white_check_mark: "
        elif d == 25:
            mine25 = ":white_check_mark: "
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        info = str(random.randint(45, 90))
        pfp = 'https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657'
        em = discord.Embed(color=0x11F1D3)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Star Predictor")
        em.add_field(name="Star Predictor",value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n" + "**Accuracy**" + "\n" + info +"%")
        await ctx.reply(embed=em)


@bot.event
async def on_ready():
    print("Bot is online and ready to use")

@bot.command()
async def towers(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36: 
        await ctx.send("Invalid round id")
    elif round_length == 36:
        tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = ":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:"
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)
        e = random.randint(1, 3)
        f = random.randint(1, 3)
        g = random.randint(1, 3)
        h = random.randint(1, 3)

        if a == 1:
            tower1 = ":star:"
        elif a == 2:
            towe2 = ":star:"
        elif a ==3:
            tower3 = ":star:"
        if b == 1:
            tower4 = ":star:"
        elif b == 2:
            tower5 = ":star:"
        elif b ==3:  
            tower6 = ":star:"
        if c == 1:
            tower7 = ":star:"
        elif c == 2:
            tower8 = ":star:"
        elif c ==3:
            tower9 = ":star:"
        if d == 1:
            tower10 = ":star:"
        elif d == 2:
            tower11 = ":star:"
        elif d ==3:
            tower12 = ":star:"
        if e == 1:
            tower13 = ":star:"
        elif e == 2:
            tower14 = ":star:"
        elif e ==3:
            tower15 = ":star:"
        if f == 1:
            tower16 = ":star:"
        elif f == 2:
            tower17 = ":star:"
        elif f ==3:
            tower18 = ":star:"
        if g == 1:
            tower19 = ":star:"
        elif g == 2:
            tower20 = ":star:"
        elif g ==3:
            tower21 = ":star:"
        if h == 1:
            tower22 = ":star:"
        elif h == 2:
            tower23 = ":star:"
        elif h ==3:
            tower24 = ":star:"

        row1 = tower1 + tower2 + tower3
        row2 = tower4 + tower5 + tower6
        row3 = tower7 + tower8 + tower9
        row4 = tower10 + tower11 + tower12
        row5 = tower13 + tower14 + tower15
        row6 = tower16 + tower17 + tower18
        row7 = tower19 + tower20 + tower21
        row8 = tower22 + tower23 + tower24
        #await ctx.send(row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8)
        info = str(random.randint(45, 95))
        pfp = 'https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657'
        list = [0xFF0000, 0x00FF2E, 0x000FFF, 0xF700FF]
        color = random.choice(list)
        em = discord.Embed(color=color)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Buy @ .gg/uMzgayuD")
        em.add_field(name="Towers Predictor", value=row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8 + "\n" + "**Accuracy**" + "\n" + info + "%")   
        await ctx.send(embed=em)







bot.run('MTAyMDc5OTIzODA4MDMxOTYwMA.GZixPX.MnzNYSk6sy4vuJmdmbQy7Wiaxj7yHI3fB4DpmY')
