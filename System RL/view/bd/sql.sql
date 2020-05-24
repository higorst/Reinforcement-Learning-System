# quantidade de combinação
select count(c.id) Combinações
from combinacao c, experimento exp
where c.idExperimento = exp.id and exp.id = '1';

# combinações e seus parâmetros
select id Combinação, alpha, gamma, epsilon
from combinacao;

# quantidade de ensaios por combinação 
select c.id Combinação, count (e.id) Ensaios, c.alpha, c.gamma, c.epsilon
from combinacao c, ensaio e, ensaioRelacao er, experimento exp
where exp.id = '1' and
	  exp.id = er.idExperimento and
	  c.id = er.idCombinacao and
	  e.id = er.idEnsaio
group by c.id;

''' 

	1 - somar todos os saldos de gols por ensaio
	2 - média de todos os ensaios (saldo de gols) - resultado do item anterior

'''

# (1) saldo de gol por ensaio
select c.id Combinação, count (e.id) Ensaios, e.soma_saldo_gol SaldoGols, c.alpha, c.gamma, c.epsilon
from combinacao c, ensaio e, ensaioRelacao er, experimento exp
where exp.id = '1' and
	  exp.id = er.idExperimento and
	  c.id = er.idCombinacao and
	  e.id = er.idEnsaio
group by e.id;

# (2) média de saldo de gol por ensaio
select c.id Combinação, count (e.id) Ensaios, sum(e.soma_saldo_gol)/count(e.id) MédiaSaldoGols, c.alpha, c.gamma, c.epsilon
from combinacao c, ensaio e, ensaioRelacao er, experimento exp
where exp.id = '1' and
	  exp.id = er.idExperimento and
	  c.id = er.idCombinacao and
	  e.id = er.idEnsaio
group by c.id;

# número máximo de ensaios entre combinações de um experimento
select max(m.ensaios) as ensaios
from (
	select count (e.id) as ensaios
	from combinacao c, ensaio e, ensaioRelacao er, experimento exp
	where exp.id = '1' and
		  exp.id = er.idExperimento and
		  c.id = er.idCombinacao and
		  e.id = er.idEnsaio
	group by c.id
) as m;