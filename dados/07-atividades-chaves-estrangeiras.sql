create table fornecedor (
	idfornecedor int not null primary key,
	nome varchar(50) unique not null
)
 create table vendedor (
	idvendedor int primary key not null,
	nome varchar(50) unique not null
 )
 create table transportadora (
	idtransportadora int  primary key not null,
	idmunicipio int references municipio (id),
	nome varchar(50) unique not null,
	logradouro varchar(50),
	numero varchar(10)
 )
create table produto (
	idproduto int primary key not null,
	idfornecedor int references municipio (id) not null,
	nome varchar(50) not null,
	valor numeric(10,2) not null
)


insert into produto (idproduto, idfornecedor, nome, valor) values (1, 1, 'Microcomputador', 800);
insert into produto (idproduto, idfornecedor, nome, valor) values (2, 1, 'Monitor', 500);
insert into produto (idproduto, idfornecedor, nome, valor) values (3, 2, 'Placa mãe', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (4, 2, 'HD', 150);
insert into produto (idproduto, idfornecedor, nome, valor) values (5, 2, 'Placa de vídeo', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (6, 3, 'Memória RAM', 100);
insert into produto (idproduto, idfornecedor, nome, valor) values (7, 1, 'Gabinete', 35);

select * from fornecedor