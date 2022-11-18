/* No terminal apos executar sqlite, execute o seguinte comaando para poder ver o nome de todas as musicas */

SELECT name FROM songs

/* Para classificar os nomes em ordem crescente usamos esse comando */
/* ORDER BY e usado para classificar o conjuto de resultados em ordem crescente ou decrescente */

SELECT name FROM songs ORDER BY tempo;

/* 
DESC e usado para classificar os dados retornados em ordem decrescente 
LIMIT e usado para especificar o numero de registros a serem retornados
*/
SELECT name FROM songs ORDER BY duration_ms DESC LIMIT 5;

