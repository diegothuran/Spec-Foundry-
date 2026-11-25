# Guardrails por domínio sensível

Em domínio sensível, a spec pode causar dano se estiver errada. Aumentar rigor, não velocidade.

## Saúde

- Dado de saúde é sensível (LGPD art. 11): consentimento, finalidade e retenção precisam estar escritos.
- Software que influencia diagnóstico pode ser SaMD (RDC 657/2022): classificar antes de prometer "não é dispositivo médico".
- Rastreabilidade de laudo, identificação de paciente e controle de acesso são requisitos P0, não melhorias.
- Nunca afirmar conformidade com RDC, ISO 15189 ou HL7 sem auditoria formal. Escrever "desenhado para atender X", com a pendência explícita.
- Fluxo de resultado crítico precisa de regra de comunicação, não só de flag.

## Jurídico

- Distinguir fato de interpretação. Citar dispositivo, não "a lei diz".
- Não opinar sobre caso concreto sem qualificação; entregar estrutura de análise.
- Prazos e competências mudam: registrar data de consulta da norma.

## Financeiro

- Toda projeção precisa de premissa explícita e fonte de cada número.
- Separar realizado, estimado e desejado. Misturar os três é o erro mais comum.
- Cálculo sensível (juros, tributos) merece teste com valor conhecido.

## Dados pessoais (qualquer domínio)

- Minimização: coletar só o necessário, com justificativa.
- Retenção declarada com prazo e responsável.
- Direito de exclusão precisa de caminho técnico, não só de promessa.

## Como registrar limite de domínio

> Este pacote foi desenhado para atender aos requisitos de rastreabilidade da RDC 978/2025 no que se refere a registro de laudo e trilha de auditoria. **Não** houve auditoria formal, nem validação clínica. A conformidade completa exige revisão por responsável técnico e processo de validação de software.

Isso é entrega profissional. "Está conforme" sem auditoria é risco transferido ao cliente sem aviso.
