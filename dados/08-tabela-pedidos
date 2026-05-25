create table pedido (
	idpedido int primary key not null,
	idcliente int references cliente (idcliente) not null,
	idtransportadora int references transportadora (idtransportadora),
	idvendedor int references vendedor (idvendedor),
	data_pedido date not null,
	valor numeric(10,2) not null
)
alter table pedido drop valor
alter table pedido add valor float not null

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (1, '2008-04-01', 1300, 1, 2, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (2, '2008-04-01', 500, 1, 2, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (3, '2008-04-01', 500, 1, 2, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (4, '2008-04-05', 1000, 8, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (5, '2008-04-06', 200, 9, 2, 6);

select * from transportadora
select * from pedido
select * from vendedor
select * from cliente
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (6, '2008-04-06', 1985, 10, 1, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (7, '2008-04-06', 800, 3, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (8, '2008-04-06', 175, 3, null, 7);	
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (9, '2008-04-07', 1300, 12, null, 8);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (10, '2008-04-10', 200, 6, 1, 8);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (11, '2008-04-15', 300, 15, 2, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (12, '2008-04-20', 300, 15, 2, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (13, '2008-04-20', 350, 9, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (14, '2008-04-23', 300, 2, 1, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (15, '2008-04-25', 200, 11, null, 5);