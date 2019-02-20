import React, { Component } from 'react';
import Navbar from './Navbar'

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
    return (
      <div>
        <Navbar />
      </div>
    );
  }
}

export default App;
