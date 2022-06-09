import './App.css';
import React from 'react';
import axios from 'axios';
import Header from "./components/Header";
import {BrowserRouter as Router, Route, Routes, Navigate, Link} from "react-router-dom";
import ProjectList  from "./components/Projects";
import UserList from "./components/Users";
import ToDoList from "./components/ToDos";
import LoginForm from './components/Auth.js';
import Footer from "./components/Footer";
import {PageNotFound404} from "./components/Base";
import Cookies from 'universal-cookie'


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

    set_token(token) { /*Устанавливаем кукки*/
        const cookies = new Cookies()
        cookies.set('token', token)
        //localStorage.setItem('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() { /*Проверяет есть ли у нас вообще токен*/
        return this.state.token != ''
    }

    logout() { /*Разлогинимься, то есть устанавливаем токен в пустоту, то есть затираем его*/
        this.set_token('')
    }

    get_token_from_storage() { /*Получаем токен их зранилиша*/
        const cookies = new Cookies()
        const token = cookies.get('token') /*Устанавливаем токен, получаем его из кук, ставим его ниже в state сайта*/
        // const token = localStorage.getItem('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(username, password) { /*Захардкоженный локалхост*/
        axios.post('http://127.0.0.1:8000/api/token-auth/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers(){ /*Получаем headers*/
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
        axios.get('http://127.0.0.1:8000/projects', {headers})
            .then(response => {
                this.setState({authors: response.data})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/todos', {headers})
            .then(response => {
                this.setState({books: response.data})
            }).catch(error => {
                console.log(error)
            this.setState({books: []})
        })
    }


    componentDidMount() {
        this.load_data()
    }

/*    axios.get('http://127.0.0.1:8000/projects')
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
  }*/

    render() {
        return (
            <div className="App">
                <Router>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/'>ToDos</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route exact path="/" element={<ProjectList items={this.state.projects} />} />
                        <Route exact path="/users" element={<UserList items={this.state.users} />} />
                        <Route exact path="/todos" element={<ToDoList items={this.state.todos} />} />
                        <Route exact path="/login" element={<LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
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