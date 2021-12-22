# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

medida = float(input("Digite a distancia em metros: "))
dm = medida * 10 #decimetro
cm = medida * 100 #centimetro
mm = medida * 1000 # milimetro
print("A medida de {}m corresponde a {:.0f}dm, {:.0f}cm e {:.0f}mm e ".format(medida, dm, cm, mm))
# nenhuma casa decimal após "." na medida dm, cm e mm
km = medida / 1000 # quilômentro
hm = medida / 100 # hectômetro
dam = medida / 10 # decâmetro
print("A medida de {}m corresponde a {}km, {}hm e {}dam ".format(medida, km, hm, dam))