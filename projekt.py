import easygui as eg
import matplotlib.pyplot as plt
import numpy as np

sisend=eg.enterbox(msg="Sisesta funktsioon\n(sisesta sama moodi nagu moodle testi) \n\n f(x)=...", title="Funktsioon")

#teisendan kasutaja sisendi programmile arusaadavale kujundlie

arc=["arctan","arccos", "arcsin"]
for i in arc:
    if i in sisend:
        sisend=sisend.replace(i, f"np.{i}")

trigo=["sin", "cos", "tan"]
for i in trigo:
    if i in sisend:
        sisend=sisend.replace(i, f"np.{i}")
        
sisend=sisend.replace("arcnp.", "arc")

if "log" in sisend:
    sisend=sisend.replace("log", "np.log10")
if "ln" in sisend:
    sisend=sisend.replace("ln", "np.log")

#määran maksimaalsed x-i väärtused koordinaatteljestikul, number 1000 näitab punktide arvu, mille põhjal fn on joonestatud
x=np.linspace(-10, 10, 1000)

#defineerin funktsiooni f(x), mis võtab argumendiks kasutaja sisendi
def f(x):
    return eval(sisend)

#annan kordinaatteljestikule x ja y telje
ax=plt.gca()
ax.spines["top"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.grid(True, which='both', linestyle="--")
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')


#annan x ja y teljele nooled
nooled = dict(markersize=4, color='black', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **nooled)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **nooled)



plt.plot(x, f(x))
plt.show()