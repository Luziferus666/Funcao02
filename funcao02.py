# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.
def calcular_area_base(raio):
    return 3.14 * raio ** 2  

def calcular_volume_cilindro(raio, altura):
    return calcular_area_base(raio) * altura  

raio = float(input("Digite o raio do círculo: "))
altura = float(input("Digite a altura do cilindro: "))

print(f"Área da base do círculo: {calcular_area_base(raio):.2f}")
print(f"Volume do cilindro: {calcular_volume_cilindro(raio, altura):.2f}")