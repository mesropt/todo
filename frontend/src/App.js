import './App.css';
import React from 'react';
import axios from 'axios';
import Menu from "./components/Menu";
import {BrowserRouter as Router, Route, Routes, Navigate, Link} from "react-router-dom";
import ProjectList  from "./components/Projects";
import UserList from "./components/Users";
import ToDoList from "./components/ToDos";
import Footer from "./components/Footer";
import {PageNotFound404} from "./components/Base";
import LoginForm from "./components/Auth";
import Cookies from 'universal-cookie';

const client = axios.create(
    { baseURL: 'http://localhost:8000/' }
)

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'projects': [],
            'todos': [],
            'users': [],
            'token': ''
        }
    }

   set_token(token) {
       const cookies = new Cookies()
       cookies.set('token', token)
       this.setState({'token': token}, ()=>this.load_data())
   }

   is_authenticated() {
       return this.state.token !== ''
   }

   logout() {
       this.set_token('')
   }

   get_token_from_storage() {
       const cookies = new Cookies()
       const token = cookies.get('token')
       this.setState({'token': token}, ()=>this.load_data())
   }

   get_token(username, password) {
       axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
           .then(response => {
               this.set_token(response.data['token'])
           }).catch(error => alert('Неверный логин или пароль'))
   }

   get_headers() {
       let headers = {
           'Content-Type': 'application/json'
       }
       if (this.is_authenticated())
       {
           headers['Authorization'] = 'Token ' + this.state.token
       }
       return headers
   }

   load_data() {

       const headers = this.get_headers()
       client.get('projects/', {headers})
       .then(response => {
           const projects = response.data.results
               this.setState({'projects': projects})
       }).catch(error => console.log(error))

       client.get('todos/', {headers})
       .then(response => {
           const todos = response.data.results
               this.setState({'todos': todos}
           )
       }).catch(error => console.log(error))

       client.get('users/', {headers})
       .then(response => {
           const users = response.data.results
               this.setState({'users': users})
       }).catch(error => console.log(error))
   }

   componentDidMount() {
       this.get_token_from_storage()
   }

    render() {
        return (
            <div className="App">
                <Router>
                    <div className="container-fluid">
                        <nav
                            className="navbar navbar-expand-lg navbar-light bg-light">
                            <Menu/>
                        </nav>
                        <div>
                            {this.is_authenticated() ? <button
                                    onClick={() => this.logout()}>Выйти</button> :
                                <Link to='/login'>
                                    <button>Войти</button>
                                </Link>}
                        </div>
                    </div>
                    <Routes>
                        <Route exact path="/" element={<ProjectList items={this.state.projects}/>}/>
                        <Route exact path="/users" element={<UserList items={this.state.users}/>}/>
                        <Route exact path="/todos" element={<ToDoList items={this.state.todos}/>}/>
                        <Route path="/projects" element={<Navigate replace to="/"/>}/>
                        <Route path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route exact path="*" element={<PageNotFound404/>}/>
                    </Routes>
                </Router>
                <Footer/>
            </div>
        )
    }
}

export default App;