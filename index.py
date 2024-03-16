import pandas as pd

db = pd.read_csv('Base-de-datos-Sour-Roulette.csv')

description = db.describe()

print(db)
print(description)





# Promedio de "Cooperación entre jugadores" durante la partida 1
promedio_1_4 = db.loc[db.index < 4, "Cooperación entre jugadores"].mean()

# Promedio de "Cooperación entre jugadores" durante la partida 2
promedio_5_8 = db.loc[db.index >= 4, "Cooperación entre jugadores"].mean()

# Promedio de "Cooperación entre jugadores" de ambas partidas
promedio_total = (promedio_1_4 + promedio_5_8) / 2

print("Promedio de Cooperación entre jugadores durante la partida 1 (jugadores 1 al 4):", promedio_1_4)
print("Promedio de Cooperación entre jugadores durante la partida 2 (jugadores 5 al 8):", promedio_5_8)
print("Promedio total de Cooperación entre jugadores:", promedio_total)





# Jugador con mayor número de "Cooperación entre jugadores"
jugador_max_cooperacion = db[db["Cooperación entre jugadores"] == db["Cooperación entre jugadores"].max()]

# Número de "Interacciones positivas" del jugador con mayor número de "Cooperación entre jugadores"
interacciones_positivas_max_cooperacion = jugador_max_cooperacion["Interacciones positivas"].values[0]

print("Número de interacciones positivas gracias al mayor número de cooperación entre jugadores:", interacciones_positivas_max_cooperacion)





# Correlación entre el "# Rondas en dominar el juego" y "Cooperación entre jugadores"
correlacion = db["# Rondas en dominar el juego"].corr(db["Cooperación entre jugadores"])

print("Correlación entre '# Rondas en dominar el juego' y 'Cooperación entre jugadores':", correlacion)
# existe una relación positiva entre ambas variables, pero no es extremadamente fuerte.
# Es decir, mientras aumenta el número de rondas en dominar el juego,
# aumenta también la cooperación entre jugadores, pero no es una relación perfecta ni muy fuerte.





# Total de interacciones positivas y negativas
total_interacciones_positivas = db["Interacciones positivas"].sum()
total_interacciones_negativas = db["Interacciones negativas"].sum()

print("Total de interacciones positivas:", total_interacciones_positivas)
print("Total de interacciones negativas:", total_interacciones_negativas)

# Comparación entre interacciones positivas y negativas
if total_interacciones_positivas > total_interacciones_negativas:
    print("Hay más interacciones positivas que negativas. Esto nos indica que hubo más cooperación que competencia")
elif total_interacciones_positivas < total_interacciones_negativas:
    print("Hay más interacciones negativas que positivas. Esto nos indica que hubo más competencia que cooperación")
else:
    print("El número de interacciones positivas es igual al número de interacciones negativas.")





# Promedio de rondas en dominar el juego
promedio_rondas_dominando = db["# Rondas en dominar el juego"].mean()

print("Promedio de rondas en dominar el juego:", promedio_rondas_dominando)

# Número mínimo y máximo de rondas en dominar el juego
min_rondas = db["# Rondas en dominar el juego"].min()
max_rondas = db["# Rondas en dominar el juego"].max()

print("Número mínimo de rondas en dominar el juego:", min_rondas)
print("Número máximo de rondas en dominar el juego:", max_rondas)

# Mediana de rondas en dominar el juego
mediana_rondas = db["# Rondas en dominar el juego"].median()

print("Mediana de rondas en dominar el juego:", mediana_rondas)

# Comparación
if max_rondas - min_rondas > 0:
    print("El rango entre el mínimo y máximo de rondas dice que hubo una competencia alta.")
    if mediana_rondas > promedio_rondas_dominando:
        print("La mediana de rondas es mayor que el promedio, por ende hubo competencia más reñida.")
    elif mediana_rondas < promedio_rondas_dominando:
        print("La mediana de rondas es menor que el promedio, por ende hubo menos competencia.")
    else:
        print("La mediana de rondas es igual al promedio.")
else:
    print("El mínimo y máximo de rondas en dominar el juego es el mismo, por ende la competencia fue pareja.")

