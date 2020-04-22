import React, { component, Component }  from 'react';
import logo from './logo.svg';
import './App.css';

import axios from 'axios';

/*
const list = [
  {
    "id":1,
    "title":"1st todo",
    "body":"Learn Django proerly"
  },
  {
    "id":2,
    "title":"second item",
    "body":"Learn python"
  },
  {
    "id":3,
    "title":"Learn HTTP",
    "body":"Learn RestzFUll API"
  },
]

class App extends Component {
  constructor(props) {
    super(props)
    this.state = { list };
  }

  render() {
    return (
      <div>
        {this.state.list.map(item => (
        <div key={item.id}>
          <h1>{item.title}</h1>
          <p>{item.body}</p>
      </div>
      ))}
      </div>
      );
      }
      }

*/

class App extends Component {

  state = {
    todos: []
  };


//new
componentDidMount() {
  this.getTodos();
  }

  getTodos() {
  axios
    .get('http://127.0.0.1:8000/api/')
    .then( res =>{
      this.setState({ todos: res.data });
    })
    .catch(err => {
      console.log(err);
      });
    }

    render() {
      return (
        <div>
          {this.state.todos.map(item => (
            <div key={item.id}>
              <h1>{item.title}</h1>
              <span>{item.body}</span>
            </div>
        ))}
      </div>
      );
}

}



export default App;
