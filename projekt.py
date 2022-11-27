import easygui as eg
import matplotlib.pyplot as plt
import numpy as np
import math as math

#annan kordinaatteljestikule x ja y telje
ax=plt.gca()
ax.spines["top"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.grid(True, which='both', linestyle="--")
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

#määran maksimaalsed x-i väärtused koordinaatteljestikul, number 1000 näitab punktide arvu, mille põhjal fn on joonestatud
x=np.linspace(-10, 10, 1000)

#annan x ja y teljele nooled
nooled = dict(markersize=4, color='black', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **nooled)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **nooled)


juhend="Sisesta funktsioon\n(sisesta sama moodi nagu moodle testi) \n ruutjuure asemel astanda 1/2)"
title="Funktsioon"
input_list=["f(x)=", "g(x)="]
kõik_sisend=eg.multenterbox(juhend, title, input_list)

#ükshaaval teisendan kasutaja sisendid sobivale kujule ja teen graafiku
try:
    for i in range(len(kõik_sisend)):
        sisend=kõik_sisend[i]
        
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
              

        #defineerin funktsiooni f(x), mis võtab argumendiks kasutaja sisendi
        def f(x):
            return eval(sisend)
        plt.plot(x, f(x))
    
except:
    None
    
plt.show()