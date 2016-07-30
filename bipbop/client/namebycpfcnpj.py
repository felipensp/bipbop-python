# BIPBOP

import bipbop.client.cpfcnpj
import bipbop

class NameByCPFCNPJ:
    def evaluate(cpfcnpj, birthday, apikey):
        if validate_cpf(cpfcnpj):
            if birthday is None:
                raise bipbop.client.Exception("É necessário a data de nascimento para consultar um CPF.")
        elif validate_cnpj(cpfcnpj):
            pass
        else:
            raise bipbop.client.Exception("O documento informado não é um CPF ou CNPJ válido.")

        ws = bipbop.client.WebService()
        ws.post("SELECT FROM 'BIPBOPJS'.'CPFCNPJ'",
            {
                'documento': cpfcnpj,
                'nascimento': birthday
            })
            
        
    evaluate = staticmethod(evaluate)

