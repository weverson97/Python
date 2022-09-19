"""
Autor: Weverson Jose da Silva

3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes.
Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos,
solicitou que você criasse um sistema capaz de atender ao seguinte requisito:
    o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49)
    e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50).

    O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a
    maior nota.
    Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das
    notas deve ser exibida uma mensagem no seguinte padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

"""
alunos = 51
alunos_turma = (alunos - 1) / 2

impar_nota_acc = 0
impar_nota_maior = 0
impar_aluno_nota_maior = 0

par_nota_acc = 0
par_nota_maior = 0
par_aluno_nota_maior = 0

for i in range(1, alunos, 2):
    impar = float(input(f"Você está digitando as notas dos alunos IMPARES. Por favor, insira a nota do aluno de numero {i}: "))
    impar_nota_acc = impar_nota_acc + impar
    if impar > impar_nota_maior:
        impar_nota_maior = impar
        impar_aluno_nota_maior = i

for i in range(2, alunos, 2):
    par = float(input(f"Você está digitando as notas dos alunos PARES. Por favor, insira a nota do aluno de numero {i}: "))
    par_nota_acc = par_nota_acc + par
    if par > par_nota_maior:
        par_nota_maior = par
        par_aluno_nota_maior = i

media_impar = impar_nota_acc / alunos_turma
media_par = par_nota_acc / alunos_turma

print(f"A media dos alunos impares é {media_impar}. A maior nota foi {impar_nota_maior} do aluno {impar_aluno_nota_maior}")
print(f"A media dos alunos pares é {media_par}. A maior nota foi {par_nota_maior} do aluno {par_aluno_nota_maior}")

