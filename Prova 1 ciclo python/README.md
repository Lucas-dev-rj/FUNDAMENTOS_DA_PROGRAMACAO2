# Sistema de Gestão de Pacientes e Atendimentos

Projeto do Ciclo 01  Avaliativo 2 de Fundamentos da Programação.

## O que o programa faz

Simula um sisteminha de gerenciamento de pacientes de uma clínica médica,
usando os conceitos de Orientação a Objetos que vimos em aula:

- **Herança**: `PacienteParticular` e `PacienteConvenio` herdam de `Paciente`.
- **Encapsulamento**: o CPF é guardado como atributo protegido (`_cpf`).
- **Polimorfismo**: o método `exibir_informacoes()` é sobrescrito nas duas
  subclasses, mas continua usando o `super()` para reaproveitar o
  comportamento da classe mãe.

## Classes

- `Paciente` (superclasse): nome, data de nascimento, CPF, telefone, tipo
  sanguíneo e número de prontuário.
- `PacienteParticular`: adiciona forma de pagamento e desconto de fidelidade,
  e calcula o valor final da consulta.
- `PacienteConvenio`: adiciona nome do convênio e número da carteirinha, e
  registra autorizações de procedimentos.

## Como rodar

```bash
python3 sistema_pacientes.py
```


