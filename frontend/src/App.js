import React, { Component } from 'react';


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
  constructor(props){
    super(props);
    this.state = {list}
  }
  render(){
    return (
      <div>
        {this.state.list.map(item =>(
          <div key={item.id}>
          <h1>{item.title}</h1>
          <h1>{item.body}</h1>

          </div>
        ))}
      </div>
    );
  }
}
export default App;