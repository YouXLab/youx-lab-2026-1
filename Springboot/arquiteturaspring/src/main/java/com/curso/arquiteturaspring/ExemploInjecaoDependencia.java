package com.curso.arquiteturaspring;

import com.curso.arquiteturaspring.todos.MailSender;
import com.curso.arquiteturaspring.todos.TodoRepository;
import com.curso.arquiteturaspring.todos.TodoService;
import com.curso.arquiteturaspring.todos.TodoValidator;
import jakarta.persistence.EntityManager;
import org.springframework.data.jpa.repository.support.SimpleJpaRepository;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import javax.sql.DataSource;
import javax.swing.text.html.parser.Entity;
import java.sql.Connection;

public class ExemploInjecaoDependencia {

    public static void main(String[] args) throws Exception {
        DataSource dataSource = new DriverManagerDataSource();
        /*dataSource.setUrl("url");
        dataSource.setUsername("user");
        dataSource.setPassword("password");*/

        Connection connection = dataSource.getConnection();

        EntityManager entityManager = null;

        TodoRepository repository = null; // new SimpleJpaRepository<TodoRepository, Integer>(null, null);
        TodoValidator todoValidator = new TodoValidator(repository);
        MailSender sender = new MailSender();

        TodoService todoService = new TodoService(repository, todoValidator, sender);

//        BeanGerenciado beanGerenciado = new BeanGerenciado(null);
//        beanGerenciado.setValidator(todoValidator);
//        if(condicao == true) {
//            beanGerenciado.setValidator();
//        }
    }
}
