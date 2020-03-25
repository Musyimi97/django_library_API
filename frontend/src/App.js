import React, { Component } from 'react';
import axios from 'axios';


const list = [
  {
  "id": 1,
  "title": "Learn React",
  "body": "just trymmma list aout an example"
}, {
  "id": 2,
  "title": "Learn React",
  "body": "Its quite popular"
}, {
  "id": 3,
  "title": "Learn Python",
  "body": "Its endearing"
}, {
  "id": 4,
  "title": "Learn Vue",
  "body": "it graphical"
}
]


class App extends Component{
  state = {
    todos:[]
  };
  componentDidMount(){
    this.getTodos();
  }
  getTodos(){
    axios
      .get('http:/12.0.0.1:8000/api/todos/')
      .then(res => {
        this.setState({
          todos:res.data
        });
      })
      .catch(err =>{
        console.log(err);
      });
  }
  render(){
    return (
      <div>
        {this.state.todos.map(item =>(
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