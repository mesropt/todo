import './App.css';
import React from 'react';
import Header from "./components/Header";
import {BrowserRouter as Router, Route, Routes, Navigate} from "react-router-dom";
import ProjectList from "./components/Projects";
import UserList from "./components/Users";
import ToDoList from "./components/ToDos";
import Footer from "./components/Footer";
import {PageNotFound404} from "./components/Base";


class App extends React.Component {

    constructor(props) {
    super(props)
    const user1 = {id: 1, username: 'Грин', firstname: '1880', lastname: 'Грин', email: 'ddd@gmail.com'}
    const user2 = {id: 2, username: 'Грин', firstname: '1880', lastname: 'Грин', email: 'ddd@gmail.com'}
    const users = [user1, user2]
    const project1 = {id: 1, project_name: 'Алые паруса', repository_link: 'dd'}
    const project2 = {id: 2, project_name: 'Алые паруса', repository_link: 'dd'}
    const projects = [project1, project2]
    const todo1 = {id: 1, project: 'Алые паруса', note_text: 'author1', date_created: 1890, date_updated: 1900, execution_status: 'dd'}
    const todo2 = {id: 1, project: 'Алые паруса', note_text: 'author1', date_created: 1890, date_updated: 1900, execution_status: 'dd'}
    const todos = [todo1, todo2]
    this.state = {
      'users': users,
      'projects': projects,
      'todos': todos
    }
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