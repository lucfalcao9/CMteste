SELECT p.nome_paciente, pr.descricao_prontuario, a.data_atendimento
FROM Pacientes p
JOIN Prontuário pr ON p.id_paciente = pr.id_paciente
JOIN Atendimento a ON p.id_paciente = a.id_paciente
WHERE p.id_paciente = 123
