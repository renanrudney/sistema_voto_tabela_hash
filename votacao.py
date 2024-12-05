# Votacao - Renan Rudney

class SistemaVotacao:
    def __init__(self):
        self.eleitores = set()
        self.votos = {}

    def votar(self, id_eleitor, candidato):
        if id_eleitor in self.eleitores:
            return "Erro: Eleitor já votou."
        
        self.eleitores.add(id_eleitor)
        
        if candidato not in self.votos:
            self.votos[candidato] = 0
        self.votos[candidato] += 1
        
        return f"Voto registrado para {candidato}!"

    def exibir_resultados(self):
        if not self.votos:
            return "Nenhum voto registrado ainda."
        
        resultados = "Resultado da Eleição:\n"
        for candidato, total_votos in self.votos.items():
            resultados += f"{candidato}: {total_votos} votos\n"
        
        return resultados.strip()



sistema = SistemaVotacao()

print(sistema.votar("123", "Alice"))  # "Voto registrado para Alice!"
print(sistema.votar("123", "Bob"))    # "Erro: Eleitor já votou."
print(sistema.votar("456", "Alice"))  # "Voto registrado para Alice!"
print(sistema.exibir_resultados())
