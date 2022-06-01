import React from 'react';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import ToDoList from './components/ToDo.js';
import {BrowserRouter, Route, Routes, Link} from "react-router-dom";

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
                <BrowserRouter>
                  <nav>
                    <ul>
                      <li>
                        <Link to="/">Users</Link>
                      </li>
                      <li>
                        <Link to="/projects">Projects</Link>
                      </li>
                      <li>
                        <Link to="/todos">ToDos</Link>
                      </li>
                    </ul>
                  </nav>
                    <Routes>
                        <Route exact path="/" element={<ProjectList items={this.state.projects}/>}/>
                        <Route exact path="/users" element={<UserList items={this.state.users}/>}/>
                        <Route exact path="/todos" element={<ToDoList items={this.state.todos}/>}/>
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;