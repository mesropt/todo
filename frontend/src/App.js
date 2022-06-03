import './App.css';
import React from 'react';
import axios from 'axios';
import Header from "./components/Header";
import {BrowserRouter as Router, Route, Routes, Navigate} from "react-router-dom";
import ProjectList  from "./components/Projects";
import UserList from "./components/Users";
import ToDoList from "./components/ToDos";
import Footer from "./components/Footer";
import {PageNotFound404} from "./components/Base";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'projects': [],
            'todos': [],
            'users': []
        }
    }


  componentDidMount() {
    axios.get('http://127.0.0.1:8000/users')
      .then(response => {
        const users = response.data
          this.setState(
          {
            'users': users.results
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/projects')
    .then(response => {
      const projects = response.data
        this.setState(
        {
          'projects': projects.results
        }
      )
    }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/todos')
    .then(response => {
      const todos = response.data
        this.setState(
        {
          'todos': todos.results
        }
      )
    }).catch(error => console.log(error))
  }

    render() {
        return (
            <div className="App">
                <Router>
                    <div className={"container d-flex justify-content-between"}>
                        <Header/>
                    </div>
                    <Routes>
                        <Route exact path="/" element={<ProjectList items={this.state.projects}/>}/>
                        <Route exact path="/users" element={<UserList items={this.state.users}/>}/>
                        <Route exact path="/todos" element={<ToDoList items={this.state.todos}/>}/>
                        <Route path="/projects" element={<Navigate replace to="/"/>}/>
                        <Route exact path="*" element={<PageNotFound404/>}/>
                    </Routes>
                </Router>
                <Footer/>
            </div>
        )
    }
}

export default App;