import React, { Component } from 'react';
import TodoList from './components/todos/TodoList'
import './App.css';

class App extends Component {
   render() {

    const todo = {
        'title': 'My todo',
        'owner': 'David',
        'tasks': [
          {
            'title': 'Todo 1',
            'description': 'Todo Text',
            'deadline': '22/03/2019',
            'status': false,
            'responsible': 'David' 
          },
          {
            'title': 'Todo 2',
            'description': 'Todo Description',
            'deadline': '23/03/2019',
            'status': true,
            'responsible': 'William' 
          },
          {
            'title': 'Todo 3',
            'description': 'Another Todo Text',
            'deadline': '24/03/2019',
            'status': false,
            'responsible': 'Josh' 
          },
          {
            'title': 'Aprender react',
            'description': 'Pra manjar dos js tudo',
            'deadline': '22/03/2019',
            'status': false,
            'responsible': 'David' 
          }
        ],
        'contributors': ['Donatello', 'Michelangelo', 'Leonardo', 'Rafael']
      }
      
      const contributorsList = todo.contributors.map((contributor) =>
        <li className='contributorsList'>{contributor}</li>
      );

      return (
        <div>
          <h1>{ todo.title }</h1>
          <h4>{ todo.owner }</h4>
          <p>Contributors:</p>
          <ul>{ contributorsList }</ul>
          <TodoList tasks={todo.tasks} />
        </div>
    );
  }
}

export default App;
