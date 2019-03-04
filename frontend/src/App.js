import React, { Component } from 'react';
import TodoList from './components/todos/TodoList'

class App extends Component {
  state = {
    todos: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://localhost:8000/api/')
      const todos = await res.json()
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {

    const todos = [
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
      }
    ]

    return (
      <div>
        <h1>Django Todo</h1>
        <TodoList todos={todos} />
      </div>
    );
  }
}

export default App;
