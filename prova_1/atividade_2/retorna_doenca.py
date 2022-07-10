#este arquivo é um complementro para o questoes_2

def taxa(imc, sexo):
#comparo sexo pois imc varia de homem e mulger
    if sexo == "M":
        diagnostico = None

        if imc < 18.5:
            diagnostico = "desnutrição"
        elif imc < 24.9:
            diagnostico = "eutrofia"
        elif imc < 29.9:
            diagnostico = "sobrepeso"
        elif imc < 34.9:
            diagnostico = "Obesidade Grau I"
        elif imc < 39.9:
            diagnostico = "Obesidade Grau II(severa)"
        elif imc < 40:
            diagnostico = "Obesidade Grau III(mórbida)"

        print(f"o diagnostico do paciente é: {diagnostico}")

        return diagnostico

    elif sexo == "F":

        diagnostico = None

        if imc < 19:
                diagnostico = "desnutrição"
        elif imc < 23.9:
                diagnostico = "sobrepeso"
        elif imc < 28.9:
                diagnostico = "Obesidade Grau I"
        elif imc < 38.9:
                diagnostico = "Obesidade Grau II(severa)"
        elif imc < 39:
                diagnostico = "Obesidade Grau III(mórbida)"

        print(f"o diagnostico do paciente é: {diagnostico}")

        return diagnostico