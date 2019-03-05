import React from 'react';
import Task from './Task';


const TodoList = ({ tasks }) => (

    <ul>
        {
            tasks.map(task => (
                    <Task
                    title={task.title}
                    description={task.description}
                    deadline={task.deadline}
                    status= {task.status}
                    responsible={task.responsible}
                    />
                ))
        }
    </ul>
)

export default TodoList