import React from 'react';
import axios from 'axios';
import logo from './logo.svg'; // Лого мы удалили, можно без этого импорта.
import './App.css'; // Подгрузка стилей.
import AuthorList from './components/Author.js';
import UserList from './components/User.js';
import FooterItem from './components/Footer.js';
import MenuItem from './components/Menu.js';

class App extends React.Component { // Создаём класс App, который наследуется от React.Component. Класс App в нашей One Way Data Flow является верхним и самым главным, имеет состояние. Все остальные компоненты будут простыми функциями в рамках нашей реализации.
  constructor(props) { // В конструктор класс передаём объект props (constructor в JS как init в Python).
    super(props) // Вызываем объект props.
    this.state = { // Объявляем состояние (this в JS как self в Python). То есть глобальное состояние есть только у класс App. Оно объявлено через этот this.
      'users': [] // В users мы будем хранить массив наших авторов, которые мы будем получать с бекенда.
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users') // get-запрос к урлу, который нас интересует.
      .then(response => { // Получаем response, через который забираем data (данные).
        const users = response.data
          this.setState( // Изменяем state.
          {
            'users': users
          }
        )
      }).catch(error => console.log(error)) // Используя catch ловим ошибки и выводим их в log.
  }

  render () { // Данный метод отвечает за отрисовку нашего компонента (то есть так же, как в Django был такой же метод, который рендерил наши templates).
    return ( // Нижу внутри div можно писать по факту что угодно. Здесь используются div, то есть это сама html, которая будет рендериться.
        <div>
          <MenuItem menu={'Menu'} />
          <UserList users={this.state.users} />
          <FooterItem footer={'Footer'} />
        </div>
    )
  }
}

export default App; // Эта функция означает, что мы экспортируем наш компонент для использования в других модулях. Например, если мы откроем файл index.js, то увидим, то в нём используется App.js
