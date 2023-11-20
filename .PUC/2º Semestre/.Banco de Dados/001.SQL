CREATE DATABASE cadastro; #Cria o Banco de dados

USE cadastro;

CREATE TABLE pessoas (
	id int NOT NULL AUTO_INCREMENT, #Chave primaria que e utilizada como identificador
    nome varchar(20),
    nascimento date, #Data de nascimento 
    sexo enum('M', 'F'), #Sexo sempre será M para masculino e F para feminino
    peso decimal(5, 2), #O peso será por padrao 5 numeros 3 antes da virgola e 2 depois
    altura decimal(3,2), #A altura será por padrao 3 numeros 2 antes da virgola e 2 depois
    nacionalidade varchar(20) DEFAULT 'Brasil', #Limitado a 20 caracteres, os nao usados nao ocuparao memoria 
    PRIMARY KEY(id)
);



ALTER TABLE pessoas 
ADD COLUMN profissao varchar (10) DEFAULT 'Estudante' AFTER nome;

ALTER TABLE pessoas 
MODIFY COLUMN profissao varchar (20);

alter table pessoas
drop column profissao;

INSERT INTO pessoas 
	(nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
	('Adriano', '2005-03-16', 'M', '70.0', '1.86', 'Brasil');
    
INSERT INTO pessoas 
	(nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
	('Pedro', '2005-01-05', 'M', '75.0', '1.88', 'Estados Unidos'),
    ('Teo', '2005-01-05', 'M', '60.0', '1.77', 'Brasil'),
    ('Caio', '2006-05-21', 'M', '60.0', '1.60', 'Israel'),
	('Ary', '2005-01-22', 'M', '65.0', '1.70', 'Brasil');
    
    
    
INSERT INTO pessoas (nome, nascimento, sexo, peso, altura, nacionalidade) 
VALUES
	('Lucas', '2004-03-12', 'M', '68.0', '1.82', 'França'),
	('Marta', '2003-07-19', 'F', '55.0', '1.65', 'Itália'),
	('Rafael', '2002-06-30', 'M', '77.0', '1.78', 'Espanha'),
	('Sofia', '2001-05-14', 'F', '60.0', '1.70', 'Portugal'),
	('Diego', '2000-04-22', 'M', '82.0', '1.85', 'México'),
	('Isabela', '1999-08-09', 'F', '58.0', '1.60', 'Argentina'),
	('João', '1998-12-05', 'M', '75.0', '1.76', 'Brasil'),
	('Ana', '1997-10-20', 'F', '62.0', '1.68', 'Canadá'),
	('Felipe', '1996-09-15', 'M', '70.0', '1.72', 'Estados Unidos'),
	('Lara', '1995-08-10', 'F', '56.0', '1.67', 'Chile'),
	('Gustavo', '1994-07-06', 'M', '78.0', '1.80', 'Colômbia'),
	('Julia', '1993-06-02', 'F', '59.0', '1.64', 'Alemanha'),
	('Henrique', '1992-04-28', 'M', '73.0', '1.77', 'Rússia'),
	('Carla', '1991-03-25', 'F', '61.0', '1.69', 'Índia'),
	('André', '1990-02-18', 'M', '80.0', '1.83', 'Japão'),
	('Fernanda', '1989-01-14', 'F', '57.0', '1.66', 'Austrália'),
	('Bruno', '1988-12-11', 'M', '76.0', '1.79', 'Noruega'),	
	('Camila', '1987-11-07', 'F', '63.0', '1.70', 'Suécia'),
	('Leonardo', '1986-10-04', 'M', '81.0', '1.84', 'Finlândia'),
	('Patricia', '1985-09-01', 'F', '58.0', '1.65', 'Dinamarca'),
	('Eduardo', '1984-07-29', 'M', '77.0', '1.78', 'Grécia'),
	('Vanessa', '1983-06-26', 'F', '62.0', '1.67', 'Turquia'),
	('Marcos', '1982-05-23', 'M', '79.0', '1.82', 'Egito'),
	('Bianca', '1981-04-20', 'F', '60.0', '1.68', 'África do Sul'),
	('Roberto', '1980-03-18', 'M', '83.0', '1.85', 'Nova Zelândia'),
	('Daniela', '1979-02-12', 'F', '59.0', '1.66', 'Israel'),
	('Paulo', '1978-01-09', 'M', '74.0', '1.75', 'China'),
	('Aline', '1977-12-06', 'F', '61.0', '1.64', 'Coreia do Sul');

SELECT id, nome, nascimento, nacionalidade FROM pessoas
ORDER BY altura;



#----------------------------------------------------------------------------------------------------------


CREATE TABLE IF NOT EXISTS cursos (
	nome varchar(20) NOT NULL UNIQUE,
    descricao text,
    carga int,
    totalaulas int,
    ano year DEFAULT '2023'
);


ALTER TABLE cursos
MODIFY nome varchar(50);

ALTER TABLE cursos 
ADD PRIMARY KEY(idcurso);

INSERT INTO cursos VALUES
	('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
	('2','Algoritimos','Logica de Programação','20','8','2014'),
	('3','Photoshop','Aulas de Photoshop CC','9','20','2014'),
	('4','PGP','PHP para Iniciantes','33','40','2010'),
	('5','Jarva','Intro ao Java','22','10','2000'),
	('6','MySQL','Curso MySQL','21','15','2016'),
	('7','World','Word Completo','40','30','2018'),
	('8','Sapateado','Dança Rítimica','14','30','2018'),
	('9','Cozinha Árabe','Aprenda a fazer Kibe','40','30','2018'),
	('10','YouTuber','Gerar Polêmicas e Ganhar Inscritos','5','2','2010');
    
INSERT INTO cursos VALUES
('11', 'Python Básico', 'Introdução à programação com Python', '30', '25', '2020'),
('12', 'JavaScript Avançado', 'Desenvolvimento avançado em JavaScript', '25', '20', '2021'),
('13', 'Desenvolvimento Web', 'HTML, CSS e JavaScript para web', '35', '30', '2019'),
('14', 'React Native', 'Criação de apps com React Native', '20', '15', '2021'),
('15', 'Inteligência Artificial', 'Fundamentos de IA e machine learning', '40', '35', '2018'),
('16', 'Django Framework', 'Desenvolvimento web com Django', '18', '12', '2020'),
('17', 'Ruby on Rails', 'Criação de aplicações web com Ruby on Rails', '22', '18', '2019'),
('18', 'Node.js', 'Back-end com Node.js', '28', '23', '2022'),
('19', 'Desenvolvimento Android', 'Curso básico de Android com Java', '33', '27', '2018'),
('20', 'Swift para iOS', 'Desenvolvimento de apps para iOS com Swift', '30', '25', '2021'),
('21', 'C# Fundamentos', 'Conceitos básicos de programação em C#', '26', '21', '2019'),
('22', 'ASP.NET MVC', 'Desenvolvimento web com ASP.NET MVC', '32', '26', '2020'),
('23', 'SQL Básico', 'Fundamentos de bancos de dados SQL', '24', '19', '2018'),
('24', 'MongoDB', 'NoSQL com MongoDB', '20', '16', '2022'),
('25', 'Bootstrap 4', 'Front-end responsivo com Bootstrap', '15', '10', '2019'),
('26', 'Angular', 'Desenvolvimento front-end com Angular', '35', '30', '2021'),
('27', 'Data Science', 'Introdução à Ciência de Dados', '40', '35', '2020'),
('28', 'Machine Learning', 'Algoritmos de aprendizado de máquina', '30', '25', '2022'),
('29', 'Docker', 'Contêineres e virtualização com Docker', '18', '14', '2021'),
('30', 'Git e GitHub', 'Controle de versão com Git e GitHub', '22', '17', '2019'),
('31', 'Kotlin Básico', 'Desenvolvimento Android com Kotlin', '25', '20', '2020'),
('32', 'Flutter', 'Criação de apps multiplataforma com Flutter', '28', '23', '2021'),
('33', 'Blockchain', 'Fundamentos de tecnologia blockchain', '30', '25', '2018'),
('34', 'Raspberry Pi', 'Projetos com Raspberry Pi', '20', '15', '2019'),
('35', 'Arduino', 'Programação e projetos com Arduino', '25', '20', '2020'),
('36', 'Cloud Computing', 'Fundamentos de computação em nuvem', '30', '25', '2021'),
('37', 'Cybersecurity', 'Princípios básicos de segurança cibernética', '35', '30', '2019'),
('38', 'UX/UI Design', 'Design de experiência e interface do usuário', '22', '18', '2020'),
('39', 'Big Data', 'Introdução ao Big Data', '28', '23', '2018'),
('40', 'DevOps', 'Práticas e ferramentas para DevOps', '26', '21', '2022'),
('41', 'Vue.js', 'Framework Vue.js para front-end', '24', '19', '2021'),
('42', 'Scrum e Agile', 'Metodologias ágeis para gestão de projetos', '20', '16', '2019'),
('43', 'Power BI', 'Análise de dados com Power BI', '30', '25', '2020'),
('44', 'Excel Avançado', 'Técnicas avançadas em Excel', '18', '14', '2018');


SELECT ano, nome, carga FROM cursos
WHERE ano = '2022'
ORDER BY ano;

SELECT * FROM pessoas
WHERE nome NOT LIKE '%a%';




UPDATE cursos
SET nome = 'java', ano = '2010', carga = '40'
WHERE idcurso = 5;

DELETE FROM cursos 
WHERE idcurso = '8';



#PESSOAS
SELECT * FROM pessoas;

DROP TABLE pessoas;

#CURSOS
SELECT * FROM cursos