"""
Python > 3.10.0
github.com/t4lesss 

# Algoritmo: Gerador de password.
# Algorithm: Password generator.


"""

import secrets;
import pytholino as p;


def genPassword(min_len=8, hnumbers=True, hsymbols=True):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789";
        symbols = "!@#$%&*()_+-=:./<>?";

        chars = letters + digits + symbols;

        pwd_len = min_len;
        
        while True:
            pwd = '';

            num_symbols = 0;
            num_digits = 0;
        
            for i in range(min_len):
        
                # Para efeitos de demonstração, resolvi criar duas maneiras de gerar a senha.
                # For demonstration purposes, I decided to create two ways to generate the password.

                # Se a senha for menor que 10 caracteres, adicionar caracteres aleatórios com base em um random em uma lista com tipo de caracteres.
                # If the password is less than 10 characters, add random characters based on a random in a list with character type.

                # Se a senha for igual ou maior que 10, adicionar caracteres aleatórios com base em random nos indices da string chars.
                # If the password is equal to or greater than 10, add random characters based on random in the indices of the chars string.

                if pwd_len < 10:
                    chartype_list = secrets.choice(['letter', 'digit', 'symbol'])
                    if chartype_list == 'letter':
                        pwd += ''.join(secrets.choice(letters));
                    elif chartype_list == 'digit':
                        pwd += ''.join(secrets.choice(digits));
                        num_digits += 1
                    else:
                        pwd += ''.join(secrets.choice(symbols));
                        num_symbols += 1
                else:
                    pwd += ''.join(secrets.choice(chars))
                    if pwd[-1] in symbols:
                        num_symbols += 1
                    elif pwd[-1] in digits:
                        num_digits += 1


            # Verifica se a senha atende aos requisitos de complexidade.
            # Checks if the password meets the complexity requirements.
            if pwd_len >= 10 and (num_symbols + num_digits) / pwd_len >= 0.3:
                break

            if pwd_len < 10 and (num_symbols + num_digits) >= 3:
                break

        return pwd



if __name__ == "__main__":
    p.p(f'Senha gerada: {genPassword(min_len=8)}');

