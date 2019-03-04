import React from 'react';
import Todo from './Todo';


const TodoList = ({ todos }) => (

    <ul>
        {
            todos.map(todo => (
                    <Todo
                    title={todo.title}
                    description={todo.description}
                    deadline={todo.deadline}
                    status= {todo.status}
                    responsible={todo.responsible}
                    />
                ))
        }
    </ul>
)

export default TodoList